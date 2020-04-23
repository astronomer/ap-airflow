# Astronomer Certified Docker Images

[![docker-pulls](https://img.shields.io/docker/pulls/astronomerinc/ap-airflow.svg)](https://hub.docker.com/r/astronomerinc/ap-airflow)

Astronomer makes it easy to run, monitor, and scale [Apache Airflow](https://github.com/apache/airflow) deployments in our cloud or yours. Source code is made available for the benefit of customers.

If you'd like to see the platform in action, [start a free trial on our SaaS service, Astronomer Cloud](https://astronomer.io/trial) and run through our [getting started guide](https://www.astronomer.io/docs/getting-started/). This is a good first step, even if you're ultimately interested in running Astronomer in your own Kubernetes cluster.

## Docker images

Docker images for deploying and running Astronomer Certified are currently available on
[DockerHub](https://hub.docker.com/u/astronomerinc/).

## Contents of this repo

* The official Dockerfiles that build Astronomer Certified Images
* Example docker-compose files for running various pieces and configurations of
  the platform.

## Contribute

* Source Code: <https://github.com/astronomer/ap-airflow>
* Issue Tracker: <https://github.com/astronomer/ap-airflow/issues>

## Changelog

All changes applied to available point releases will be documented in the `CHANGELOG.md` files within each version folder:
- [1.10.5 Changelog](https://github.com/astronomer/ap-airflow/blob/master/1.10.5/CHANGELOG.md)
- [1.10.7 Changelog](https://github.com/astronomer/ap-airflow/blob/master/1.10.7/CHANGELOG.md)

### Local testing

This testing will run automatically in CI, but it will save some time to try it out locally first.

Airflow is launched into a local Kubernetes cluster using the project "kind" and the most recent version of the Astronomer airflow chart. Python's 'testinfra' module is used to perform system testing on the components while they are running in "kind".

### Ensure prerequisites are met:

- docker
- python3
- virtualenv

Ensure docker installed, and user has permissions
```
docker run -it --rm hello-world
```

Ensure Python3 is installed and in PATH
```
python3 -c "print('Confirmed python3 installed.')"
```

Ensure virtualenv is installed
```
which virtualenv
```

### Set up virtual environment

```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r .circleci/test-requirements.txt
```

### Run system testing

Build the image you want to test
```
docker build -t airflow ./1.10.5/buster
```

Run system testing
```
.circleci/bin/test-airflow airflow
```

The first time you do the build, and the first time you do the system test it will take longer than subsequent runs. The system testing will install the tested versions of CI tools in /tmp/bin (helm, kubectl, kind). It will leave an airflow cluster running on your kind cluster in 'test-cluster'. When you run it again, it will delete the namespace of your most recent deployment and redeploy into a new namespace. If you make changes in the image, don't forget to re-build the image before testing it.

Use the newly installed tools
```
export PATH=/tmp/bin:$PATH
```

Ensure kubectl configured to use kind
```
kubectl cluster-info --context kind-test-cluster
```

Look at the pods
```
kubectl get pods --all-namespaces
```

Clean up
```
kind delete cluster --name test-cluster
```
