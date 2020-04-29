# Changelog

Astronomer Certified 1.10.7-9, 2020-04-28
--------------------------------------------

No user-facing changes in `astronomer/airflow` repo.

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
