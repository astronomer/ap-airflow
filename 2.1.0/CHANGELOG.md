# Changelog

Astronomer Certified 2.1.0-6.dev, 2021-11-05
--------------------------------------------

### Bug Fixes

- Dockerfile: Fix `CVE-2021-21240` and `CVE-2021-33503` in 2.1.0 ([commit](https://github.com/astronomer/ap-airflow/commit/5ccde33))
- Only mark SchedulerJobs as failed, not any jobs (#19375) ([commit](https://github.com/astronomer/airflow/commit/3b4d947))

Astronomer Certified 2.1.0-5, 2021-09-24
--------------------------------------------

### Bug Fixes

- [astro] Fix istio sidecar shutdown on newer GKE ([commit](https://github.com/astronomer/airflow/commit/d50737791))

Astronomer Certified 2.1.0-4, 2021-09-08
----------------------------------------

## Bugfixes

- Add missing permissions to `varimport` (#17468) ([commit](https://github.com/astronomer/airflow/commit/57f1629f8))
- Dockerfile: Pin `elasticsearch` python client version to `7.13.4` (#294)
- Dockerfile: Update pip to latest version in buster images (#289)

Astronomer Certified 2.1.0-3, 2021-07-13
----------------------------------------

## Bugfixes

- [astro] Handle Istio containers with Kubernetes Executor Pod adoption (#1318) ([commit](https://github.com/astronomer/airflow/commit/58cfc68bf))
- Only allow webserver to request from the worker log server (#16754) ([commit](https://github.com/astronomer/airflow/commit/a2b574c0c))
- Avoid recursing too deep when redacting logs (#16491) ([commit](https://github.com/astronomer/airflow/commit/5398eb5ab))
- Switch to built-in data structures in SecretsMasker (#16424) ([commit](https://github.com/astronomer/airflow/commit/7e5968aaa))
- Don't fail to log if we can't redact something (#16118) ([commit](https://github.com/astronomer/airflow/commit/41ae7090d))
- Don't show stale Serialized DAGs if they are deleted in DB (#16368) ([commit](https://github.com/astronomer/airflow/commit/9d14b1d6d))
- fix: change graph focus to top of view instead of center (#16484) ([commit](https://github.com/astronomer/airflow/commit/9eca94bb6))
- Fix Orphaned tasks stuck in CeleryExecutor as running (#16550) ([commit](https://github.com/astronomer/airflow/commit/83fb4bf9e))
- Redact conn secrets in webserver logs (#16579) ([commit](https://github.com/astronomer/airflow/commit/9ac87a9cf))
- Don't crash attempting to mask secrets in dict with non-string keys (#16601) ([commit](https://github.com/astronomer/airflow/commit/6af516b29))
- Fix Dag Details start date bug (#16206) ([commit](https://github.com/astronomer/airflow/commit/8d40ce481))
- Tree View UI for larger DAGs & more consistent spacing in Tree View (#16522) ([commit](https://github.com/astronomer/airflow/commit/f3fb06ce5))
- Make task ID on legend have enough width and width of line chart to be 100%.  (#15915) ([commit](https://github.com/astronomer/airflow/commit/8b2a7b75c))
- Fix normalize-url vulnerability (#16375) ([commit](https://github.com/astronomer/airflow/commit/58357b578))
- Clean Markdown with dedent to respect indents (#16414) ([commit](https://github.com/astronomer/airflow/commit/26abb8d37))
- add num_runs query param for tree refresh (#16437) ([commit](https://github.com/astronomer/airflow/commit/71feed690))
- set max tree width to 1200px (#16067) ([commit](https://github.com/astronomer/airflow/commit/9bcfd97d7))
- Exclude ``yarn.lock`` from built Python wheel file (#16577) ([commit](https://github.com/astronomer/airflow/commit/8fcc68d88))
- Bump version to 2.1.0.dev1+astro.3 ([commit](https://github.com/astronomer/airflow/commit/2700c8cf3))
- Add `passphrase` and `private_key` to default sensitive fileld names (#16392) ([commit](https://github.com/astronomer/airflow/commit/5917abf11))
- Dockerfile: Add constraint for installed Airflow version (#274) ([commit](https://github.com/astronomer/ap-airflow/commit/60174ec))
- Dockerfile: Upgrade Fab Security manager to 1.6.0 (#272) ([commit](https://github.com/astronomer/ap-airflow/commit/417fd5993982e49424fb427941552d0d42ed567e))

Astronomer Certified 2.1.0-2, 2021-06-03
----------------------------------------

## Bugfixes

- Update Kubernetes Provider to `1!1.2.1` to fix Pod hanging due to Istio container
- Don't die when masking `log.exception` when there is no exception (#16047) ([commit](https://github.com/astronomer/airflow/commit/e24040de6))
- Ensure that we don't try to mask empty string in logs (#16057) ([commit](https://github.com/astronomer/airflow/commit/d20eaa86c))
- Fill the "job_id" field for `airflow task run` without `--local`/`--raw` for KubeExecutor (#16108) ([commit](https://github.com/astronomer/airflow/commit/55fc6f6d8))
- Fix auto-refresh in tree view When webserver ui is not in ``/`` (#16018) ([commit](https://github.com/astronomer/airflow/commit/0c1d91917))

## Improvements

- Parse recently modified files even if just parsed (#16075) ([commit](https://github.com/astronomer/airflow/commit/19b3f1bd8))

Astronomer Certified 2.1.0-1, 2021-05-21
----------------------------------------
User-facing CHANGELOG for AC 2.1.0+astro.1 from Airflow 2.1.0:

## Bugfixes

- [astro] Continually check if we should shut down istio contaner when running K8sPodOperator ([commit](https://github.com/astronomer/airflow/commit/40a852bda))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/47528ff07))
- [astro-new]Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/3d3e35e7d))
