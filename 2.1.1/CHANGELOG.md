# Changelog

Astronomer Certified 2.1.1-2, 2021-07-13
----------------------------------------

### Bugfixes

- [astro] Handle Istio containers with Kubernetes Executor Pod adoption (#1318) ([commit](https://github.com/astronomer/airflow/commit/98abd2fb7))
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
