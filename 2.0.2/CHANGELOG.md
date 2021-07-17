# Changelog

Astronomer Certified 2.0.2-4, 2021-07-13
----------------------------------------

### Bugfixes

- [astro] Handle Istio containers with Kubernetes Executor Pod adoption (#1318) ([commit](https://github.com/astronomer/airflow/commit/1141c186f))
- Only allow webserver to request from the worker log server (#16754) ([commit](https://github.com/astronomer/airflow/commit/ebf2e305c))
- Avoid recursing too deep when redacting logs (#16491) ([commit](https://github.com/astronomer/airflow/commit/de563e385))
- Switch to built-in data structures in SecretsMasker (#16424) ([commit](https://github.com/astronomer/airflow/commit/523bba07e))
- Don't fail to log if we can't redact something (#16118) ([commit](https://github.com/astronomer/airflow/commit/ae0d11995))
- Don't show stale Serialized DAGs if they are deleted in DB (#16368) ([commit](https://github.com/astronomer/airflow/commit/c95f6d96f))
- Fix Orphaned tasks stuck in CeleryExecutor as running (#16550) ([commit](https://github.com/astronomer/airflow/commit/d44c223c1))
- Redact conn secrets in webserver logs (#16579) ([commit](https://github.com/astronomer/airflow/commit/836803b64))
- Don't crash attempting to mask secrets in dict with non-string keys (#16601) ([commit](https://github.com/astronomer/airflow/commit/a1f3daf7f))
- Fix Dag Details start date bug (#16206) ([commit](https://github.com/astronomer/airflow/commit/39ff9d198))
- Make task ID on legend have enough width and width of line chart to be 100%.  (#15915) ([commit](https://github.com/astronomer/airflow/commit/44ddad0e6))
- Clean Markdown with dedent to respect indents (#16414) ([commit](https://github.com/astronomer/airflow/commit/19b303e27))
- Exclude ``yarn.lock`` from built Python wheel file (#16577) ([commit](https://github.com/astronomer/airflow/commit/99d5ebd1f))
- Add `passphrase` and `private_key` to default sensitive fileld names (#16392) ([commit](https://github.com/astronomer/airflow/commit/aba6acbda))
- Dockerfile: Add constraint for installed Airflow version (#274) ([commit](https://github.com/astronomer/ap-airflow/commit/60174ec))
- Dockerfile: Upgrade Fab Security manager to 1.6.0 (#272) ([commit](https://github.com/astronomer/ap-airflow/commit/417fd5993982e49424fb427941552d0d42ed567e))

Astronomer Certified 2.0.2-3, 2021-06-03
----------------------------------------

### Bugfixes

- Update Kubernetes Provider to `1!1.2.1` to fix Pod hanging due to Istio container
- Fill the "job_id" field for `airflow task run` without `--local`/`--raw` for KubeExecutor (#16108) ([commit](https://github.com/astronomer/airflow/commit/7a6492e70))
- Ensure that we don't try to mask empty string in logs (#16057) ([commit](https://github.com/astronomer/airflow/commit/215758c0a))
- Don't die when masking `log.exception` when there is no exception (#16047) ([commit](https://github.com/astronomer/airflow/commit/c4c2ab288))
- Ensure that secrets are masked no matter what logging config is in use (#15899) ([commit](https://github.com/astronomer/airflow/commit/3e61ccddd))

### Improvements

- Parse recently modified files even if just parsed (#16075) ([commit](https://github.com/astronomer/airflow/commit/cb21b0aca))

Astronomer Certified 2.0.2-2, 2021-05-12
----------------------------------------

- Mask passwords and sensitive info in task logs and UI (#15599) ([commit](https://github.com/astronomer/airflow/commit/7378d458d))
- Bump stylelint to remove vulnerable sub-dependency (#15784) ([commit](https://github.com/astronomer/airflow/commit/838ace342))
- Add resolution to force dependencies to use patched version of lodash (#15777) ([commit](https://github.com/astronomer/airflow/commit/05757577f))
- Remove unused dependency (#15762) ([commit](https://github.com/astronomer/airflow/commit/25cd6b6ed))
- Docker: Bump `apache-airflow-providers-cncf-kubernetes` to `1.2.0`
- Docker: Bump `apache-airflow-providers-elasticsearch` to `1.0.4`

Astronomer Certified 2.0.2-1, 2021-04-26
----------------------------------------

User-facing CHANGELOG for AC 2.0.2+astro.1 from Airflow 2.0.2:

### Bugfixes

- Fix critical CeleryKubernetesExecutor bug (#13247) ([commit](https://github.com/astronomer/airflow/commit/02f780295))
- Fix deprecated provider aliases (#15465) ([commit](https://github.com/astronomer/airflow/commit/b3664d9a0))
- Further fix trimmed `pod_id` for `KubernetesPodOperator` (#15445) ([commit](https://github.com/astronomer/airflow/commit/085bfc3f9))
- Bugfix: Invalid name when trimmed `pod_id` ends with hyphen in ``KubernetesPodOperator`` (#15443) ([commit](https://github.com/astronomer/airflow/commit/cdfe3b0b6))
- Fix `sync-perm` to work correctly when update_fab_perms = False (#14847) ([commit](https://github.com/astronomer/airflow/commit/06c3630ad))
- [astro] Continually check if we should shut down istio contaner when running K8sPodOperator ([commit](https://github.com/astronomer/airflow/commit/ff080c3fd))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/baeb8367e))
- [astro] Fix logs downloading for tasks (#63) ([commit](https://github.com/astronomer/airflow/commit/e31d293da))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/aa876183e))

### Improvements

- Skip DAG perm sync during parsing if possible (#15464) ([commit](https://github.com/astronomer/airflow/commit/ab297b731))
- Sync DAG specific permissions when parsing (#15311) ([commit](https://github.com/astronomer/airflow/commit/4bedb7b1f))
- Finish refactor of DAG resource name helper (#15511) ([commit](https://github.com/astronomer/airflow/commit/fd86869a8))
- Elasticsearch: Add Traceback in LogRecord in ``JSONFormatter`` (#15414) ([commit](https://github.com/astronomer/airflow/commit/9a913fe97))

### New Features

- Add different modes to sort dag files for parsing (#15046) ([commit](https://github.com/astronomer/airflow/commit/60c71b7cd))
