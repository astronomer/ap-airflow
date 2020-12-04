# Changelog

Astronomer Certified 1.10.12-2, 2020-12-04
-----------------------------------------------

### Bug Fixes

- SkipMixin: Handle empty branches ([commit](https://github.com/astronomer/airflow/commit/64a37512e))
- Sync FAB Permissions for all base views ([commit](https://github.com/astronomer/airflow/commit/3db82c98f))
- Fixes issue with affinity backcompat in Airflow 1.10 ([commit](https://github.com/astronomer/airflow/commit/aa13576d0))
- Fix empty asctime field in JSON formatted logs ([commit](https://github.com/astronomer/airflow/commit/21a9bd07c))
- Show Generic Error for Charts & Query View in old UI ([commit](https://github.com/astronomer/airflow/commit/d737558eb))
- Webserver: Further Sanitize values passed to origin param ([commit](https://github.com/astronomer/airflow/commit/728dbddf5))
- Mask Password in Log table when using the CLI ([commit](https://github.com/astronomer/airflow/commit/f746e3c75))
- Limit version of marshmallow-sqlalchemy ([commit](https://github.com/astronomer/airflow/commit/97a39dd19))
- Bump attrs to > 20.0 ([commit](https://github.com/astronomer/airflow/commit/2379b6a23))
- Bump attrs and cattrs dependencies ([commit](https://github.com/astronomer/airflow/commit/dad229d71))
- Install cattr on Python 3.7 ([commit](https://github.com/astronomer/airflow/commit/dacc4ab8c))
- Pin `kubernetes` to a max version of 11.0.0 ([commit](https://github.com/astronomer/airflow/commit/d9a90c26c))
- Pin pyzmq<20.0 for Alpine images ([commit](https://github.com/astronomer/ap-airflow/commit/3059797))
- Dockerfile: Add `sync_perm` command to buster images ([commit](https://github.com/astronomer/ap-airflow/commit/5a28d3f))
- BugFix: Tasks with depends_on_past or task_concurrency are stuck ([commit](https://github.com/astronomer/airflow/commit/381a55009))
- Fix issue with empty Resources in executor_config ([commit](https://github.com/astronomer/airflow/commit/d5b89e88e))
- [AIRFLOW-2809] Fix security issue regarding Flask SECRET_KEY ([commit](https://github.com/astronomer/airflow/commit/91f64a3d1))
- [AIRFLOW-2884] Fix Flask SECRET_KEY security issue in www_rbac ([commit](https://github.com/astronomer/airflow/commit/f0b4547d5))
- [AIRFLOW-2886] Generate random Flask SECRET_KEY in default config ([commit](https://github.com/astronomer/airflow/commit/2efe39197))
- Don't let webserver run with dangerous config ([commit](https://github.com/astronomer/airflow/commit/075d4ddb0))

### Improvements

- [AIRFLOW-3607] Only query DB once per DAG run for TriggerRuleDep ([commit](https://github.com/astronomer/airflow/commit/7693514bb))
- [AIRFLOW-3607] Optimize dep checking when depends on past set and concurrency limit ([commit](https://github.com/astronomer/airflow/commit/63bb7f3ae))
- Dockerfile: Stop running `sync_perm` multiple times for Airflow >= 1.10.7 ([commit](https://github.com/astronomer/ap-airflow/commit/9c10dcf))
- Dockerfile: Bump astronomer_airflow_scripts to 0.0.5 ([commit](https://github.com/astronomer/ap-airflow/commit/42b4169))
- Dockerfile: Use Airflow Constraints file for AC 1.10.12 and 1.10.13 ([commit](https://github.com/astronomer/ap-airflow/commit/e968f12))

Astronomer Certified 1.10.12-1, 2020-09-29
-----------------------------------------------

CHANGELOG for AC `1.10.12+astro.1` from Airflow `1.10.12`:

### Bug Fixes

- Add role-based authentication backend ([commit](https://github.com/astronomer/airflow/commit/49d4840))
- KubernetesPodOperator template fix (#10963) ([commit](https://github.com/astronomer/airflow/commit/259f1b797))
- Fix operator field update for SerializedBaseOperator ([commit](https://github.com/astronomer/airflow/commit/cfc9732d7))
- Fix pod_mutation_hook ([commit](https://github.com/astronomer/airflow/commit/73b5fe1aa))
- Fix formatting of Host information ([commit](https://github.com/astronomer/airflow/commit/4d820744c))

### Improvements

- Adding body as templated field for CloudSqlImportOperator ([commit](https://github.com/astronomer/airflow/commit/18e3a3b))
- Stop showing Import Errors for Plugins in Webserver ([commit](https://github.com/astronomer/airflow/commit/ac17612))
- Restrict 'nteract-scrapbook' to <0.4 ([commit](https://github.com/astronomer/airflow/commit/b4312ef))
- Enable DAG Serialization by default ([commit](https://github.com/astronomer/airflow/commit/8da0ad8))
- Remove deprecation warning from contrib/kubernetes/pod.py ([commit](https://github.com/astronomer/airflow/commit/5721d39))
- Make grace_period_seconds option on KubernetesPodOperator ([commit](https://github.com/astronomer/airflow/commit/236b9b3b2))
- Add on_kill support for the KubernetesPodOperator ([commit](https://github.com/astronomer/airflow/commit/ce94497cc))

### New Features

- Add Secrets backend for Microsoft Azure Key Vault ([commit](https://github.com/astronomer/airflow/commit/908515f13))
