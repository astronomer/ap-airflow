#!/usr/bin/env bash
set -euo pipefail

dags=(
    qa-scenario-dags
)

GIT_BASE="git@github.com:astronomer/"

for d in ${dags[@]}; do
    git clone $GIT_BASE/$d $DIR/$d
done
