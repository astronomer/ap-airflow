# Changelog

Astronomer Certified 2.1.3-3, 2021-11-13
----------------------------------------

### Bug Fixes

- Dockerfile: Fix `CVE-2021-33503` in AC 2.1.1 ([commit](https://github.com/astronomer/ap-airflow/commit/b511b30))
- Only mark SchedulerJobs as failed, not any jobs (#19375) ([commit](https://github.com/astronomer/airflow/commit/60e80df))
- Backport bugfix: fix last run not loading ([commit](https://github.com/astronomer/airflow/commit/628ed10))

Astronomer Certified 2.1.3-2, 2021-09-24
--------------------------------------------

### Bug Fixes

- [astro] Fix istio sidecar shutdown on newer GKE ([commit](https://github.com/astronomer/airflow/commit/1883d7a06))

Astronomer Certified 2.1.3-1, 2021-08-23
----------------------------------------

User-facing CHANGELOG for AC 2.1.3+astro.1 from Airflow 2.1.3:

### Bugfixes

- [astro] Handle Istio containers with Kubernetes Executor Pod adoption (#1318) ([commit](https://github.com/astronomer/airflow/commit/26d52248b))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/dc8b2a999))
- Use `1!2.0.2` version of Kubernetes Provider
- Dockerfile: Use latest version of `pip`: `21.2.4`
