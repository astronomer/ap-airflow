# Changelog

Astronomer Certified 1.10.10-2.dev, [DEV Package]
-----------------------------------------------

### Bug Fixes

- Fix pip install issue caused by Python3.7.7 packages on Alpine-based images


Astronomer Certified 1.10.10-1, 2020-04-22
-----------------------------------------------

CHANGELOG for AC `1.10.10+astro.1` from Airflow `1.10.10`:


### New Features

- Add support for AWS Secrets Manager as Secrets Backend ([commit](https://github.com/apache/airflow/commit/75156fb23))
- [AIRFLOW-7049] Persistent display/filtering of DAG status ([commit](https://github.com/apache/airflow/commit/830987fd7))


### Bug Fixes

- [AIRFLOW-6576] Fix scheduler crash caused by deleted task with sla misses ([commit](https://github.com/apache/airflow/commit/))
- [AIRFLOW-6381] Remove styling based on DAG id from DAGs page ([commit](https://github.com/apache/airflow/commit/))
- Move `DAG._schedule_interval` logic out of `DAG.__init__` ([commit](https://github.com/apache/airflow/commit/a354cc3a1))
- Fix non updating DAG code by checking against last modification time ([commit](https://github.com/apache/airflow/commit/9166df5ef))
- RBAC ui: Fix missing task runs being rendered as circles instead ([commit](https://github.com/apache/airflow/commit/cd763cd1f))
- RBAC ui: Fix missing Y-axis labels with units in plots ([commit](https://github.com/apache/airflow/commit/1c5a1c121))
- [AIRFLOW-6697] fix modal_backdrop z-index ([commit](https://github.com/apache/airflow/commit/4066447f7))
- Fix Extra Links in Gannt View ([commit](https://github.com/apache/airflow/commit/504c711a6))
- WTForms 2.3.0 break our Flask apps ([commit](https://github.com/apache/airflow/commit/bb48dafe9))


### Improvements

- Improve add_dag_code_table migration ([commit](https://github.com/apache/airflow/commit/3dded72db))
- Consistent formatting in CSS files ([commit](https://github.com/apache/airflow/commit/b261516c8))
- [AIRFLOW-4235] Add table-hover css class to DAGs table ([commit](https://github.com/apache/airflow/commit/324954c7d))
- [AIRFLOW-7019] Show un/pause errors in dags view. ([commit](https://github.com/apache/airflow/commit/a99520180))
- [AIRFLOW-4038] Restructure database queries on /home ([commit](https://github.com/apache/airflow/commit/63260c995))
- [AIRFLOW-6351] Security - Add Cross Site Scripting defence ([commit](https://github.com/apache/airflow/commit/afa4b11fd))
- Make Gantt tooltip the same as Tree and Graph view ([commit](https://github.com/apache/airflow/commit/94757dd55))
- [AIRFLOW-6320] Add quarterly to crontab presets ([commit](https://github.com/apache/airflow/commit/5d1aaa90b))
- [AIRFLOW-6885] Delete worker on success ([commit](https://github.com/apache/airflow/commit/14ddf04b8))
- [AIRFLOW-6885] Change delete-on-success to delete-on-failure ([commit](https://github.com/apache/airflow/commit/27dc6c299))
