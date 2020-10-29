#!/usr/bin/env python3
"""
This file is for configuration testing Airflow images.
The Airflow image is started in Docker, configured to access an
instance of postgres, which is also running in Docker.

Testinfra is used to configuration test the image. In effect,
testinfra simplifies and provides syntactic sugar for doing
execs into a running container.
"""

import os
import docker
import pytest
import subprocess
import testinfra
from time import sleep
from enum import Enum

from packaging.version import parse as semantic_version


class ImageType(Enum):
    BASE = "base"
    ONBUILD = "onbuild"


airflow_version = os.environ.get("AIRFLOW_VERSION")
airflow_2 = True if airflow_version.startswith("2") else False


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
    airflow_ver = get_label(docker_client, 'io.astronomer.docker.airflow.version')
    assert airflow_ver == airflow_version

    version_output = webserver.check_output('airflow version')
    assert airflow_ver in version_output


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


@pytest.mark.skipif(airflow_2, reason="Not needed for Airflow>=2")
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

    if airflow_2:
        # Assert Connection can be added
        assert f"Successfully added `conn_id`={test_conn_id} : {test_conn_uri}" in scheduler.check_output(
            'airflow connections add --conn-uri %s %s', test_conn_uri, test_conn_id)

        # Assert Connection can be removed
        assert f"Successfully deleted `conn_id`={test_conn_id}" in scheduler.check_output(
            'airflow connections delete %s', test_conn_id)
    else:
        # Assert Connection can be added
        assert f"Successfully added `conn_id`={test_conn_id} : {test_conn_uri}" in scheduler.check_output(
            'airflow connections -a --conn_uri %s --conn_id %s', test_conn_uri, test_conn_id)

        # Assert Connection can be removed
        assert f"Successfully deleted `conn_id`={test_conn_id}" in scheduler.check_output(
            'airflow connections -d --conn_id %s', test_conn_id)


def test_airflow_variables(scheduler):
    """Test Variables can be added, retrieved and deleted"""
    if airflow_2:
        # Assert Variables can be added
        assert "" in scheduler.check_output("airflow variables set test_key test_value")

        # Assert Variables can be retrieved
        assert "test_value" in scheduler.check_output("airflow variables get test_key")

        # Assert Variables can be deleted
        assert "" in scheduler.check_output("airflow variables delete test_key")
    else:
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
    if airflow_2:
        airflow_list_dags_output = scheduler.check_output("airflow dags list")
    else:
        airflow_list_dags_output = scheduler.check_output("airflow list_dags -r")
        assert "Number of DAGs: 1" in airflow_list_dags_output

    assert "example_dag" in airflow_list_dags_output


def test_airflow_trigger_dags(scheduler):
    """Test Triggering of DAGs & Pausing & Unpausing Dags"""
    if airflow_2:
        pause_dag_command = "airflow dags pause example_dag"
        trigger_dag_command = "airflow dags trigger -r test_run -e 2020-05-01 example_dag"
        unpause_dag_command = "airflow dags unpause example_dag"
        dag_state_command = "airflow dags state example_dag 2020-05-01"
    else:
        pause_dag_command = "airflow pause example_dag"
        trigger_dag_command = "airflow trigger_dag -r test_run -e 2020-05-01 example_dag"
        unpause_dag_command = "airflow unpause example_dag"
        dag_state_command = "airflow dag_state example_dag 2020-05-01"

    assert "Dag: example_dag, paused: True" in scheduler.check_output(pause_dag_command)
    assert "Created <DagRun example_dag @ 2020-05-01T00:00:00+00:00: " \
           "test_run, externally triggered: True>" \
           in scheduler.check_output(trigger_dag_command)

    assert "Dag: example_dag, paused: False" in scheduler.check_output(unpause_dag_command)

    # Verify the DAG succeeds in 100 seconds
    timeout = 100
    sleep_count = 0
    sleep_time_between_polls = 5
    try_count = 0
    while "success" not in scheduler.check_output(dag_state_command):
        sleep_count += sleep_time_between_polls
        sleep(sleep_time_between_polls)
        try_count += 1
        print("Try: ", try_count)
        if "failed" in scheduler.run(dag_state_command).stdout.rstrip("\r\n"):
            print("Timed out waiting for DAG to succeed")
            print()
            print("Logs: ")
            subprocess.run(["kubectl", "logs", os.environ.get('SCHEDULER_POD'), os.environ.get('NAMESPACE')])
            raise Exception("DAGRun failed !")
        if sleep_count >= timeout:
            print("Timed out waiting for DAG to succeed")
            print()
            print("Logs: ")
            subprocess.run(["kubectl", "logs", os.environ.get('SCHEDULER_POD'), os.environ.get('NAMESPACE')])
            break

    assert "success" in scheduler.check_output(dag_state_command)


def test_airflow_configs(scheduler, docker_client):
    """Verify certain Airflow configurations"""
    distro = get_label(docker_client, "io.astronomer.docker.distro")

    if distro == "debian":
        config_file_path = "/usr/local/lib/python3.7/site-packages/airflow/config_templates/default_airflow.cfg"
        expected_run_as_user = "50000"
    elif distro == "alpine":
        config_file_path = "/usr/lib/python3.7/site-packages/airflow/config_templates/default_airflow.cfg"
        expected_run_as_user = "100"
    elif distro == "rhel":
        config_file_path = "/usr/local/lib/python3.6/site-packages/airflow/config_templates/default_airflow.cfg"
        expected_run_as_user = "100"
    else:
        config_file_path = "/usr/lib/python3.7/site-packages/airflow/config_templates/default_airflow.cfg"
        expected_run_as_user = ""

    if airflow_2:
        assert scheduler.check_output(
            f"cat {config_file_path} | "
            "grep '^lazy_load_plugins' | awk '{print $3}'"
        ) == "False", "[core] lazy_load_plugins needs to be False for astronomer-version-check plugin to work"
    else:
        # Confirm that run_as_user is the UID for astro user (and not root) for AC images
        assert scheduler.check_output(
            f"cat {config_file_path} | "
            "grep '^run_as_user' | awk '{print $3}'").strip() == expected_run_as_user

    if semantic_version(airflow_version) >= semantic_version('1.10.7'):
        assert scheduler.check_output(
            f"cat {config_file_path} | "
            "grep '^update_fab_perms' | awk '{print $3}'"
        ) == "False", "[webserver] update_fab_perms needs to be False for AC >= 1.10.10"


def test_labels_for_onbuild_image(docker_client):
    """ Ensure correct labels exists on onbuild image """
    labels = get_labels(docker_client, ImageType.ONBUILD.value)
    assert labels['io.astronomer.docker.airflow.onbuild'] == "true"
    assert labels['maintainer'] == "Astronomer <humans@astronomer.io>", \
        "'maintainer' label should be 'Astronomer <humans@astronomer.io>'"


def test_apache_airflow_in_requirements(tmp_path):
    """
    Add test to check that docker build errors when apache-airflow is specified
    in requirements.txt for an onbuild image
    """
    test_project = tmp_path / "test_project"
    test_project.mkdir()
    image_name = get_image_name(ImageType.ONBUILD.value)

    restricted_value_patterns = [
        "apache-airflow==1.10.10", "apache-airflow>=1.10.5", "apache-airflow~=1.10.7",
        "apache-airflow == 1.10.10",
    ]

    (test_project / "Dockerfile").write_text(f"FROM {image_name}")
    (test_project / "packages.txt").touch()
    for restricted_value in restricted_value_patterns:
        (test_project / "requirements.txt").write_text(restricted_value)
        output = subprocess.run(
            ['docker', 'build', '-t', 'testimage', test_project.resolve()], capture_output=True)
        assert output.returncode == 1
        assert b"Do not upgrade by specifying 'apache-airflow' in your requirements.txt" in output.stderr

    # Test that you can still use backport-packages that start with "apache-airflow"
    (test_project / "requirements.txt").write_text("apache-airflow-backport-providers-amazon")
    output = subprocess.run(['docker', 'build', '-t', 'testimage', test_project.resolve()], capture_output=True)
    assert output.returncode == 0


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
    """ This is a test fixture for the docker client, should it be needed in a test """
    client = docker.from_env()
    yield client
    client.close()


def get_image_name(image_type=ImageType.BASE.value):
    """ Fetch image name from an environment variable and inform the user if they are not using it right """
    env_name = 'AIRFLOW_IMAGE'
    try:
        if image_type == ImageType.ONBUILD.value:
            env_name = 'AIRFLOW_ONBUILD_IMAGE'
            image = os.environ[env_name]
        else:
            image = os.environ[env_name]
        return image
    except KeyError:
        raise Exception(f"Please provide docker image name to pytest using environment variable {env_name}")


def get_label(client, label, image_type=ImageType.BASE.value):
    """ Fetch the value of a label from the image """
    image_name = get_image_name(image_type=image_type)
    image = client.images.get(image_name)
    try:
        return image.labels[label]
    except KeyError:
        raise Exception(f"Image should have a label '{label}'")


def get_labels(client, image_type=ImageType.BASE.value):
    """ Fetch all the labels from the image """
    image_name = get_image_name(image_type=image_type)
    image = client.images.get(image_name)
    return image.labels
