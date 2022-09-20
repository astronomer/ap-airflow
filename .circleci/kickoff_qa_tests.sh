#!/bin/bash
# This script kicks off QA smoke or regression tests

TEST_REPO_NAME=qa-airflow-run-on-software
GIT_REPOSITORY="https://github.com/astronomer/${TEST_REPO_NAME}.git"

if [[ $# -lt 3 ]]; then
    echo >&2 "kickoff_qa_tests.sh <airflow_version> <image_tag> <test_type>"
    echo >&2 ""
    echo >&2 "Arguments:"
    echo >&2 "  airflow_version (required) - the version of Airflow to test"
    echo >&2 "  image_tag (required)       - the Airflow container image to pull"
    echo >&2 "  test_type (required)       - the type of tests to kick off, can be either 'smoke' or 'regression'"
    echo >&2 ""
    echo >&2 "You must specify both arguments"
    exit 1
fi

AIRFLOW_VERSION=$1

IMAGE_TAG=$2

TEST_TYPE=$(echo "$3" | tr '[:upper:]' '[:lower:]')  # smoke or regression
if [[ "$TEST_TYPE" != "smoke" && "$TEST_TYPE" != "regression" ]]; then
    echo "The specified test type must be either 'smoke' or 'regression'" >&2
    exit 1
fi

# IMAGE_TAG=...



set -ex -o pipefail

# Update the repo with the latest
if [[ -d "${TEST_REPO_NAME}" ]]; then
    cd "${TEST_REPO_NAME}"
    git pull || ( git rebase --abort; git reset --hard "origin/$(git branch --show-current)" )
else
    git clone "${GIT_REPOSITORY}"
    cd "${TEST_REPO_NAME}"
fi

git branch --show-current

CONFIG_FILE=platforms_config.yaml

# Update $CONFIG_FILE:
# - platform:
#     ...
#     airflow:
#       - "${AIRFLOW_VERSION}"
#     ...
#     tests:
#       - "smoke"
#     ...
# Replace each .platform.airflow value with a list of airflow versions and
# replace each .platform.tests value with the test type
# https://stackoverflow.com/a/72627603
# https://stackoverflow.com/a/72795815
# We double quote the array values to ensure YAML interprets them as strings
# and not floats (for the version strings)
AIRFLOW_VERSION=$AIRFLOW_VERSION \
TEST_TYPE=$TEST_TYPE \
IMAGE_TAG=$IMAGE_TAG \
yq eval --inplace \
    '(.[].platform.airflow) |= [strenv(AIRFLOW_VERSION)] | ..style="double"
    |(.[].platform.tests) |= [strenv(TEST_TYPE)] | ..style="double"
    |(.[].platform.image_tag = strenv(IMAGE_TAG) | ..style="double")' \
    ${CONFIG_FILE}

# For runtime, need to update version and image_tag properties in $CONFIG_FILE

# where_to_run setting - 'astro' for runtime and 'software' for AC

# For runtime, it will need to be a build matrix with 'astro' and 'runtime' on one dimension
# and version/s on another

git add $CONFIG_FILE
git config user.name "ap-airflow"
git config user.email "astronomer@users.noreply.github.com"
git commit --allow-empty --message="Run ${TEST_TYPE} tests for Airflow $AIRFLOW_VERSION

CircleCI build: ${CIRCLE_BUILD_URL}
Git commit: https://github.com/${CIRCLE_PROJECT_USERNAME}/${CIRCLE_PROJECT_REPONAME}/commit/${CIRCLE_SHA1}"

if [[ -n "$DRY_RUN" ]]; then
    exit 0
fi

# Try to minimize the amount of time we are vulnerable to a race condition with other jobs
FAILURE_COUNT=0
until [[ $FAILURE_COUNT -ge 5 ]] || git push; do
    git fetch && git merge --no-edit --strategy=ours "origin/$(git branch --show-current)"
    FAILURE_COUNT=$(( FAILURE_COUNT + 1 ))
    sleep $FAILURE_COUNT
done
if [[ "$FAILURE_COUNT" -ge 5 ]]; then
    echo "Could not push changes to test repository" >&2
    exit 1
fi
