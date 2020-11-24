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

FROM alpine:3.10
LABEL maintainer="Astronomer <humans@astronomer.io>"

ARG ORG="astronomer"
ARG VERSION="1.10.12-2.*"
ARG SUBMODULES="all, statsd, elasticsearch"
ARG AIRFLOW_MODULE="astronomer_certified[${SUBMODULES}]==$VERSION"
ARG REPO_BRANCH=master
ENV AIRFLOW_VERSION="1.10.12"

LABEL io.astronomer.docker=true
LABEL io.astronomer.docker.distro="alpine"
LABEL io.astronomer.docker.module="airflow"
LABEL io.astronomer.docker.component="airflow"
LABEL io.astronomer.docker.airflow.version="${AIRFLOW_VERSION}"
LABEL io.astronomer.docker.ac.version="${VERSION}"

ENV AIRFLOW_HOME="/usr/local/airflow"
ENV PYTHONPATH=${PYTHONPATH:+${PYTHONPATH}:}${AIRFLOW_HOME}

ARG ASTRONOMER_USER="astro"
ARG ASTRONOMER_GROUP="astro"
ENV ASTRONOMER_USER=${ASTRONOMER_USER}
ENV ASTRONOMER_GROUP=${ASTRONOMER_GROUP}

RUN addgroup -S ${ASTRONOMER_GROUP} \
	&& adduser -S -G ${ASTRONOMER_GROUP} ${ASTRONOMER_USER}

COPY include/humans@astronomer.io.rsa.pub /etc/apk/keys

# Make pip look at our pip repo too, and force it to install these specific
# versions when ever it installs a module.
COPY include/pip.conf /etc/pip.conf
COPY include/pip-constraints.txt /usr/local/share/astronomer-pip-constraints.txt

# Install packages
RUN echo https://github.com/astronomer/ap-airflow/raw/${REPO_BRANCH}/alpine-packages/3.10/repo >> /etc/apk/repositories \
  && apk update \
	&& apk add --no-cache --virtual .build-deps \
		build-base \
		cyrus-sasl-dev \
		freetds-dev \
		freetype-dev \
		krb5-dev \
		libffi-dev \
		libxml2-dev \
		libxslt-dev \
		linux-headers \
		python3-dev \
		musl-dev \
		postgresql-dev \
		tzdata \
	&& apk add --no-cache \
		bash \
		ca-certificates \
		cyrus-sasl \
		cython3 \
		freetds \
		krb5-libs \
		py3-bcrypt \
		py3-cassandra-driver'>='3 \
		py3-cryptography \
		py3-fastavro \
		py3-grpcio \
		py3-mysqlclient \
		py3-numpy-dev \
		py3-numpy \
		py3-pandas \
		py3-pip \
		py3-psycopg2 \
		py3-pycryptodome \
		py3-pynacl \
		py3-typed-ast \
		python3 \
		tini \
	&& apk add --upgrade \
		openssl \
	&& update-ca-certificates \
	&& cp /usr/share/zoneinfo/UTC /etc/localtime \
	&& pip3 install --no-cache-dir --upgrade snowflake-connector-python==1.9.1 \
	&& pip3 install "${AIRFLOW_MODULE}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.7.txt" \
	&& pip3 install --no-cache-dir "https://github.com/astronomer/astronomer-airflow-scripts/releases/download/v0.0.5/astronomer_airflow_scripts-0.0.5-py3-none-any.whl" \
	&& pip3 install --no-cache-dir "astronomer-fab-security-manager~=1.2, >=1.2.2" \
	&& apk del .build-deps py3-numpy-dev \
	&& ln -sf /usr/bin/python3 /usr/bin/python \
	&& ln -sf /usr/bin/pip3 /usr/bin/pip \
	&& sed -i -e '\#https://github.com/astronomer/#d' /etc/apk/repositories

RUN sed -i \
    # Run pods spun up by Kubernetes Executor as astro user
    -e 's/^run_as_user =.*/run_as_user = 100/g' \
    # We sync permissions in the entrypoint so do not need to run in the Webserver again
    -e 's/^update_fab_perms =.*/update_fab_perms = False/g' \
    /usr/lib/python3.7/site-packages/airflow/config_templates/default_airflow.cfg

# Create logs directory so we can own it when we mount volumes
RUN mkdir -p ${AIRFLOW_HOME}/logs

# Copy entrypoint to root
COPY include/entrypoint /

# Copy "cron" scripts
COPY include/clean-airflow-logs /usr/local/bin/clean-airflow-logs

# Ensure our user has ownership to AIRFLOW_HOME
RUN chown -R ${ASTRONOMER_USER}:${ASTRONOMER_GROUP} ${AIRFLOW_HOME}

# Switch to AIRFLOW_HOME
WORKDIR ${AIRFLOW_HOME}

# Expose all airflow ports
EXPOSE 8080 5555 8793

# Run airflow with minimal init
ENTRYPOINT ["tini", "--", "/entrypoint"]
