# Changelog

Astronomer Certified 2.2.0-2, 2021-10-14
---------------------------------

User-facing CHANGELOG for AC 2.2.0+astro.2 from Airflow 2.2.0:

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
