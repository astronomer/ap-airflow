# Changelog

Astronomer Certified 1.10.13-2.dev
-----------------------------------------------

### Bug Fixes

- BugFix: Tasks with depends_on_past or task_concurrency are stuck ([commit](https://github.com/astronomer/airflow/commit/56e446811))
- Fix issue with empty Resources in executor_config ([commit](https://github.com/astronomer/airflow/commit/7ef6354da))
- Typo Fix: Deprecated config force_log_out_after was not used ([commit](https://github.com/astronomer/airflow/commit/45410abdc))

Astronomer Certified 1.10.13-1, 2020-11-25
-----------------------------------------------

User-facing CHANGELOG for AC `1.10.13+astro.1` from Airflow `1.10.13`:

### Bug Fixes

- Add role-based authentication backend ([commit](https://github.com/astronomer/airflow/commit/d64ad84))
- Fix operator field update for SerializedBaseOperator ([commit](https://github.com/astronomer/airflow/commit/cfc9732d7))
- Fix empty asctime field in JSON formatted logs ([commit](https://github.com/astronomer/airflow/commit/a4b4d84))

### Improvements

- Stop showing Import Errors for Plugins in Webserver ([commit](https://github.com/astronomer/airflow/commit/cd3a34e))
- Enable DAG Serialization by default ([commit](https://github.com/astronomer/airflow/commit/2954e4c))

### New Features

- Show "Warning" to Users with Duplicate Connections ([commit](https://github.com/astronomer/airflow/commit/386487e))
