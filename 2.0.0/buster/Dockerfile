#
# Copyright 2019 Astronomer Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
ARG APT_DEPS_IMAGE="airflow-apt-deps"
ARG PYTHON_BASE_IMAGE="python:3.7-slim"

FROM ${PYTHON_BASE_IMAGE} as airflow-apt-deps

LABEL maintainer="Astronomer <humans@astronomer.io>"

ARG ASTRONOMER_USER="astro"
ARG ASTRONOMER_UID="50000"

LABEL io.astronomer.docker=true
LABEL io.astronomer.docker.distro="debian"
LABEL io.astronomer.docker.module="airflow"
LABEL io.astronomer.docker.component="airflow"
LABEL io.astronomer.docker.uid="${ASTRONOMER_UID}"


ARG ORG="astronomer"


ENV AIRFLOW_HOME="/usr/local/airflow"
ENV PYTHONPATH=${PYTHONPATH:+${PYTHONPATH}:}${AIRFLOW_HOME}

ENV ASTRONOMER_USER=${ASTRONOMER_USER}
ENV ASTRONOMER_UID=${ASTRONOMER_UID}

# Need to repeat the empty argument here otherwise it will not be set for this stage
# But the default value carries from the one set before FROM
ARG PYTHON_BASE_IMAGE
ENV PYTHON_BASE_IMAGE=${PYTHON_BASE_IMAGE}

# Make sure noninteractie debian install is used and language variables set
ENV DEBIAN_FRONTEND=noninteractive LANGUAGE=C.UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8 \
    LC_CTYPE=C.UTF-8 LC_MESSAGES=C.UTF-8

# By increasing this number we can do force build of all dependencies
ARG DEPENDENCIES_EPOCH_NUMBER="1"
# Increase the value below to force renstalling of all dependencies
ENV DEPENDENCIES_EPOCH_NUMBER=${DEPENDENCIES_EPOCH_NUMBER}

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
           apt-utils \
           curl \
           libmariadb3 \
           freetds-bin \
           gosu \
           libffi6 \
           libkrb5-3 \
           libpq5 \
           libsasl2-2 \
           libsasl2-modules \
           libssl1.1 \
           locales  \
           netcat \
           rsync \
           sasl2-bin \
           sudo \
           tini \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip==19.3.1

RUN useradd --uid $ASTRONOMER_UID --create-home ${ASTRONOMER_USER} \
    && groupadd astrogroup --gid 101 \
    && usermod --append --groups astrogroup ${ASTRONOMER_USER}

# From the airflow image on master

#################################################################
######## Installed dependencies - now installing Airflow ########
#################################################################

FROM ${APT_DEPS_IMAGE} as devel
SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

ENV PIP_NO_CACHE_DIR="true"

RUN apt-get update \
    && curl -sL https://deb.nodesource.com/setup_13.x | sudo bash - \
    && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        libffi-dev \
        libkrb5-dev \
        libpq-dev \
        libsasl2-dev \
        libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG VERSION="2.0.0-3.*"
ARG SUBMODULES="async,azure,amazon,celery,elasticsearch,google,password,cncf.kubernetes,mysql,postgres,redis,slack,ssh,statsd,virtualenv"
ARG AIRFLOW_MODULE="astronomer_certified[${SUBMODULES}]==$VERSION"
ARG AIRFLOW_VERSION="2.0.0"

# Make pip look at our pip repo too, and force it to install these specific
# versions when ever it installs a module.
COPY include/pip.conf /etc/pip.conf
COPY include/pip-constraints.txt /usr/local/share/astronomer-pip-constraints.txt

# Pip install airflow and astro security manager
RUN pip install "${AIRFLOW_MODULE}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.7.txt" \
  && pip install "https://github.com/astronomer/astronomer-airflow-scripts/releases/download/v0.0.5/astronomer_airflow_scripts-0.0.5-py3-none-any.whl" \
	&& pip install "astronomer-fab-security-manager~=1.5"


## move this to same layer as airflow because its from tag.

FROM ${APT_DEPS_IMAGE} as main

# By increasing this number we force CI to upgrade all system packages
ARG PACKAGE_UPGRADE_EPOCH_NUMBER="3"

RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG VERSION="2.0.0-3.*"
ARG AIRFLOW_VERSION="2.0.0"
LABEL io.astronomer.docker.airflow.version="${AIRFLOW_VERSION}"
LABEL io.astronomer.docker.ac.version="${VERSION}"

# Copy all installed python modules. This gets us the compiled without needing dev installed
COPY --from=devel /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=devel /usr/local/bin /usr/local/bin

# Force pip to install these specific versions when ever it installs a module
COPY include/pip.conf /etc/pip.conf
COPY include/pip-constraints.txt /usr/local/share/astronomer-pip-constraints.txt

RUN sed -i \
    # Run pods spun up by Kubernetes Executor as astro user
    -e 's/^run_as_user =.*/run_as_user = 50000/g' \
    # Needed by astronomer-version-check-plugin
    -e 's/^lazy_load_plugins =.*/lazy_load_plugins = False/g' \
    # We sync permissions in the entrypoint so do not need to run in the Webserver again
    -e 's/^update_fab_perms =.*/update_fab_perms = False/g' \
    # Use Auth Backend defined in Astronomer FAB Security Manager
    -e 's/^auth_backend =.*/auth_backend = astronomer.flask_appbuilder.current_user_backend/g' \
    /usr/local/lib/python3.7/site-packages/airflow/config_templates/default_airflow.cfg

# Create logs directory, so we can own it when we mount volumes
RUN install --directory --owner="${ASTRONOMER_USER}" "${AIRFLOW_HOME}" \
    && install --directory --owner="${ASTRONOMER_USER}" "${AIRFLOW_HOME}/logs"

# Copy entrypoint to root
COPY include/entrypoint /

# Copy "cron" scripts
COPY include/clean-airflow-logs /usr/local/bin/clean-airflow-logs

# Set it up so that _apt/UID 100 can `gosu`, but no other users can
RUN groupadd gosuers \
    && usermod --append --groups gosuers _apt \
    && chgrp gosuers /usr/sbin/gosu \
    && chmod u+s,g+sx,o-rx /usr/sbin/gosu

# Create man directory to solve issues installing JRE
RUN mkdir -pv /usr/share/man/man1 && mkdir -pv /usr/share/man/man7

# Though this is set here we currently override this in the helm template, so
# this _might_ not have any effect once deployed. The /entrypoint script copes
# with this
USER ${ASTRONOMER_USER}

# Switch to AIRFLOW_HOME
WORKDIR ${AIRFLOW_HOME}

ENTRYPOINT ["/entrypoint"]
CMD ["airflow", "--help"]
