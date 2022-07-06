#!/bin/bash
# This script kicks off QA smoke or regression tests

GIT_REPOSITORY="https://github.com/astronomer/${TEST_REPO_NAME}.git"

if [[ -z "${TEST_REPO_NAME}" ]]; then
    echo "The TEST_REPO_NAME environment variable must be defined" >&2
    exit 1
fi

read -r -d '' USAGE <<EOF
kickoff_qa_tests.sh <test_type> <airflow_version>

Arguments:
  airflow_version (required) - the version of Airflow to test
  test_type (required)       - the type of tests to kick off, can be either 'smoke' or 'regression'
EOF

if [[ $# -lt 2 ]]; then
    echo "$USAGE" >&2
    echo
    echo "You must specify both arguments" >&2
    exit 1
fi

AIRFLOW_VERSION=$1

TEST_TYPE=$(echo "$2" | tr '[[:upper:]]' '[[:lower:]]')  # smoke or regression
if [[ "$TEST_TYPE" = "smoke" && "$TEST_TYPE" = "regression" ]]; then
    echo "The specified test type must be either 'smoke' or 'regression'" >&2
    exit 1
fi

# IMAGE_TAG=...



# Update the repo with the latest
if [[ -d "${TEST_REPO_NAME}" ]]; then
    cd "${TEST_REPO_NAME}"
    git fetch
    git reset --hard origin/$(git branch --show-current)
else
    git clone ${GIT_REPOSITORY}
    cd ${TEST_REPO_NAME}
fi

git branch --show-current

CONFIG_FILE=platform_configs_default.yaml

# Update $CONFIG_FILE:
# - platform:
#     ...
#     airflow: ${AIRFLOW_VERSION}
#     ...
sed -i.bak "s/^\([[:space:]]*airflow:[[:space:]]*\)\".*\"/\1\"${AIRFLOW_VERSION}\"/" $CONFIG_FILE

# For runtime, need to update version and image_tag properties in $CONFIG_FILE

# where_to_run setting - 'astro' for runtime and 'software' for AC

# For runtime, it will need to be a build matrix with 'astro' and 'runtime' on one dimension
# and version/s on another

git add $CONFIG_FILE
git commit -m "Run ${TEST_TYPE} tests for Airflow $AIRFLOW_VERSION"

# Try to minimize the amount of time we are vulnerable to a race condition with other jobs

FAILURE_COUNT=0
until [[ $FAILURE_COUNT -ge 5 ]] || git push; do
    git fetch && git merge --no-edit --strategy=ours origin/$(git branch --show-current)
    FAILURE_COUNT=$(( $FAILURE_COUNT + 1 ))
    sleep $FAILURE_COUNT
done
if [[ "$FAILURE_COUNT" -ge 5 ]]; then
    echo "Could not push changes to test repository" >&2
    exit 1
fi
