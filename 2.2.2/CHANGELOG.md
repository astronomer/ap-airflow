# Changelog

Astronomer Certified 2.2.2-2, 2022-01-19
----------------------------------------

### Security

- Updated `celery` to `5.2.3` to fix [CVE-2021-23727](https://nvd.nist.gov/vuln/detail/CVE-2021-23727) ([commit](https://github.com/astronomer/ap-airflow/commit/b7ce051b726978691f6f37cb1f2f00a3c88da56f))
- Updated `numpy` to `1.21.5` to fix [CVE-2021-33430](https://nvd.nist.gov/vuln/detail/CVE-2021-33430) ([commit](https://github.com/astronomer/ap-airflow/commit/953ec71d9228f0c6558d4cd9aa74b8ddb5dfd141))

### Bugfixes

- Fix labels used to find queued KubeExecutor pods (#19904) ([commit](https://github.com/astronomer/airflow/commit/3802c17eabe007a20c110ffa8389d66b1fd73f3f))
- Update [Astronomer FAB Security Manager](https://github.com/astronomer/astronomer-fab-securitymanager) to version [1.8.1](https://github.com/astronomer/astronomer-fab-securitymanager/releases/tag/v1.8.1)

Astronomer Certified 2.2.2-1, 2021-11-15
----------------------------------------

User-facing CHANGELOG for AC 2.2.2+astro.1 from Airflow 2.2.2:

### Bugfixes

- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/c065531014fc596a251d915bfa228cfb113a51a8))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods ([commit](https://github.com/astronomer/airflow/commit/11a80aede0d1b51e6c424e45805ef3b36d1debaf))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/6a477103a4ed7358e82a1560c1c64477f85949d3))
