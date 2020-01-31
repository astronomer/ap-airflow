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

FROM astronomerinc/ap-airflow:1.10.5-rhel7
LABEL maintainer="Astronomer <humans@astronomer.io>"

LABEL io.astronomer.docker=true
LABEL io.astronomer.docker.airflow.onbuild=true

# Install RHEL packages
ONBUILD COPY packages.txt .
ONBUILD RUN if [[ -s packages.txt ]]; then \
    yum update -y && cat packages.txt | xargs yum install -y; \
  fi

# Install python packages
ONBUILD COPY requirements.txt .
ONBUILD RUN if [[ -s requirements.txt ]]; then \
    pip install --no-cache-dir -q -r requirements.txt; \
  fi

# Copy entire project directory
ONBUILD COPY . .
