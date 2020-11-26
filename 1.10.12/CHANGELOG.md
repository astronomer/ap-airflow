# Changelog

Astronomer Certified 1.10.12-2, 2020-12-01
-----------------------------------------------

### Bug Fixes

- SkipMixin: Handle empty branches ([commit](https://github.com/astronomer/airflow/commit/64a37512e))
- Sync FAB Permissions for all base views ([commit](https://github.com/astronomer/airflow/commit/26ad9eba6))
- Fixes issue with affinity backcompat in Airflow 1.10 ([commit](https://github.com/astronomer/airflow/commit/d7ac1b911))
- Fix empty asctime field in JSON formatted logs ([commit](https://github.com/astronomer/airflow/commit/376e8c445))
- Show Generic Error for Charts & Query View in old UI ([commit](https://github.com/astronomer/airflow/commit/e87277dcd))
- Webserver: Further Sanitize values passed to origin param ([commit](https://github.com/astronomer/airflow/commit/4c27334a5))
- Mask Password in Log table when using the CLI ([commit](https://github.com/astronomer/airflow/commit/a09201069))
- Limit version of marshmallow-sqlalchemy ([commit](https://github.com/astronomer/airflow/commit/f88ae68e5))
- Bump attrs to > 20.0 ([commit](https://github.com/astronomer/airflow/commit/7fcf2e5eb))
- Bump attrs and cattrs dependencies ([commit](https://github.com/astronomer/airflow/commit/aede56833))
- Install cattr on Python 3.7 ([commit](https://github.com/astronomer/airflow/commit/1173785c3))
- Pin `kubernetes` to a max version of 11.0.0 ([commit](https://github.com/astronomer/airflow/commit/2d070bdab))
- Allow overrides for pod_template_file ([commit](https://github.com/astronomer/airflow/commit/76b17f23b))

### Improvements

- [AIRFLOW-3607] Only query DB once per DAG run for TriggerRuleDep ([commit](https://github.com/astronomer/airflow/commit/e1659b2d1))
- [AIRFLOW-3607] Optimize dep checking when depends on past set and concurrency limit ([commit](https://github.com/astronomer/airflow/commit/8673e0147))

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
