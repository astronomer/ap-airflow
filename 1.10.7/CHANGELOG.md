# Changelog

Astronomer Certified 1.10.7-18, 2021-04-27
--------------------------------------------

### Bug Fixes

- Fix `sync-perm` to work correctly when `update_fab_perms = False` (#14847) ([commit](https://github.com/astronomer/airflow/commit/8e49e8f22))
- Webserver: Sanitize string passed to origin param (#14738) ([commit](https://github.com/astronomer/airflow/commit/c0c4ff8b3))
- Correctly parse (and copy) extras with python version to metadist ([commit](https://github.com/astronomer/airflow/commit/38de13b67))

Astronomer Certified 1.10.7-17, 2021-01-05
-------------------------------------------

### Bug Fixes

- Continually check if we should shut down istio contaner when running K8sPodOperator ([commit](https://github.com/astronomer/airflow/commit/b295c8b4c4acb8f63772413e7959e43b6566309c))
- Pin `kubernetes` to a max version of 11.0.0 ([commit](https://github.com/astronomer/airflow/commit/80c9fba46a29bf93c109dc519a5362ef132f6d68))
- Bump ini from 1.3.5 to 1.3.8 in /airflow/www_rbac ([commit](https://github.com/astronomer/airflow/commit/140fea8f6c47adcefa002b7ccb880e4ba1abc9d3))
- Bump datatables.net from 1.10.21 to 1.10.22 in /airflow/www_rbac ([commit](https://github.com/astronomer/airflow/commit/335c1ccd8bd5307bf9f995ff09ece48e5115e801))
- Respect LogFormat when using ES logging with Json Format ([commit](https://github.com/astronomer/airflow/commit/29c8b4e41db817046fff24c8e409fd0c623d925d))

Astronomer Certified 1.10.7-16, 2020-12-10
-------------------------------------------

### Bug Fixes

- Sync FAB Permissions for all base views ([commit](https://github.com/astronomer/airflow/commit/c0ce191dbd20cc562ba2dabb2f56d0a09c083856))
- Show Generic Error for Charts & Query View in old UI ([commit](https://github.com/astronomer/airflow/commit/b904b9b0d4fd11167c4e37bab95623a56b794063))
- Webserver: Further Sanitize values passed to origin param ([commit](https://github.com/astronomer/airflow/commit/4626acfca7052c150059b06698a0070577a695bf))
- Mask Password in Log table when using the CLI ([commit](https://github.com/astronomer/airflow/commit/669d53a3c90e0f22e911625e99863ccc09c7fe83))
- [AIRFLOW-2809] Fix security issue regarding Flask SECRET_KEY ([commit](https://github.com/astronomer/airflow/commit/e570b31ea4f3033610d2afe8c417de85335bdf23))
- [AIRFLOW-2884] Fix Flask SECRET_KEY security issue in www_rbac ([commit](https://github.com/astronomer/airflow/commit/5ba2518c2e1218a465954532a3ccb1c5eb473b6c))
- [AIRFLOW-2886] Generate random Flask SECRET_KEY in default config ([commit](https://github.com/astronomer/airflow/commit/be2e6a85c71ce659e4894b49ea3c0bfc4be3f261))
- Don't let webserver run with dangerous config ([commit](https://github.com/astronomer/airflow/commit/8873829d979a43d0f7724d5cfeecf42969378ce6))
- Pin marshmallow-sqlalchemy for >= 3.6 ([commit](https://github.com/astronomer/airflow/commit/f45ff1b1345d03b732fd96a0cbfd3f9f82926ba2))
- Pin marshmallow <= 2.21 ([commit](https://github.com/astronomer/airflow/commit/17e52868200522015ae20987b76b7ff1a60c8840))

### Improvements

- Dockerfile: Stop running `sync_perm` multiple times for Airflow >= 1.10.7 ([commit](https://github.com/astronomer/ap-airflow/commit/9c10dcf))
- Dockerfile: Bump astronomer_airflow_scripts to 0.0.5 ([commit](https://github.com/astronomer/ap-airflow/commit/42b4169))

Astronomer Certified 1.10.7-15, 2020-09-22
-------------------------------------------

### Bug Fixes

- Use Serialized DAGs to sync permissions when DAG Serialization is enabled ([commit](https://github.com/astronomer/airflow/commit/185c13d033a8fa95a8323fba36a52d2e23e34265))
- Webserver: Sanitize values passed to origin param ([commit](https://github.com/astronomer/airflow/commit/b24f1f43b970210e86e261f2cb8c19f500840439))


Astronomer Certified 1.10.7-14, 2020-08-04
--------------------------------------------

### Bug Fixes

- Fix broken `/landing_times` View ([commit](https://github.com/astronomer/airflow/commit/5e27133))
- Run Kubernetes Worker Pods as astro user ([commit](https://github.com/astronomer/ap-airflow/commit/f6819a4))
- **Dockerfile**: Exactly match `apache-airflow` in `requirements.txt` to restrict installation of 'apache-airflow' ([commit](https://github.com/astronomer/ap-airflow/commit/c2536db))
- **Astro Version Check Plugin**: Only show warnings on old versions ([commit](https://github.com/astronomer/astronomer-airflow-version-check/commit/24ad49e))
- **Astro Version Check Plugin**: Make the plugin MySQL compatible ([commit](https://github.com/astronomer/astronomer-airflow-version-check/commit/0210f60))

Astronomer Certified 1.10.7-13, 2020-06-18
--------------------------------------------

### Bug Fixes

- Block people from upgrading Airflow in the image ([commit](https://github.com/astronomer/ap-airflow/commit/bf517ea5bb3))

### Improvements

- Add man directories to buster images to fix jre install problems ([commit](https://github.com/astronomer/ap-airflow/commit/551995e))
- Don't use the `|safe` filter in code, it's risky ([commit](https://github.com/astronomer/airflow/commit/e84c4eb))
- Further validation that only task commands are run by executors ([commit](https://github.com/astronomer/airflow/commit/9405e0b))
- Validate only task commands are run by executors ([commit](https://github.com/astronomer/airflow/commit/22c5f2b))
- Fix Celery default to no longer allow pickle ([commit](https://github.com/astronomer/airflow/commit/d819da6))
- Remove duplicate error message on chart connection failure ([commit](https://github.com/astronomer/airflow/commit/476c44c))
- Add note about using dag_run.conf in BashOperator ([commit](https://github.com/astronomer/airflow/commit/4d86731))

Astronomer Certified 1.10.7-12, 2020-06-03
--------------------------------------------

### Bug Fixes

- Fix pip install issue caused by Python3.7.7 packages on Alpine-based images ([commit](https://github.com/astronomer/ap-airflow/commit/404dce6))

Astronomer Certified 1.10.7-11, 2020-05-28
--------------------------------------------

### Bug Fixes

- Make loading plugins from entrypoint fault-tolerant (#628) ([commit](https://github.com/astronomer/airflow/commit/ae9d5b7))
- Pin Azure storage to <0.37.0 (#8833) ([commit](https://github.com/astronomer/airflow/commit/cd12692))
- Pin Version of Azure Cosmos to <4 ([commit](https://github.com/astronomer/airflow/commit/ff74293))
- Stop showing Import Errors for Plugins in Webserver ([commit](https://github.com/astronomer/airflow/commit/69dba65))

### New Features
- Add support for AWS Secrets Manager as Secrets Backend (#8186)([commit](https://github.com/astronomer/airflow/commit/0dc4736))

Astronomer Certified 1.10.7-10, 2020-04-29
--------------------------------------------

### Bug Fixes

- Constraint version of Flask-Appbuilder to non-broken version ([commit](https://github.com/astronomer/ap-airflow/commit/33da5f5))

### New Features

- Allow setting Airflow Variable values to empty string ('') ([commit](https://github.com/astronomer/airflow/commit/d6d666c33))
- Get Airflow Variables from AWS Systems Manager Parameter Store ([commit](https://github.com/astronomer/airflow/commit/6a7130f55))
- Get Airflow Variables from GCP Secrets Manager ([commit](https://github.com/astronomer/airflow/commit/595ede548))
- Get Airflow Variables from Hashicorp Vault ([commit](https://github.com/astronomer/airflow/commit/59435bb88))
- Get Airflow Variables from Environment Variables ([commit](https://github.com/astronomer/airflow/commit/fe1a6a3bd))
- Make BaseSecretsBackend.build_path generic ([commit](https://github.com/astronomer/airflow/commit/1623b80bc))
- Fix CloudSecretsManagerBackend invalid connections_prefix ([commit](https://github.com/astronomer/airflow/commit/fe0a9d850))
- Standardize SecretBackend class names ([commit](https://github.com/astronomer/airflow/commit/008cb6ebe))
- [AIRFLOW-7105] Unify Secrets Backend method interfaces ([commit](https://github.com/astronomer/airflow/commit/5ddff01e8))
- [AIRFLOW-7104] Add Secret backend for GCP Secrets Manager ([commit](https://github.com/astronomer/airflow/commit/19bcf781b))
- [AIRFLOW-5705] Make AwsSsmSecretsBackend consistent with VaultBackend ([commit](https://github.com/astronomer/airflow/commit/cff559cbb))
- [AIRFLOW-7076] Add support for HashiCorp Vault as Secrets Backend ([commit](https://github.com/astronomer/airflow/commit/99bb2a7ef))
- [AIRFLOW-5705] Fix bugs in AWS SSM Secrets Backend ([commit](https://github.com/astronomer/airflow/commit/afae4b62b))
- [AIRFLOW-5705] Fix bug in Secrets Backend ([commit](https://github.com/astronomer/airflow/commit/29015f537))
- [AIRFLOW-5705] Add secrets backend and support for AWS SSM ([commit](https://github.com/astronomer/airflow/commit/2a82f5365))

### Improvements

- [AIRFLOW-5167] Update dependencies for GCP packages ([commit](https://github.com/astronomer/airflow/commit/6277fcd499))

Astronomer Certified 1.10.7-9, 2020-04-28
--------------------------------------------

### New Features

- Require the AC version check plugin ([commit](https://github.com/astronomer/airflow/commit/3af238f))

Dockerfile changes are:

- Upgrade sqlite3 packages for Alpine 3.10 to mitigate [CVE-2020-1967](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2020-1967) ([commit](https://github.com/astronomer/ap-airflow/commit/2f29d493259cddd487bcc306b829a4ec4a74f35e))
- Upgrade OpenSSL to mitigate [CVE-2019-16168](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-16168) ([commit](https://github.com/astronomer/ap-airflow/commit/6de11c2c87e78b7a3171d8fb222c7278fcb673c9))
- Constraint version of WTForms to non-broken version ([commit](https://github.com/astronomer/ap-airflow/commit/3cd34236f8a7214434dc313af525160133520bcb))
- JPype1 0.7.3 no longer installs on Alpline/musl-libc ([commit](https://github.com/astronomer/ap-airflow/commit/44164ba40cd1878cabeec5edc32fe0a7bb7a8e0d))
- Constraint version of Flask-Appbuilder to non-broken version ([commit](https://github.com/astronomer/ap-airflow/commit/33da5f5))

Astronomer Certified 1.10.7-8, 2020-04-11
-----------------------------------------------

### Bug Fixes

- Fix issue with SQLAlchemy 1.3.16 ([commit](https://github.com/astronomer/airflow/commit/3b6cf61e0f2de3fe3be98c8ff5809060d6e42ba4))
- [AIRFLOW-7113] Fix gantt render error ([commit](https://github.com/astronomer/airflow/commit/dc015a0f3a836fe519f97acc75a26873a226695a))
- Add prestop hook to prevent logging issue ([commit](https://github.com/astronomer/airflow/commit/328705f5f74e49be0ab251705172be45c19635f3))
- [AIRFLOW-6584] Pin cassandra driver ([commit](https://github.com/astronomer/airflow/commit/21fd6fb56ee23c0a287874ed094e42fb22385916))

Astronomer Certified 1.10.7-7, 2020-03-13
-----------------------------------------------

### Bug Fixes

- [AIRFLOW-6576] Fix scheduler crash caused by deleted task with sla misses (apache#7187)
- [AIRFLOW-6381] Remove styling based on DAG id from DAGs page (apache#6985)

### Improvements

- [AIRFLOW-6666] Resolve js-yaml advisory (apache#7283)
- [AIRFLOW-6632] Bump dagre-d3 to resolve lodash CVE advisory (apache#7280)
- [AIRFLOW-6667] Resolve serialize-javascript advisory (apache#7282)
- [AIRFLOW-6519] Make TI logs constants in Webserver configurable (apache#7113)
- [AIRFLOW-4445] Mushroom cloud errors too verbose (apache#6952)
- [AIRFLOW-6514] use RUNNING_DEPS to check run from UI (apache#6367)
- [AIRFLOW-6608] Change logging level for Bash & PyOperator Env exports
- [AIRFLOW-6627] Email with incorrect DAG not delivered (apache#7250)
- [AIRFLOW-6677] Remove deprecation warning from SQLAlchmey (apache#7289)
- [AIRFLOW-6495] Load DAG only once when running a task using StandardTaskRunner (apache#7090)
- [AIRFLOW-6683] REST API respects store_serialized_dag setting (apache#7296)
