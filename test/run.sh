#!/usr/bin/env bash
set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

### Helper function, defines a pattern
#     entrypoint to behave tests should be "test/docker.sh"
run-dags() {
    DAG_FOLDER=$1
    shift 1

    pushd $DIR/$DAG_FOLDER
    ./test/docker.sh $@
    popd
}

source $DIR/config.sh

### QA Scenario Dags
run-dags qa-scenario-dags behave features/001_example_dag.feature


