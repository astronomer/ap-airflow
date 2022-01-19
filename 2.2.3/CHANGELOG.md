# Changelog

Astronomer Certified 2.2.3-2, 2022-01-19
----------------------------------------

No Airflow source changes.

### Security

- Updated `celery` to `5.2.3` to fix [CVE-2021-23727](https://nvd.nist.gov/vuln/detail/CVE-2021-23727) ([commit](https://github.com/astronomer/ap-airflow/commit/953ec71d9228f0c6558d4cd9aa74b8ddb5dfd141))
- Updated `numpy` to `1.21.5` to fix [CVE-2021-33430](https://nvd.nist.gov/vuln/detail/CVE-2021-33430) ([commit](https://github.com/astronomer/ap-airflow/commit/953ec71d9228f0c6558d4cd9aa74b8ddb5dfd141))

Astronomer Certified 2.2.3-1, 2021-12-21
----------------------------------------

User-facing CHANGELOG for AC 2.2.3+astro.1 from Airflow 2.2.3:

### Bugfixes

- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/0880b82a2d84cc1d6d46cf8acb31c627936dfa85))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/1f0e8bea4bb2656c0523a2f177a4dbf5b26ba48e))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/71e6ffdc57a818ac7af1abf195bff9047851b96a))
