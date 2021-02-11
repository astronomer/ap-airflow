# Changelog

Astronomer Certified 2.0.0-3.dev
-----------------------------------------

## Bugfixes

- Bugfix: Return XCom Value in the XCom Endpoint API ([commit](https://github.com/astronomer/airflow/commit/c2c9c06b3))
- BugFix: Dag-level Callback Requests were not run ([commit](https://github.com/astronomer/airflow/commit/4412aba55))
- Increase the default ``min_file_process_interval`` to decrease CPU Usage ([commit](https://github.com/astronomer/airflow/commit/6de02157f))
- Stop creating duplicate Dag File Processors ([commit](https://github.com/astronomer/airflow/commit/4ced807ab))
- Fix drop_user_and_chart migration rule for MySQL ([commit](https://github.com/astronomer/airflow/commit/ebbbc62b542c32b791dd265338d253ed1c1c19f9))
- Bugfix: Import error when using custom backend and `sql_alchemy_conn_secret` ([commit](https://github.com/astronomer/airflow/commit/ebbbc62b542c32b791dd265338d253ed1c1c19f9))
- Fix broken SLA Mechanism ([commit](https://github.com/astronomer/airflow/commit/7036fda8ca5735d85c35a565b436e53259670146))
- Make v1/config endpoint respect webserver `expose_config` setting ([commit](https://github.com/astronomer/airflow/commit/3b45503b5da56a4c9ed9a135102851cfc1969e6b))
- Fix DB Migration for SQLite to upgrade to 2.0 ([commit](https://github.com/astronomer/airflow/commit/7ca3915ba16cead50d1dfdd93d55170cc84ece56))
- Add authentication to lineage endpoint for experimental API ([commit](https://github.com/astronomer/airflow/commit/a181b9034ea797cd250245d45e3af682547a6430))
- Only compare updated time when Serialized DAG exists ([commit](https://github.com/astronomer/airflow/commit/c14f467478118df1fe20e343fece967b7addc11d))
- Fix race condition when using Dynamic DAGs ([commit](https://github.com/astronomer/airflow/commit/7441ce155582e249cced79272300b30aa8f160d1))
- Upgrade azure blob to v12 ([commit](https://github.com/astronomer/airflow/commit/6960757562f149d4ed40dd59f66d7b3ac16ceba4))

Astronomer Certified 2.0.0-2, 2020-12-23
-----------------------------------------

## Bugfixes

- Allow PID file path to be relative when daemonizing a process (scheduler, kerberos, etc) (#13232) ([commit](https://github.com/astronomer/airflow/commit/ebfb6f207))
- Dispose connections when running tasks with `os.fork` & CeleryExecutor ([commit](https://github.com/astronomer/airflow/commit/3a7d34c7a))
- Bump datatables.net from 1.10.21 to 1.10.23 in /airflow/www ([commit](https://github.com/astronomer/airflow/commit/a46642b6d))
- Stop sending Callback Requests if no callbacks are defined on DAG (#13163) ([commit](https://github.com/astronomer/airflow/commit/0c54f684c))
- Filter DagRuns with Task Instances in removed State while Scheduling (#13165) ([commit](https://github.com/astronomer/airflow/commit/426ce80cc))

Astronomer Certified 2.0.0-1, 2020-12-17
-----------------------------------------

User-facing CHANGELOG for AC 2.0.0+astro.1 from Airflow 2.0.0:

## Bugfixes

- Fix race conditions in task callback invocations ([commit](https://github.com/astronomer/airflow/commit/b179f544c))
