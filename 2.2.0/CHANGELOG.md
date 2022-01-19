# Changelog

Astronomer Certified 2.2.0-5, 2022-01-19
----------------------------------------

### Security

- Updated `celery` to `5.2.3` to fix [CVE-2021-23727](https://nvd.nist.gov/vuln/detail/CVE-2021-23727) ([commit](https://github.com/astronomer/ap-airflow/commit/b7ce051b726978691f6f37cb1f2f00a3c88da56f))
- Updated `Flask-AppBuilder` to `3.4.3` to fix [CVE-2021-41265](https://nvd.nist.gov/vuln/detail/CVE-2021-41265) ([commit](https://github.com/astronomer/ap-airflow/commit/b7ce051b726978691f6f37cb1f2f00a3c88da56f))
- Updated `numpy` to `1.21.5` to fix [CVE-2021-33430](https://nvd.nist.gov/vuln/detail/CVE-2021-33430) ([commit](https://github.com/astronomer/ap-airflow/commit/953ec71d9228f0c6558d4cd9aa74b8ddb5dfd141))

### Bugfixes

- Fix labels used to find queued KubeExecutor pods (#19904) ([commit](https://github.com/astronomer/airflow/commit/ce9f4ce3b4209d1df28306c978b27729ece634f2))
- Update [Astronomer FAB Security Manager](https://github.com/astronomer/astronomer-fab-securitymanager) to version [1.8.1](https://github.com/astronomer/astronomer-fab-securitymanager/releases/tag/v1.8.1)

Astronomer Certified 2.2.0-4, 2021-11-05
----------------------------------------

### Bugfixes

- Only mark SchedulerJobs as failed, not any jobs (#19375) ([commit](https://github.com/astronomer/airflow/commit/39ef7280940a39aa9a98ecf48422d0f876f12747))

Astronomer Certified 2.2.0-3, 2021-11-02
----------------------------------------

### Bugfixes

- Bugfix: Check next run exists before reading data interval (#19307) ([commit](https://github.com/astronomer/airflow/commit/c6dea7c7bb911c6863fee1a3a6fe21c9f5106eb2))
- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/3b6b0da59983bbdd68686f7dd172ee951b0d66e5))
- Try to move "dangling" rows in upgradedb (#18953) ([commit](https://github.com/astronomer/airflow/commit/e0584063d2cd4a8a93e7d83df620f4c6b6dc1adc))
- Revert "Handle DagRuns with no execution_date or dag_id." ([commit](https://github.com/astronomer/airflow/commit/2b0bc063f03b2378d7db52aa8717ab0bbe06e89c))
- Revert "Try to move "dangling" rows in upgradedb" ([commit](https://github.com/astronomer/airflow/commit/be7a722131cd0d25a434019f1acd5815acde5b2e))
- Fix Unexpected commit error in schedulerjob (#19213) ([commit](https://github.com/astronomer/airflow/commit/ec8dfba198a82644c54888dc9caf1c19a6930567))
- Don't install SQLAlchemy/Pendulum adapters for other DBs (#18745) ([commit](https://github.com/astronomer/airflow/commit/eb03da87599edfbd0b1fb615ab6df5811f9401f2))
- Add DagRun.logical_date as a property (#19198) ([commit](https://github.com/astronomer/airflow/commit/97314d3985f217be2501e7de8a8de9dc1a2a760b))
- Add test for interval timetable catchup=False (#19145) ([commit](https://github.com/astronomer/airflow/commit/a67c83866b6c0ce566ccb4ff61dae6e1b4b7ffe4))
- Clear ``ti.next_method`` and ``ti.next_kwargs`` on task finish (#19183) ([commit](https://github.com/astronomer/airflow/commit/a056d2957f98e3f7794dad50ecc7a96162c139c3))
- Create TI context with data interval compat layer (#19148) ([commit](https://github.com/astronomer/airflow/commit/c94f5faf358d6aa0f45121365ccbf2be767e6558))
- Faster PostgreSQL db migration to Airflow 2.2 (#19166) ([commit](https://github.com/astronomer/airflow/commit/68697ec7a5a9cd3983908ed2911d5cec773b7911))
- Fix queued dag runs changes catchup=False behaviour (#19130) ([commit](https://github.com/astronomer/airflow/commit/e6e6f3f49f18dd1f15e3f0ff88269f0de626b713))
- Prevent scheduler crash when serialized dag is missing (#19113) ([commit](https://github.com/astronomer/airflow/commit/78316ce18dec7d954c16e385c25113bde317640e))
- Ensure task state doesn't change when marked as failed/success/skipped (#19095) ([commit](https://github.com/astronomer/airflow/commit/2c569f4d45af5c7540004fa90ce17a48bb5cc18f))
- Change `ds`, `ts`, etc. back to use logical date (#19088) ([commit](https://github.com/astronomer/airflow/commit/d039c15147f427d1d1c6aff0e348147a9703e184))
- Relax packaging requirement (#19087) ([commit](https://github.com/astronomer/airflow/commit/f97b2ac38479c907a665bf674fa33845e6bbecd9))
- Row lock TI query in SchedulerJob._process_executor_events (#18975) ([commit](https://github.com/astronomer/airflow/commit/b7811c2165117dfde0bf9262de4e7ced827781db))
- Fix ``XCom.delete`` error in Airflow 2.2.0 (#18956) ([commit](https://github.com/astronomer/airflow/commit/0e8daeee355cf71b48eef0f68e15d4bef0fca79a))
- Fix catchup by limiting queued dagrun creation using max_active_runs (#18897) ([commit](https://github.com/astronomer/airflow/commit/e3fed9b272eef530b04a59261c75b8e03906a20c))
- Allow Param to support a default value of ``None`` (#19034) ([commit](https://github.com/astronomer/airflow/commit/bba4659faaf9ff667db97c9263bf4924406e7e50))
- Upgrade old DAG/task param format when deserializing from the DB (#18986) ([commit](https://github.com/astronomer/airflow/commit/5164f510456213026ce54cfb83a3c6b5911a8460))

Astronomer Certified 2.2.0-2, 2021-10-14
----------------------------------------

### Bugfixes

- Fix null exec date on insert to task_fail ([commit](https://github.com/astronomer/airflow/commit/c4a5eaa65))
- Try to move "dangling" rows in upgradedb ([commit](https://github.com/astronomer/airflow/commit/56bdc223a))

Astronomer Certified 2.2.0-1, 2021-10-11
----------------------------------------

User-facing CHANGELOG for AC 2.2.0+astro.1 from Airflow 2.2.0:

### Bugfixes

- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods ([commit](https://github.com/astronomer/airflow/commit/8648bf2ff7b11def3122af5f60b81168fcb8a8a2))
- [astro] Fix istio sidecar shutdown on newer GKE ([commit](https://github.com/astronomer/airflow/commit/84ae13c73))

### Improvements

- Docker: Upgrade to Debian Bullseye and Python 3.9 for AC 2.2.0-1 (#298)
