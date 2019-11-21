#!/usr/bin/env python3

import os
import sys
import json
import pytest
import subprocess
import testinfra
import docker

from time import sleep, time
from packaging.version import parse as semantic_version

def get_image_name():
    try:
        return os.environ['AIRFLOW_IMAGE']
    except KeyError:
        raise Exception("Please provide docker image name to pytest using environment variable AIRFLOW_IMAGE")

def get_label(client, label):
    image_name = get_image_name()
    image = client.images.get(image_name)
    try:
        return image.labels[label]
    except KeyError:
        raise Exception(f"Image should have a label '{label}'")

def start_postgres():
    docker_client = docker.from_env()
    try:
        postgres = docker_client.containers.get('postgres')
    except docker.errors.NotFound:
        return subprocess.check_output(
            ['docker', 'run',
             '--name', 'postgres',
             '-e', 'POSTGRES_PASSWORD=notsecretpassword',
             '-d', 'postgres:9.6.15']
        ).decode().strip()
    return postgres.short_id

def get_ip_from_id(_id):
    return subprocess.check_output(
        ['docker', 'inspect',
         '-f', '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}',
         _id]
    ).decode().strip()

@pytest.fixture(scope='session')
def webserver(request):

    docker_id_db = start_postgres()
    db_connection_string = f"postgres://postgres:notsecretpassword@{get_ip_from_id(docker_id_db)}:5432"
    docker_id = subprocess.check_output(
        ['docker', 'run',
         '--name', 'webserver',
         '-e', f"AIRFLOW__CORE__SQL_ALCHEMY_CONN={db_connection_string}",
         '-d', get_image_name(), 'airflow', 'webserver']).decode().strip()

    yield testinfra.get_host("docker://" + docker_id)

    subprocess.check_call(['docker', 'rm', '-f', docker_id, docker_id_db])

@pytest.fixture(scope='session')
def docker_client(request):
    client = docker.from_env()
    yield client
    client.close()

def test_airflow_in_path(webserver):
    assert webserver.exists('airflow'), \
        "Expected 'airflow' to be in PATH"

def test_maintainer(webserver, docker_client):
    maintainer  = get_label(docker_client, 'maintainer')
    assert maintainer  == "Astronomer <humans@astronomer.io>", \
        "'maintainer' label should be 'Astronomer <humans@astronomer.io>'"

def test_version(webserver, docker_client):
    airflow_version = get_label(docker_client, 'io.astronomer.docker.airflow.version')
    version_output = webserver.check_output('airflow version')
    assert airflow_version in version_output

def test_elasticsearch_version(webserver):
    try:
        elasticsearch_module = webserver.pip_package.get_packages()['elasticsearch']
    except KeyError:
        raise Exception("elasticsearch pip module is not installed")
    version = elasticsearch_module['version']
    assert semantic_version(version) >= semantic_version('5.5.3'), \
        "elasticsearch module must be version 5.5.3 or greater"
