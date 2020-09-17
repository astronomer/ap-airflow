# Changelog

Astronomer Certified 1.10.5-11.dev, 2020-09-17
----------------------------------------------

### Bug Fixes
- Webserver: Sanitize values passed to origin param (apache#10334) ([commit](https://github.com/astronomer/airflow/commit/4eda6ba))
- Dockerfile (buster): Add astro user to group 101 (#133)

### Improvements
- Upgrade npm to 6.14.8 ([commit](https://github.com/astronomer/airflow/commit/054e118))

Astronomer Certified 1.10.5-10, 2020-08-04
----------------------------------------------

### Bug Fixes
- Fix broken Configuration & Version navigation links ([commit](https://github.com/astronomer/airflow/commit/21de28e))
- Fix broken `/landing_times` View ([commit](https://github.com/astronomer/airflow/commit/6567df3))
- Add host name to task runner log ([commit](https://github.com/astronomer/airflow/commit/2696f87))
- Run Kubernetes Worker Pods as astro user ([commit](https://github.com/astronomer/ap-airflow/commit/f6819a4))
- **Dockerfile**: Exactly match `apache-airflow` in `requirements.txt` to restrict installation of 'apache-airflow' ([commit](https://github.com/astronomer/ap-airflow/commit/c2536db))

Astronomer Certified 1.10.5-9, 2020-06-18
--------------------------------------------

### Bug Fixes

- Block people from upgrading Airflow in the image ([commit](https://github.com/astronomer/ap-airflow/commit/bf517ea))
- Pin azure-storage-blob version to <12 ([commit](https://github.com/astronomer/airflow/commit/1794ea0))
- Azure storage 0.37.0 is not installable any more ([commit](https://github.com/astronomer/airflow/commit/cf9be33c))
- Pin Werkzeug < 1.0.0 release - 1.0.0 is not compatible ([commit](https://github.com/astronomer/airflow/commit/8a7549c5ff))
- Fix issue with SQLAlchemy 1.3.16 ([commit](https://github.com/astronomer/airflow/commit/a437cff))
- WTForms 2.3.0 break our Flask apps ([commit](https://github.com/astronomer/airflow/commit/3c74c75))

### Improvements

- Add man directories to buster images to fix jre install problems ([commit](https://github.com/astronomer/ap-airflow/commit/551995e))
- Don't use the `|safe` filter in code, it's risky ([commit](https://github.com/astronomer/airflow/commit/ba48ce8d72))
- Further validation that only task commands are run by executors ([commit](https://github.com/astronomer/airflow/commit/7e31614))
- Validate only task commands are run by executors ([commit](https://github.com/astronomer/airflow/commit/e2bf177))
- Fix Celery default to no longer allow pickle ([commit](https://github.com/astronomer/airflow/commit/8a3076b))
- Remove duplicate error message on chart connection failure ([commit](https://github.com/astronomer/airflow/commit/09c52d9))
- Add note about using dag_run.conf in BashOperator ([commit](https://github.com/astronomer/airflow/commit/17b4f06))

Astronomer Certified 1.10.5-8, 2020-06-03
--------------------------------------------

### Bug Fixes

- Fix pip install issue caused by Python3.7.7 packages on Alpine-based images ([commit](https://github.com/astronomer/ap-airflow/commit/6c400ad))

Astronomer Certified 1.10.5-7, 2020-04-27
--------------------------------------------

No changes in `astronomer/airflow` repo.

Dockerfile changes are:

- Upgrade sqlite3 packages for Alpine 3.10 to mitigate [CVE-2020-1967](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2020-1967) ([commit](https://github.com/astronomer/ap-airflow/commit/2f29d493259cddd487bcc306b829a4ec4a74f35e))
- Upgrade OpenSSL to mitigate [CVE-2019-16168](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-16168) ([commit](https://github.com/astronomer/ap-airflow/commit/6de11c2c87e78b7a3171d8fb222c7278fcb673c9))
- Constraint version of WTForms to non-broken version ([commit](https://github.com/astronomer/ap-airflow/commit/3cd34236f8a7214434dc313af525160133520bcb))
- JPype1 0.7.3 no longer installs on Alpline/musl-libc ([commit](https://github.com/astronomer/ap-airflow/commit/44164ba40cd1878cabeec5edc32fe0a7bb7a8e0d))


Astronomer Certified 1.10.5-6, 2020-03-30
-----------------------------------------------

### Bug Fixes

- Add Prestop hook to prevent logging issue (#469)
