#!/bin/sh

# This script is intended to be run from the root of ap-airflow

if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters. Specify version of python and Airflow."
    exit 1
fi

acceptable_airflow_versions=("2.2.0"${IFS}"2.2.1"${IFS}"2.2.2")
acceptable_python_versions=("3.7"${IFS}"3.8")

if [[ ! " ${acceptable_airflow_versions[*]} " =~ "$2" ]]; then
    echo "Illegal Airflow version. Must be a released Airflow from 2.2 onward."
    exit 1
fi

if [[ ! " ${acceptable_python_versions[*]} " =~ "$1" ]]; then
    echo "Illegal python version. Must be 3.7 or 3.8."
    exit 1
fi

echo "Creating image of Airflow $2 based on python $1. This is an unofficial image and may have unforeseen bugs and limited support. Use at your own risk."

baseimg="ap-airflow:$2-python$1"

docker build --tag "$baseimg" \
    --file "$2/bullseye/Dockerfile"  \
    --build-arg PYTHON_MAJOR_MINOR_VERSION=$1 \
    "$2/bullseye"



docker build --tag "ap-airflow:$2-python$1-onbuild" \
    --file common/Dockerfile.onbuild-bullseye  \
    --build-arg baseimage=$baseimg \
    common
