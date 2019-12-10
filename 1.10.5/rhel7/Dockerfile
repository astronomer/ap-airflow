FROM registry.access.redhat.com/ubi7/ubi
MAINTAINER Arun Kumar

LABEL io.astronomer.docker=true
LABEL io.astronomer.docker.distro="alpine"
LABEL io.astronomer.docker.module="airflow"
LABEL io.astronomer.docker.component="airflow"
LABEL io.astronomer.docker.airflow.version="1.10.5"

ARG ORG="astronomer"
ARG VERSION="1.10.5-2"
ARG SUBMODULES="all, statsd, elasticsearch"
ARG REPO_BRANCH=master


ENV AIRFLOW_REPOSITORY="https://github.com/${ORG}/airflow"
ENV AIRFLOW_MODULE="git+${AIRFLOW_REPOSITORY}@${VERSION}#egg=apache-airflow[${SUBMODULES}]"
ENV AIRFLOW_HOME="/usr/local/airflow"
ENV PYMSSQL_BUILD_WITH_BUNDLED_FREETDS=1
ENV PYTHONPATH=${PYTHONPATH:+${PYTHONPATH}:}${AIRFLOW_HOME}
ENV AIRFLOW_GPL_UNIDECODE="True"

ARG ASTRONOMER_USER="astro"
ARG ASTRONOMER_GROUP="astro"
ENV ASTRONOMER_USER=${ASTRONOMER_USER}
ENV ASTRONOMER_GROUP=${ASTRONOMER_GROUP}

RUN useradd  ${ASTRONOMER_USER}
RUN usermod -g ${ASTRONOMER_GROUP} ${ASTRONOMER_USER}

ENV PIP_CONSTRAINT=/usr/local/share/astronomer-pip-constraints.txt
COPY include/pip-constraints.txt /usr/local/share/astronomer-pip-constraints.txt

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 && \
    yum -y install https://rhel7.iuscommunity.org/ius-release.rpm && \
    rpm -ivh http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm


RUN yum install -y epel-release cyrus-sasl-devel krb5-libs python-devel mysql-devel make tini build-base git krb5-dev openssl-devel libffi-dev linux-headers nodejs nodejs-npm python3-dev tzdata  wget libaio  zlib-devel libcurl-devel python-setuptools python-virtualenv bzip2-devel openssl-devel ncurses-devel  libxml2-devel libxslt-devel  sqlite sqlite-devel gcc sharutils unzip bash tar gcc-c++ && \
    yum groupinstall -y "Development Tools"

RUN wget https://nodejs.org/dist/v12.13.1/node-v12.13.1-linux-x64.tar.xz && \
    tar -xvf /node-v12.13.1-linux-x64.tar.xz

COPY include/install-python /install-python
RUN chmod 750 ./install-python && \
    ./install-python
#    cp /usr/share/zoneinfo/UTC /etc/localtime && \

RUN pip3.6 install --no-cache-dir cryptography  \
     &&  pip3.6 install --no-cache-dir  pymssql==2.1.4 \
     &&  pip3.6 install --no-cache-dir --upgrade pip==19.3.1 \
     &&  pip3.6 install --no-cache-dir --upgrade setuptools==41.0.1 \
     &&  pip3.6 install --no-cache-dir --upgrade snowflake-connector-python==1.9.1 \
     &&  pip3.6 install --no-cache-dir "${AIRFLOW_MODULE}" \
     &&  pip3.6 install --no-cache-dir "https://github.com/astronomer/astronomer-fab-securitymanager/releases/download/v1.2.1/astronomer_fab_security_manager-1.2.1-py3-none-any.whl" \
     &&  pip3.6 install --no-cache-dir "https://github.com/astronomer/astronomer-airflow-scripts/releases/download/v0.0.4/astronomer_airflow_scripts-0.0.4-py3-none-any.whl" \
     &&  cd /usr/local/lib/python3.6/site-packages/airflow/www_rbac \
     &&  /node-v12.13.1-linux-x64/bin/npm install \
     &&  /node-v12.13.1-linux-x64/bin/npm run build

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
ENTRYPOINT ["/tini", "--", "/entrypoint"]
