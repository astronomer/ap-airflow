#!/usr/bin/env python3
"""
This file is for configuration testing Airflow images.
The Airflow image is started in Docker, configured to access an
instance of postgres, which is also running in Docker.

Testinfra is used to configuration test the image. In effect,
testinfra simplifies and provides syntactic sugar for doing
execs into a running container.
"""

import json
import os
import pytest
import subprocess
import testinfra
import docker
from time import sleep

from packaging.version import parse as semantic_version


def test_airflow_in_path(webserver):
    """ Ensure Airflow is in PATH
    """
    assert webserver.exists('airflow'), \
        "Expected 'airflow' to be in PATH"


def test_tini_in_path(webserver):
    """ Ensure 'tini' is in PATH
    """
    assert webserver.exists('tini'), \
        "Expected 'tini' to be in PATH"


def test_entrypoint(webserver):
    """ There should be a file '/entrypoint'
    """
    assert webserver.file("/entrypoint").exists, \
        "Expected to find /entrypoint"


def test_maintainer(webserver, docker_client):
    """ Ensure the Docker image label 'maintainer' is set correctly
    """
    maintainer = get_label(docker_client, 'maintainer')
    assert maintainer == "Astronomer <humans@astronomer.io>", \
        "'maintainer' label should be 'Astronomer <humans@astronomer.io>'"


def test_version(webserver, docker_client):
    """ Ensure the version of Airflow matches the Docker image label
    """
    airflow_version = get_label(docker_client, 'io.astronomer.docker.airflow.version')
    version_output = webserver.check_output('airflow version')
    assert airflow_version in version_output


def test_elasticsearch_version(webserver):
    """ Astronomer runs a version of ElasticSearch that requires
    our users to run the client code of version 5.5.3 or greater
    """
    try:
        elasticsearch_module = webserver.pip_package.get_packages()['elasticsearch']
    except KeyError:
        raise Exception("elasticsearch pip module is not installed")
    version = elasticsearch_module['version']
    assert semantic_version(version) >= semantic_version('5.5.3'), \
        "elasticsearch module must be version 5.5.3 or greater"


def test_werkzeug_version(webserver):
    """ Werkzeug pip module version >= 1.0.0 has an issue
    """
    try:
        werkzeug_module = webserver.pip_package.get_packages()['Werkzeug']
    except KeyError:
        raise Exception("Werkzeug pip module is not installed")
    version = werkzeug_module['version']
    assert semantic_version(version) < semantic_version('1.0.0'), \
        "Werkzeug pip module version must be less than 1.0.0"


def test_redis_version(webserver):
    """ Redis pip module version 3.4.0 has an issue in the Astronomer platform
    """
    try:
        redis_module = webserver.pip_package.get_packages()['redis']
    except KeyError:
        raise Exception("redis pip module is not installed")
    version = redis_module['version']
    assert semantic_version(version) != semantic_version('3.4.0'), \
        "redis module must not be 3.4.0"


def test_astronomer_airflow_check_version(webserver):
    """ astronomer-airflow-version-check 1.0.0 has an issue in the Astronomer platform
    """
    try:
        version_check_module = webserver.pip_package.get_packages()['astronomer-airflow-version-check']
    except KeyError:
        print("astronomer-airflow-version-check pip module is not installed")
        return
    version = version_check_module['version']
    assert semantic_version(version) >= semantic_version('1.0.1'), \
        "astronomer-airflow-version-check module must be greater than 1.0.0"


def test_airflow_connections(scheduler):
    """Test Connections can be added and deleted"""
    test_conn_uri = "postgresql://postgres_user:postgres_test@1.1.1.1:5432"
    test_conn_id = "test"

    # Assert Connection can be added
    assert f"Successfully added `conn_id`={test_conn_id} : {test_conn_uri}" in scheduler.check_output(
        'airflow connections -a --conn_uri %s --conn_id %s', test_conn_uri, test_conn_id)

    # Assert Connection can be removed
    assert f"Successfully deleted `conn_id`={test_conn_id}" in scheduler.check_output(
        'airflow connections -d --conn_id %s', test_conn_id)


def test_airflow_variables(scheduler):
    """Test Variables can be added, retrieved and deleted"""
    # Assert Variables can be added
    assert "" in scheduler.check_output("airflow variables --set test_key test_value")

    # Assert Variables can be retrieved
    assert "test_value" in scheduler.check_output("airflow variables --get test_key")

    # Assert Variables can be deleted
    assert "" in scheduler.check_output("airflow variables --delete test_key")


def test_list_dags(scheduler):
    """
    Create Example DAG and add it to Scheduler POD
    """
    airflow_list_dags_output = scheduler.check_output("airflow list_dags -r")
    assert "Number of DAGs: 1" in airflow_list_dags_output
    assert "example_dag" in airflow_list_dags_output


def test_airflow_trigger_dags(scheduler):
    """Test Triggering of DAGs & Pausing & Unpausing Dags"""

    assert "Dag: example_dag, paused: True" in scheduler.check_output("airflow pause example_dag")
    assert "Created <DagRun example_dag @ 2020-05-01T00:00:00+00:00: " \
           "test_run, externally triggered: True>" \
           in scheduler.check_output("airflow trigger_dag -r test_run -e 2020-05-01 example_dag")

    assert "Dag: example_dag, paused: False" in scheduler.check_output("airflow unpause example_dag")

    # Verify the DAG succeeds in 180 seconds
    timeout = 180
    sleep_count = 0
    sleep_time_between_polls = 5
    try_count = 0
    while "success" not in scheduler.check_output("airflow dag_state example_dag 2020-05-01"):
        sleep_count += sleep_time_between_polls
        sleep(sleep_time_between_polls)
        try_count += 1
        print("Try: ", try_count)
        if "failed" in scheduler.check_output("airflow dag_state example_dag 2020-05-01"):
            raise Exception("DAGRun failed !")
        if sleep_count >= timeout:
            print("Timed out waiting for DAG to succeed")
            break

    assert "success" in scheduler.check_output("airflow dag_state example_dag 2020-05-01")


def test_webserver_health_endpoint(webserver):
    """
    Test Webserver is able to reach the Database and check the health of Scheduler & Metadata DB
    """
    response = scheduler.check_output()
    json_response = json.loads(response)

    assert "metadatabase" in json_response
    assert json_response["metadatabase"]["status"] == "healthy"
    assert json_response["scheduler"]["status"] == "healthy"


@pytest.fixture(scope='session')
def webserver(request):
    """ This is the host fixture for testinfra. To read more, please see
    the testinfra documentation:
    https://testinfra.readthedocs.io/en/latest/examples.html#test-docker-images
    """
    namespace = os.environ.get('NAMESPACE')
    pod = os.environ.get('WEBSERVER_POD')
    yield testinfra.get_host(f'kubectl://{pod}?container=webserver&namespace={namespace}')


@pytest.fixture(scope='session')
def scheduler(request):
    """ This is the host fixture for testinfra. To read more, please see
    the testinfra documentation:
    https://testinfra.readthedocs.io/en/latest/examples.html#test-docker-images
    """
    namespace = os.environ.get('NAMESPACE')
    pod = os.environ.get('SCHEDULER_POD')
    yield testinfra.get_host(f'kubectl://{pod}?container=scheduler&namespace={namespace}')


@pytest.fixture(scope='session')
def docker_client(request):
    """ This is a text fixture for the docker client,
    should it be needed in a test
    """
    client = docker.from_env()
    yield client
    client.close()


def get_image_name():
    """ Fetch image name from an environment variable
    and inform the user if they are not using it right
    """
    try:
        return os.environ['AIRFLOW_IMAGE']
    except KeyError:
        raise Exception("Please provide docker image name to pytest using environment variable AIRFLOW_IMAGE")


def get_label(client, label):
    """ Fetch the value of a label from the image
    """
    image_name = get_image_name()
    image = client.images.get(image_name)
    try:
        return image.labels[label]
    except KeyError:
        raise Exception(f"Image should have a label '{label}'")


def start_postgres():
    """ Idempotently start a Postgres database
    """
    docker_client = docker.from_env()
    try:
        postgres = docker_client.containers.get('postgres')
    except docker.errors.NotFound:
        return subprocess.check_output(
            ['docker', 'run', '--rm',
             '--name', 'postgres',
             '-e', 'POSTGRES_PASSWORD=notsecretpassword',
             '-d', 'postgres:9.6.15']
        ).decode().strip()
    return postgres.short_id


def get_ip_from_id(_id):
    """ Return the Docker private network IP of a given Docker container ID
    """
    return subprocess.check_output(
        ['docker', 'inspect',
         '-f', '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}',
         _id]
    ).decode().strip()


def wait_for_container(_id):
    # It takes Docker a short time to start
    # the container. We want to make sure it's up
    # and running before handing off to be tested.
    found_container = False
    for _ in range(0, 100):
        output = subprocess.check_output("docker ps", shell=True).decode()
        if _id[:5] in output:
            found_container = True
            break
        sleep(0.1)
    if not found_container:
        raise Exception("Error: Docker container did not start running within 10 seconds. "
                        "It did not show up in the docker ps output")
