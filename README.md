# Astronomer Core Docker Images

[![docker-pulls](https://img.shields.io/docker/pulls/astronomerinc/ap-airflow.svg)](https://hub.docker.com/r/astronomerinc/ap-airflow)

Astronomer makes it easy to run, monitor, and scale [Apache Airflow](https://github.com/apache/airflow) deployments in our cloud or yours. Source code is made available for the benefit of customers.

## Docker images

Docker images for deploying and running Astronomer Core are currently available on
[Quay](https://quay.io/repository/astronomer/ap-airflow?tab=tags).

We publish 2 variants for each AC Version (example: `1.10.10-3`):

1. `quay.io/astronomer/ap-airflow:1.10.10-3-buster`
2. `quay.io/astronomer/ap-airflow:1.10.10-3-buster-onbuild`

The only difference between them is that the `-onbuild` images uses Docker `ONBUILD` commands to
copy `packages.txt`, `requirements.txt` and the entire project directory (including `dags`,
`plugins` folders etc) in the docker file.

For each of our `-onbuild` images we publish two flavors of tag:

1. `quay.io/astronomer/ap-airflow:1.10.10-buster-onbuild` which is our latest release of the `1.10.10` series,
including latest security patches. This tag is "floating" or movable.
2. `quay.io/astronomer/ap-airflow:1.10.10-3-buster-onbuild` once this tag is pushed it will never change again.

## Contents of this repo

* The official Dockerfiles that build Astronomer Core Images
* Example docker-compose files for running various pieces and configurations of
  the platform.

## Contribute

* Source Code: <https://github.com/astronomer/ap-airflow>
* Issue Tracker: <https://github.com/astronomer/ap-airflow/issues>

## Changelog

All changes applied to available point releases will be documented in the `CHANGELOG.md` files within each version folder:
- [1.10.5 Changelog](https://github.com/astronomer/ap-airflow/blob/master/1.10.5/CHANGELOG.md)
- [1.10.7 Changelog](https://github.com/astronomer/ap-airflow/blob/master/1.10.7/CHANGELOG.md)
- [1.10.10 Changelog](https://github.com/astronomer/ap-airflow/blob/master/1.10.10/CHANGELOG.md)
- [1.10.12 Changelog](https://github.com/astronomer/ap-airflow/blob/master/1.10.12/CHANGELOG.md)
- [1.10.14 Changelog](https://github.com/astronomer/ap-airflow/blob/master/1.10.14/CHANGELOG.md)
- [2.0.0 Changelog](https://github.com/astronomer/ap-airflow/blob/master/2.0.0/CHANGELOG.md)
- [2.0.1 Changelog](https://github.com/astronomer/ap-airflow/blob/master/2.0.1/CHANGELOG.md)

## Testing

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

## License

Apache 2.0 with Commons Clause
