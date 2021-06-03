# Changelog

Astronomer Certified 2.1.0-2, 2021-06-03
----------------------------------------

## Bugfixes

- Update Kubernetes Provider to `1!1.2.1` to fix Pod hanging due to Istio container
- Don't die when masking `log.exception` when there is no exception (#16047) ([commit](https://github.com/astronomer/airflow/commit/e24040de6))
- Ensure that we don't try to mask empty string in logs (#16057) ([commit](https://github.com/astronomer/airflow/commit/d20eaa86c))
- Fill the "job_id" field for `airflow task run` without `--local`/`--raw` for KubeExecutor (#16108) ([commit](https://github.com/astronomer/airflow/commit/55fc6f6d8))
- Fix auto-refresh in tree view When webserver ui is not in ``/`` (#16018) ([commit](https://github.com/astronomer/airflow/commit/0c1d91917))

##Improvements

- Parse recently modified files even if just parsed (#16075) ([commit](https://github.com/astronomer/airflow/commit/19b3f1bd8))

Astronomer Certified 2.1.0-1, 2021-05-21
----------------------------------------
User-facing CHANGELOG for AC 2.1.0+astro.1 from Airflow 2.1.0:

## Bugfixes

- [astro] Continually check if we should shut down istio contaner when running K8sPodOperator ([commit](https://github.com/astronomer/airflow/commit/40a852bda))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/47528ff07))
- [astro-new]Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/3d3e35e7d))
