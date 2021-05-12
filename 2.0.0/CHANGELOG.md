# Changelog

Astronomer Certified 2.0.0-6, 2021-05-12
-----------------------------------------

## Bugfixes

- Mask passwords and sensitive info in task logs and UI (#15599) ([commit](https://github.com/astronomer/airflow/commit/2f88ffc41))
- Bump stylelint to remove vulnerable sub-dependency (#15784) ([commit](https://github.com/astronomer/airflow/commit/c21820064))
- Add resolution to force dependencies to use patched version of `lodash` (#15777) ([commit](https://github.com/astronomer/airflow/commit/3c48c0084))
- Remove unused dependency (#15762) ([commit](https://github.com/astronomer/airflow/commit/15be415e5))

Astronomer Certified 2.0.0-5, 2021-04-26
-----------------------------------------

User-facing CHANGELOG for AC 2.0.0+astro.5 from AC 2.0.0+astro.4:

## Bugfixes

- Bugfix: `TypeError` when Serializing & sorting iterables (#15395) ([commit](https://github.com/astronomer/airflow/commit/14f18b3fd))
- Add Traceback in LogRecord in `JSONFormatter` (#15414) ([commit](https://github.com/astronomer/airflow/commit/7787ede4d))
- Fix Task adoption in Kubernetes Executor ([commit](https://github.com/astronomer/airflow/commit/b7b73ac12))
- Further fix trimmed `pod_id` for `KubernetesPodOperator` (#15445) ([commit](https://github.com/astronomer/airflow/commit/4fef61621))
- Bugfix: Invalid name when trimmed `pod_id` ends with hyphen in `KubernetesPodOperator` (#15443) ([commit](https://github.com/astronomer/airflow/commit/07a191f90))
- Fix to ensure 100vh min plays nicely w/ Linux+Chrome (#13857) ([commit](https://github.com/astronomer/airflow/commit/540eda273))
- Fix `used_group_ids` in partial_subset (#13700) (#15308) ([commit](https://github.com/astronomer/airflow/commit/c68ea977f))
- Fix password masking in CLI `action_logging` (#15143) ([commit](https://github.com/astronomer/airflow/commit/477de9407))
- Change default of `[kubernetes] enable_tcp_keepalive` to `True` (#15338) ([commit](https://github.com/astronomer/airflow/commit/4c3803aaf))
- Adds missing LDAP "extra" dependencies to ldap provider. (apache#13308) ([commit](https://github.com/astronomer/airflow/commit/674bd98))
- Add missing Azure Storage libraries ([commit](https://github.com/astronomer/airflow/commit/206c6a6))

Astronomer Certified 2.0.0-4, 2021-04-13
-----------------------------------------

## Bugfixes

- Change the default celery worker_concurrency to 16 ([commit](https://github.com/astronomer/airflow/commit/924ba1c4f))
- Fix backfill crash on task retry or reschedule ([commit](https://github.com/astronomer/airflow/commit/a0407d2d9))
- Disables provider's manager warning for source-installed prod image. ([commit](https://github.com/astronomer/airflow/commit/66078273f))
- Setting `max_tis_per_query` to 0 now correctly removes the limit ([commit](https://github.com/astronomer/airflow/commit/1f96b4c0c))
- Add __repr__ for Executors ([commit](https://github.com/astronomer/airflow/commit/779030136))
- Fix SQL syntax to check duplicate connections ([commit](https://github.com/astronomer/airflow/commit/db0296264))
- Fix `TaskNotFound` in log endpoint ([commit](https://github.com/astronomer/airflow/commit/fedf636dc))
- Fix dag run type enum query for mysqldb driver ([commit](https://github.com/astronomer/airflow/commit/88221df57))
- Bugfix: Don't try to create a duplicate Dag Run in Scheduler ([commit](https://github.com/astronomer/airflow/commit/f492f79e8))
- Bugfix: Scheduler fails if task is removed at runtime ([commit](https://github.com/astronomer/airflow/commit/cfb562184))
- Bugfix: Manual DagRun trigger should not skip scheduled runs ([commit](https://github.com/astronomer/airflow/commit/6eca58d94))
- Unable to trigger backfill or manual jobs with Kubernetes executor. ([commit](https://github.com/astronomer/airflow/commit/217aa1c1b))
- Bugfix: Fix overriding `pod_template_file` in KubernetesExecutor ([commit](https://github.com/astronomer/airflow/commit/6076fb5f7))
- Pass queue to `BaseExecutor.execute_async` like in airflow 1.10 ([commit](https://github.com/astronomer/airflow/commit/e8d858569))
- Scheduler: Remove TIs from starved pools from the critical path. ([commit](https://github.com/astronomer/airflow/commit/aa995b59a))
- Remove extra/needless deprecation warnings from airflow.contrib module ([commit](https://github.com/astronomer/airflow/commit/1d87b16f2))
- Fix support for long dag_id and task_id in KubernetesExecutor ([commit](https://github.com/astronomer/airflow/commit/4641f8e73))
- Bugfix: resources in `executor_config` breaks Graph View in UI ([commit](https://github.com/astronomer/airflow/commit/a74efa2fd))
- Fix invalid value error caused by long k8s pod name ([commit](https://github.com/astronomer/airflow/commit/b0276e5b2))
- Fix `KubernetesExecutor` issue with deleted pending pods ([commit](https://github.com/astronomer/airflow/commit/44d305944))
- Avoid scheduler/parser manager deadlock by using non-blocking IO ([commit](https://github.com/astronomer/airflow/commit/9746f5171))
- Add different modes to sort dag files for parsing ([commit](https://github.com/astronomer/airflow/commit/66dc00c92))
- Remove duplicate call to sync_metadata inside DagFileProcessorManager ([commit](https://github.com/astronomer/airflow/commit/19a21d218))
- Bump Redoc to resolve vulnerability in sub-dependency ([commit](https://github.com/astronomer/airflow/commit/b00b845bb))
- Bump dompurify from 2.0.12 to 2.2.6 in /airflow/www ([commit](https://github.com/astronomer/airflow/commit/66830abd7))
- Scheduler should not fail when invalid executor_config is passed ([commit](https://github.com/astronomer/airflow/commit/bf5e385f3))
- BugFix: Fix taskInstance API call fails if a task is removed from running DAG ([commit](https://github.com/astronomer/airflow/commit/5f416f4a1))
- Fix crash when user clicks on  "Task Instance Details" caused by start_date being None ([commit](https://github.com/astronomer/airflow/commit/432fff9e4))
- Gracefully handle missing start_date and end_date for DagRun ([commit](https://github.com/astronomer/airflow/commit/587123326))
- Fix logging error with task error when JSON logging is enabled ([commit](https://github.com/astronomer/airflow/commit/8f2e99d52))
- BugFix: TypeError in `monitor_pod` ([commit](https://github.com/astronomer/airflow/commit/b0e334bfb))
- Bugfix: Plugins endpoint was unauthenticated ([commit](https://github.com/astronomer/airflow/commit/a87a20d5d))
- Pin SQLAlchemy to <1.4 due to breakage of sqlalchemy-utils ([commit](https://github.com/astronomer/airflow/commit/ce2849ed0))
- Disable row level locking for Mariadb and MySQL <8 ([commit](https://github.com/astronomer/airflow/commit/a1af062bc))
- Compare string values, not if strings are the same object ([commit](https://github.com/astronomer/airflow/commit/c6e10c1b1))
- Sort lists, sets and tuples in Serialized DAGs ([commit](https://github.com/astronomer/airflow/commit/e8f872849))
- Simplify cleaning string passed to origin param (#14738) ([commit](https://github.com/astronomer/airflow/commit/3c61a3b81))
- BugFix: Serialize `max_retry_delay` as a timedelta ([commit](https://github.com/astronomer/airflow/commit/c1136e05c))
- Fix `sync-perm` to work correctly when update_fab_perms = False ([commit](https://github.com/astronomer/airflow/commit/471c95cee))
- Webserver: Sanitize string passed to origin param ([commit](https://github.com/astronomer/airflow/commit/a5b18475a))
- AC Docker: Fix CVEs for `curl`: CVE-2020-8169, CVE-2020-8177, CVE-2020-8231, CVE-2020-8285, CVE-2020-8286, CVE-2020-8169, CVE-2020-8177, CVE-2020-8285, CVE-2020-8286

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
