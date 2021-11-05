# Changelog

Astronomer Certified 2.1.1-5.dev, 2021-11-05
--------------------------------------------

### Bug Fixes

- Dockerfile: Fix `CVE-2021-33503` in AC 2.1.1 ([commit](https://github.com/astronomer/ap-airflow/commit/b511b30))
- Only mark SchedulerJobs as failed, not any jobs (#19375) ([commit](https://github.com/astronomer/airflow/commit/91f8f6f))

Astronomer Certified 2.1.1-4, 2021-09-24
--------------------------------------------

### Bug Fixes

- [astro] Fix istio sidecar shutdown on newer GKE ([commit](https://github.com/astronomer/airflow/commit/ad5a98ff8))

Astronomer Certified 2.1.1-3, 2021-09-08
----------------------------------------

### Bugfixes

- Add missing permissions to `varimport` (#17468) ([commit](https://github.com/astronomer/airflow/commit/f5c0a8db1))
- Dockerfile: Pin `elasticsearch` python client version to `7.13.4` (#294)
- Dockerfile: Update pip to latest version in buster images (#289)

Astronomer Certified 2.1.1-2, 2021-07-13
----------------------------------------

### Bugfixes

- [astro] Handle Istio containers with Kubernetes Executor Pod adoption (#1318) ([commit](https://github.com/astronomer/airflow/commit/12349a100))
- Introduce compat shim airflow.compat.functools (#15969) ([commit](https://github.com/astronomer/airflow/commit/72521e457))
- Add Python 3.9 support (#15515) (#16883) ([commit](https://github.com/astronomer/airflow/commit/9b96fd1b9))
- Fix ``CeleryKubernetesExecutor`` (#16700) ([commit](https://github.com/astronomer/airflow/commit/90aaf3d48))
- yarn audit (#16440) ([commit](https://github.com/astronomer/airflow/commit/40accb2a4))
- Fix impersonation issue with LocalTaskJob (#16852) ([commit](https://github.com/astronomer/airflow/commit/075622cbe))
- Mask value if the key is ``token`` (#16474) ([commit](https://github.com/astronomer/airflow/commit/5834fb7ce))
- Only allow webserver to request from the worker log server (#16754) ([commit](https://github.com/astronomer/airflow/commit/74fa1325c))
- Set process title for ``serve-logs`` and ``LocalExecutor`` (#16644) ([commit](https://github.com/astronomer/airflow/commit/d8d851d70))
- Fix: Marking Task as success/failed ([commit](https://github.com/astronomer/airflow/commit/df1ff499c))
- Fix "Invalid JSON configuration, must be a dict" (#16648) ([commit](https://github.com/astronomer/airflow/commit/2637d9a15))

Astronomer Certified 2.1.1-1, 2021-07-02
----------------------------------------

User-facing CHANGELOG for AC 2.1.1+astro.1 from Airflow 2.1.1:

### Bugfixes

- Fix TI success/failure links ([commit](https://github.com/astronomer/airflow/commit/8f598f6fa))
- Fix TI success confirm page (#16650) ([commit](https://github.com/astronomer/airflow/commit/b0aaf266f))
- Fail tasks in scheduler when executor reports they failed (#15929) ([commit](https://github.com/astronomer/airflow/commit/fa7a14daa))
- Fix bug in mark TI success api (#16524) ([commit](https://github.com/astronomer/airflow/commit/ebae41f0e))
- Fix TI success/failure links (#16233) ([commit](https://github.com/astronomer/airflow/commit/1fb970f90))
- [astro] Continually check if we should shut down istio contaner when running K8sPodOperator ([commit](https://github.com/astronomer/airflow/commit/5c5dee67b))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/320675746))
