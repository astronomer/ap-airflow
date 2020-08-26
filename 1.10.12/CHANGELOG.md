# Changelog

Astronomer Certified 1.10.12-1.dev, 2020-09-18
-----------------------------------------------

CHANGELOG for AC `1.10.12+astro.1` from Airflow `1.10.12`:

### Bug Fixes

- Add role-based authentication backend ([commit](https://github.com/apache/airflow/commit/49d4840))
- KubernetesPodOperator template fix (#10963) ([commit](https://github.com/apache/airflow/commit/259f1b797))
- Fix operator field update for SerializedBaseOperator ([commit](https://github.com/apache/airflow/commit/cfc9732d7))
- Fix pod_mutation_hook ([commit](https://github.com/apache/airflow/commit/73b5fe1aa))
- Fix formatting of Host information ([commit](https://github.com/apache/airflow/commit/4d820744c))

### Improvements

- Adding body as templated field for CloudSqlImportOperator ([commit](https://github.com/apache/airflow/commit/18e3a3b))
- Stop showing Import Errors for Plugins in Webserver ([commit](https://github.com/apache/airflow/commit/ac17612))
- Restrict 'nteract-scrapbook' to <0.4 ([commit](https://github.com/apache/airflow/commit/b4312ef))
- Enable DAG Serialization by default ([commit](https://github.com/apache/airflow/commit/8da0ad8))
- Remove deprecation warning from contrib/kubernetes/pod.py ([commit](https://github.com/apache/airflow/commit/5721d39))
- Make grace_period_seconds option on KubernetesPodOperator ([commit](https://github.com/apache/airflow/commit/236b9b3b2))
- Add on_kill support for the KubernetesPodOperator ([commit](https://github.com/apache/airflow/commit/ce94497cc))

### New Features
- Add Secrets backend for Microsoft Azure Key Vault ([commit](https://github.com/apache/airflow/commit/908515f13))
