# Changelog

Astronomer Certified 2.0.0-3, 2021-02-16
-----------------------------------------

## Bugfixes

- Bugfix: Return XCom Value in the XCom Endpoint API ([commit](https://github.com/astronomer/airflow/commit/c2c9c06b3))
- BugFix: Dag-level Callback Requests were not run ([commit](https://github.com/astronomer/airflow/commit/4412aba55))
- Increase the default ``min_file_process_interval`` to decrease CPU Usage ([commit](https://github.com/astronomer/airflow/commit/6de02157f))
- Stop creating duplicate Dag File Processors ([commit](https://github.com/astronomer/airflow/commit/4ced807ab))
- Fix drop_user_and_chart migration rule for MySQL ([commit](https://github.com/astronomer/airflow/commit/ebbbc62b542c32b791dd265338d253ed1c1c19f9))
- Bugfix: Import error when using custom backend and `sql_alchemy_conn_secret` ([commit](https://github.com/astronomer/airflow/commit/6e661baa7ed642a511ae5b1857ccbbddb4c04001))
- Fix broken SLA Mechanism ([commit](https://github.com/astronomer/airflow/commit/5746aa68a0d0097b45afe6cb8529f16fa2349a36))
- Make v1/config endpoint respect webserver `expose_config` setting ([commit](https://github.com/astronomer/airflow/commit/554c1075b96f4ed61385dc93ab4b6d9bc913886c))
- Fix DB Migration for SQLite to upgrade to 2.0 ([commit](https://github.com/astronomer/airflow/commit/73b045c35ca299a950e7c021973961e04e9729b2))
- Add authentication to lineage endpoint for experimental API ([commit](https://github.com/astronomer/airflow/commit/5c5b994bae38038a03686eaa57a96a40ddb33ee9))
- Only compare updated time when Serialized DAG exists ([commit](https://github.com/astronomer/airflow/commit/fa83ffe088fc1646e899f6fbce367e27c464f5a4))
- Fix race condition when using Dynamic DAGs ([commit](https://github.com/astronomer/airflow/commit/1387ff23318d26506c6f1fa72f669acc7ee3f415))
- Upgrade azure blob to v12 ([commit](https://github.com/astronomer/airflow/commit/c716b78f0667a2c53b5fd6a2e781b277719698dc))

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
