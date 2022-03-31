# Astronomer Core Docker Images

[![docker-pulls](https://img.shields.io/docker/pulls/astronomerinc/ap-airflow.svg)](https://hub.docker.com/r/astronomerinc/ap-airflow)

Astronomer makes it easy to run, monitor, and scale [Apache Airflow](https://github.com/apache/airflow) deployments in our cloud or yours. Source code is made available for the benefit of customers.

#### Terminology

| Terms         | Example                  | Description                                                                                         |
| :------------ | :----------------------- | :-------------------------------------------------------------------------------------------------- |
| `edge` build  | `main-dev`               | Built from the current `main` branch of [astronomer/airflow](https://github.com/astronomer/airflow) |
| dev build     | `2.2.4-4-dev`            | Development build, released during ap-airflow changes, including pre-releases and version releases  |
| nightly build | `2.2.4-nightly-20220314` | Nightly builds, regularly triggered by a CircleCI pipeline sometime during the midnight hour UTC    |
| release build | `2.2.4-4`                | Release builds, triggered by a release PR                                                           |

Note: Edge builds are always development builds

#### Build matrix

| Build         | Nightly                   | Pre-release PR     | Release PR         |
| :------------ | :------------------------ | :----------------- | :----------------- |
| `edge` build  | :white_check_mark:        | :white_check_mark: | :white_check_mark: |
| nightly build | :white_check_mark:        | :white_check_mark: |                    |
| dev build     | (only during pre-release) | :white_check_mark: | :white_check_mark: |
| release build |                           |                    | :white_check_mark: |

## Docker images

Docker images for deploying and running Astronomer Core are currently available on
[Quay](https://quay.io/repository/astronomer/ap-airflow?tab=tags).

We publish 2 variants for each AC Version (example: `1.10.15-3`):

**For AC<2.2.0**:
1. `quay.io/astronomer/ap-airflow:1.10.15-3-buster`
2. `quay.io/astronomer/ap-airflow:1.10.15-3-buster-onbuild`

**For AC>=2.2.0**:

We dropped the distribution name from the image tag so the 2 variants are as follows:

1. `quay.io/astronomer/ap-airflow:2.2.1-1`
2. `quay.io/astronomer/ap-airflow:2.2.1-1-onbuild`

The only difference between them is that the `-onbuild` images uses Docker `ONBUILD` commands to
copy `packages.txt`, `requirements.txt` and the entire project directory (including `dags`,
`plugins` folders etc) in the docker file.

For each of our `-onbuild` images we publish two flavors of tag:

**For AC<2.2.0**:
1. `quay.io/astronomer/ap-airflow:1.10.15-buster-onbuild` which is our latest release of the `1.10.15` series,
including latest security patches. This tag is "floating" or movable.
2. `quay.io/astronomer/ap-airflow:1.10.15-3-buster-onbuild` once this tag is pushed it will never change again.

**For AC>=2.2.0**:

1. `quay.io/astronomer/ap-airflow:2.2.0-onbuild` which is our latest release of the `2.2.0` series,
including latest security patches. This tag is "floating" or movable.
2. `quay.io/astronomer/ap-airflow:2.2.0-3-onbuild` once this tag is pushed it will never change again.

## Version Life Cycle & Maintenance policy

The support and maintenance of the  Docker images are described in
the [Version Life Cycle](https://docs.astronomer.io/software/ac-support-policy/).

## Contents of this repo

* The official Dockerfiles that build Astronomer Core Images
* Example docker-compose files for running various pieces and configurations of
  the platform.

## Contribute

* Source Code: <https://github.com/astronomer/ap-airflow>
* Issue Tracker: <https://github.com/astronomer/ap-airflow/issues>

## Step-by-step instructions for common activities

### Release a new Astronomer Certified major, minor, or bugfix version (eg: X.Y.Z)

<details>
<summary>Click to expand Step-By-Step instructions</summary>

1. Remove the `-dev` part of the relevant version in `IMAGE_MAP` in `.circleci/common.py`.

   Example:
   The latest dev version is `2.2.1-1-dev`, and we want to release `2.2.1-1`.
   ```diff
   diff --git a/.circleci/common.py b/.circleci/common.py
   index xxxxxxx..yyyyyyy 100644
   --- a/.circleci/common.py
   +++ b/.circleci/common.py
   @@ -35,7 +35,7 @@ IMAGE_MAP = collections.OrderedDict([
        ("2.1.3-2", ["buster"]),
        ("2.1.4-2", ["buster"]),
        ("2.2.0-3-dev", ["bullseye", "buster"]),
   -    ("2.2.1-1-dev", ["bullseye", "buster"]),
   +    ("2.2.1-1", ["bullseye", "buster"]),
   ])

   # Airflow Versions for which we don't publish Python Wheels
   ```
2. Run the `update-dockerfiles` pre-commit hook (this should fail but it should change the
   relevant Dockerfile).

   Example:
   ```bash
   pre-commit run update-dockerfiles
   ```
3. Add the changed Dockerfile and commit (this should succeed).

   Example: The `update-dockerfiles` hook updated `2.2.1/bullseye/Dockerfile`:
   ```bash
   git add 2.2.1/bullseye/Dockerfile; git commit
   ```

</details>

### Release an existing Astronomer Certified version with an updated version of Airflow

<details>
<summary>Click to expand Step-By-Step instructions</summary>

1. Update the postfix version of the relevant version in `IMAGE_MAP` in `.circleci/common.py`.

   Example:
   The latest AC version is `2.2.0-1` and we want to release `2.2.0-2`.
   ```diff
   diff --git a/.circleci/common.py b/.circleci/common.py
   index xxxxxxx..yyyyyyy 100644
   --- a/.circleci/common.py
   +++ b/.circleci/common.py
   @@ -35,7 +35,7 @@ IMAGE_MAP = collections.OrderedDict([
        ("2.1.3-2", ["buster"]),
        ("2.1.4-2", ["buster"]),
        ("2.2.0-3-dev", ["bullseye", "buster"]),
   -    ("2.2.1-1", ["bullseye", "buster"]),
   +    ("2.2.1-2", ["bullseye", "buster"]),
    ])

    # Airflow Versions for which we don't publish Python Wheels
   ```
2. Run the `update-dockerfiles` pre-commit hook (this should fail but it should change the
   relevant Dockerfile).

   Example:
   ```bash
   pre-commit run update-dockerfiles
   ```
3. Add the changed Dockerfile and commit (this should succeed).

   Example:
   The `update-dockerfiles` hook updated `2.2.0/bullseye/Dockerfile`:
   ```bash
   git add 2.2.0/bullseye/Dockerfile; git commit
   ```

</details>

### Add new Astronomer Certified development version

<details>
<summary>Click to expand Step-By-Step instructions</summary>

1. Add the Astronomer Certified version to `IMAGE_MAP` in `.circleci/common.py`.

   Example:
   The latest previous release was `2.2.1-1` and we're adding `2.3.0-1-dev`.
   ```diff
   diff --git a/.circleci/common.py b/.circleci/common.py
   index xxxxxxx..yyyyyyy 100644
   --- a/.circleci/common.py
   +++ b/.circleci/common.py
   @@ -36,6 +36,7 @@ IMAGE_MAP = collections.OrderedDict([
        ("2.1.4-2", ["buster"]),
        ("2.2.0-3-dev", ["bullseye", "buster"]),
        ("2.2.1-1", ["bullseye", "buster"]),
   +    ("2.3.0-1-dev", ["bullseye"]),
    ])

    # Airflow Versions for which we don't publish Python Wheels
   ```
4. Edit the new `CHANGELOG.md` to show what has changed in this release.

   Example:
   ```bash
   nano 2.3.0/CHANGELOG.md
   ```
5. Add the new directory to the Git staging area.

   Example:
   ```bash
   git add 2.3.0
   ```
6. Run the `update-dockerfiles` pre-commit hook (this should fail but it should change the
   relevant Dockerfile).

   Example:
   ```bash
   pre-commit run update-dockerfiles
   ```

   The pre-commit hook should change some lines in the new `Dockerfile`.
   ```diff
   diff --git a/2.3.0/bullseye/Dockerfile b/2.3.0/bullseye/Dockerfile
   index xxxxxxx..yyyyyyy 100644
   --- a/2.3.0/bullseye/Dockerfile
   +++ b/2.3.0/bullseye/Dockerfile
   @@ -110,10 +110,10 @@ RUN apt-get update \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

   -ARG VERSION="2.2.1-1"
   +ARG VERSION="2.3.0-1.*"
    ARG SUBMODULES="async,azure,amazon,elasticsearch,google,password,cncf.kubernetes,mysql,postgres,redis,slack,ssh,statsd,virtualenv"
    ARG AIRFLOW_MODULE="astronomer_certified[${SUBMODULES}]==$VERSION"
   -ARG AIRFLOW_VERSION="2.2.1"
   +ARG AIRFLOW_VERSION="2.3.0"

    # Make pip look at our pip repo too, and force it to install these specific
    # versions when ever it installs a module.
   @@ -145,8 +145,8 @@ RUN apt-get update \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

   -ARG VERSION="2.2.1-1"
   -ARG AIRFLOW_VERSION="2.2.1"
   +ARG VERSION="2.3.0-1.*"
   +ARG AIRFLOW_VERSION="2.3.0"
    LABEL io.astronomer.docker.airflow.version="${AIRFLOW_VERSION}"
    LABEL io.astronomer.docker.ac.version="${VERSION}"

   ```
7. Stage the changes to the Dockerfile and commit (this should succeed).

   Example:
   ```bash
   git add 2.3.0/bullseye/Dockerfile && git commit
   ```

</details>

### Add a new base build image (eg: new Debian stable release)

<details>
<summary>Click to expand Step-By-Step instructions</summary>

1. Add or adjust the Debian release name in `IMAGE_MAP`.

   Example:
   Previous Astronomer Certified versions only built with Debian Buster, but Debian Bullseye has
   just been released as the new Debian stable version and we'd like to add support for that.
   ```diff
   diff --git a/.circleci/common.py b/.circleci/common.py
   index xxxxxxx..yyyyyyy 100644
   --- a/.circleci/common.py
   +++ b/.circleci/common.py
   @@ -36,7 +36,7 @@ IMAGE_MAP = collections.OrderedDict([
        ("2.1.4-2", ["buster"]),
        ("2.2.0-3-dev", ["bullseye", "buster"]),
        ("2.2.1-1", ["bullseye", "buster"]),
   -    ("2.3.0-1-dev", ["buster"]),
   +    ("2.3.0-1-dev", ["bullseye", "buster"]),
    ])

    # Airflow Versions for which we don't publish Python Wheels
   ```
2. Add a new version directory for it.

   Example:
   There is currently a `2.3.0/buster` directory that we need to copy to `2.3.0/bullseye` and
   then modify that `Dockerfile` to use Debian Bullseye.
   ```bash
   cp -a 2.3.0/buster 2.3.0/bullseye
   ```
3. Adjust the relevant Dockerfile.

   Example:
   Update the `2.3.0/bullseye/Dockerfile` to use the upstream Debian Bullseye image.
   ```diff
   diff --git a/2.3.0/bullseye/Dockerfile b/2.3.0/bullseye/Dockerfile
   index xxxxxxx..yyyyyyy 100644
   --- a/2.3.0/bullseye/Dockerfile
   +++ b/2.3.0/bullseye/Dockerfile
   @@ -14,7 +14,7 @@
    # limitations under the License.
    ARG APT_DEPS_IMAGE="airflow-apt-deps"
    ARG PYTHON_MAJOR_MINOR_VERSION="3.9"
   -ARG PYTHON_BASE_IMAGE="python:${PYTHON_MAJOR_MINOR_VERSION}-slim-buster"
   +ARG PYTHON_BASE_IMAGE="python:${PYTHON_MAJOR_MINOR_VERSION}-slim-bullseye"

    FROM ${PYTHON_BASE_IMAGE} as airflow-apt-deps

   ```
4. Stage the changes to the Dockerfile and commit (the pre-commit hooks should all succeed).

   Example:
   ```bash
   git add .circleci/common.py 2.3.0/bullseye && git commit
   ```

</details>

<!-- CHANGELOG START -->
## Changelog

All changes applied to available point releases will be documented in the `CHANGELOG.md` files within each version folder:
- [1.10.15 Changelog](https://github.com/astronomer/ap-airflow/blob/master/1.10.15/CHANGELOG.md)
- [2.1.4 Changelog](https://github.com/astronomer/ap-airflow/blob/master/2.1.4/CHANGELOG.md)
- [2.2.4 Changelog](https://github.com/astronomer/ap-airflow/blob/master/2.2.4/CHANGELOG.md)
- [2.2.5 Changelog](https://github.com/astronomer/ap-airflow/blob/master/2.2.5/CHANGELOG.md)
<!-- CHANGELOG END -->

## Testing

### Local testing

This testing will run automatically in CI, but it will save some time to try it out locally first.

Airflow is launched into a local Kubernetes cluster using the project "kind" and the most recent
version of the Astronomer airflow chart. Python's 'testinfra' module is used to perform system
testing on the components while they are running in "kind".

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

The first time you do the build, and the first time you do the system test it will take longer
than subsequent runs. The system testing will install the tested versions of CI tools in /tmp/bin
(helm, kubectl, kind). It will leave an airflow cluster running on your kind cluster in
'test-cluster'. When you run it again, it will delete the namespace of your most recent deployment
and redeploy into a new namespace. If you make changes in the image, don't forget to re-build the
image before testing it.

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

## Scheduled Tasks

The regularly scheduled tasks are:

#### Edge Builds

* Rebase the `astro-main` branch of [`astronomer/airflow`](https://github.com/astronomer/airflow)
  onto `main` and push it to `astronomer/airflow:astro-main` (this then kicks off a GitHub Actions
  workflow that builds Airflow and Astronomer Certified Python packages/wheels) and pushes them to
  our PyPI package repository
* Build nightly Docker images for QA (using those nightly Airflow and Astronomer Certified wheels)
  and push them to the dev image repository

### CircleCI Schedules

The [CircleCI documentation](https://github.com/CircleCI-Public/api-preview-docs/blob/master/docs/scheduled-pipelines.md)
on scheduled pipelines is very new and in slight disarray.

See also:
* The [announcement](https://discuss.circleci.com/t/scheduled-pipelines-are-here/41684/2) for
  scheduled pipelines
* This [relevant (for now) PR](https://github.com/CircleCI-Public/api-preview-docs/pull/104),
  which includes an example of branch filtering
* Documentation on [parameter syntax](https://circleci.com/docs/2.0/reusing-config/#parameter-syntax)
* Documentation on [logic statements](https://circleci.com/docs/2.0/configuration-reference/#logic-statements)

The API for manipulating schedules is documented [here](https://circleci.com/docs/api/v2/#tag/Schedule),
including examples.

Here is an example listing all schedules with HTTPie (and colorizing the response with `jq`):

```bash
$ http https://circleci.com/api/v2/project/gh/astronomer/ap-airflow/schedule \
       circle-token:<CIRCLECI_PERSONAL_ACCESS_TOKEN> \
       | jq
```

To create a new schedule (refer to the [HTTPie docs about raw JSON](https://httpie.io/docs#json)):

```bash
$ http --verbose \
       https://circleci.com/api/v2/project/gh/astronomer/ap-airflow/schedule \
       circle-token:<CIRCLECI_PERSONAL_ACCESS_TOKEN> \
       name="every-morning-0200-UTC" \
       description="Every morning at 02:00 UTC" \
       attribution-actor="system" \
       parameters:='{ "branch": "master" }' \
       timetable:='{ "per-hour": 1, "hours-of-day": [2], "days-of-week": ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]}'
```

Note that updating and deleting schedules uses a different URL path:

```bash
$ http PATCH \
       https://circleci.com/api/v2/schedule/<schedule_uuid> \
       circle-token:<CRCLECI_PERSONAL_ACCESS_TOKEN> \
       name=every-sunday-0100-utc \
       description="Every Sunday at 01:00 UTC"
````

You can create a CircleCI personal API token [in your CircleCI user settings](https://app.circleci.com/settings/user/tokens).
Do note that a PAT will authenticate as you, and have full, read and write access on CircleCI, so
keep your PAT secret and do not publish it anywhere!

## License

Apache 2.0 with Commons Clause
