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
        raise Exception("Error: Docker container did not start running within 10 seconds. It did not show up in the docker ps output")
