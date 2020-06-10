#!/usr/bin/env python3
"""
This file is for configuration testing Airflow Onbuild images.

Testinfra is used to configuration test the image. In effect,
testinfra simplifies and provides syntactic sugar for doing
execs into a running container.
"""

import docker
import os
import pytest


def test_labels(docker_client):
    """ Ensure the version of Airflow matches the Docker image label
    """
    assert get_label(docker_client, 'io.astronomer.docker.airflow.onbuild') == "true"
    assert get_label(docker_client, 'maintainer') == "Astronomer <humans@astronomer.io>", \
        "'maintainer' label should be 'Astronomer <humans@astronomer.io>'"


@pytest.fixture(scope='session')
def docker_client(request):
    """ This is a text fixture for the docker client, should it be needed in a test """
    client = docker.from_env()
    yield client
    client.close()


def get_image_name():
    """ Fetch image name from an environment variable and inform the user if they are not using it right """
    try:
        return os.environ['AIRFLOW_IMAGE']
    except KeyError:
        raise Exception("Please provide docker image name to pytest using environment variable AIRFLOW_IMAGE")


def get_label(client, label):
    """ Fetch the value of a label from the image """
    image_name = get_image_name()
    image = client.images.get(image_name)
    try:
        return image.labels[label]
    except KeyError:
        raise Exception(f"Image should have a label '{label}'")
