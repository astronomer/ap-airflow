# Changelog

Astronomer Certified 1.10.12-6, 2021-09-24
--------------------------------------------

### Bug Fixes

- [astro] Fix istio sidecar shutdown on newer GKE ([commit](https://github.com/astronomer/airflow/commit/c0d57d71f))

Astronomer Certified 1.10.12-5, 2021-07-26
-----------------------------------------------

### Bugfixes

- Only allow webserver to request from the worker log server (#16754) ([commit](https://github.com/astronomer/airflow/commit/0ec3decda))
- Exclude ``yarn.lock`` from built Python wheel file (#16577) ([commit](https://github.com/astronomer/airflow/commit/492573cd7))
- [backport] Fix bug with `executor_config` and Volumes ([commit](https://github.com/astronomer/airflow/commit/ae9a5ed41))
- Dockerfile: Add constraint for installed Airflow version (#274) ([commit](https://github.com/astronomer/ap-airflow/commit/60174ec))
- Dockerfile: Update / Override PIP version in Env Vars (#263) ([commit](https://github.com/astronomer/ap-airflow/commit/ab60218))
- Dockerfile: Bump Epoch to fix CVEs (#239) ([commit](https://github.com/astronomer/ap-airflow/commit/6522368))
- Dockerfile: Add missing '--no-cache-dir' in 1.10.12 alpine image (#230) ([commit](https://github.com/astronomer/ap-airflow/commit/6cc5015))
- Dockerfile: Upgrade Fab Security Manager to 1.6.0

Astronomer Certified 1.10.12-4, 2021-03-18
-----------------------------------------------

### Bugfixes

- Fix `sync-perm` to work correctly when `update_fab_perms = False` (apache#14847) ([commit](https://github.com/astronomer/airflow/commit/ee476eba705116cd4c2b01ede3645c13b6a226e6))
- Webserver: Sanitize string passed to origin param (apache#14738) ([commit](https://github.com/astronomer/airflow/commit/469faa82f5a449ea4d2c1317942b5ce5b2ae656f))

Astronomer Certified 1.10.12-3, 2021-01-05
-----------------------------------------------

### Bug Fixes

- Fix error in resolving env_from in KubernetesExecutor ([commit](https://github.com/astronomer/airflow/commit/b3b2a160026647069c1961b24cfcbc80d1a746c1))
- Continually check if we should shut down istio contaner when running K8sPodOperator ([commit](https://github.com/astronomer/airflow/commit/119b67569667ecb533f234edf7132c301fed140c))
- Bump ini from 1.3.5 to 1.3.8 in /airflow/www_rbac ([commit](https://github.com/astronomer/airflow/commit/588cfcf33942547e670de2edc73ed16b98967696))
- Bump datatables.net from 1.10.21 to 1.10.22 in /airflow/www_rbac ([commit](https://github.com/astronomer/airflow/commit/10cabc8b5dfb45a0adc6d3c4ae6efa0bbb265192))
- Respect LogFormat when using ES logging with Json Format ([commit](https://github.com/astronomer/airflow/commit/0bcd5fb8b43871def2841457ef7503009df8dc2c))

Astronomer Certified 1.10.12-2, 2020-12-04
-----------------------------------------------

### Bug Fixes

- SkipMixin: Handle empty branches ([commit](https://github.com/astronomer/airflow/commit/64a37512e))
- Sync FAB Permissions for all base views ([commit](https://github.com/astronomer/airflow/commit/3db82c98f))
- Fixes issue with affinity backcompat in Airflow 1.10 ([commit](https://github.com/astronomer/airflow/commit/aa13576d0))
- Fix empty asctime field in JSON formatted logs ([commit](https://github.com/astronomer/airflow/commit/21a9bd07c))
- Show Generic Error for Charts & Query View in old UI ([commit](https://github.com/astronomer/airflow/commit/d737558eb))
- Webserver: Further Sanitize values passed to origin param ([commit](https://github.com/astronomer/airflow/commit/728dbddf5))
- Mask Password in Log table when using the CLI ([commit](https://github.com/astronomer/airflow/commit/f746e3c75))
- Limit version of marshmallow-sqlalchemy ([commit](https://github.com/astronomer/airflow/commit/97a39dd19))
- Bump attrs to > 20.0 ([commit](https://github.com/astronomer/airflow/commit/2379b6a23))
- Bump attrs and cattrs dependencies ([commit](https://github.com/astronomer/airflow/commit/dad229d71))
- Install cattr on Python 3.7 ([commit](https://github.com/astronomer/airflow/commit/dacc4ab8c))
- Pin `kubernetes` to a max version of 11.0.0 ([commit](https://github.com/astronomer/airflow/commit/d9a90c26c))
- Pin pyzmq<20.0 for Alpine images ([commit](https://github.com/astronomer/ap-airflow/commit/3059797))
- Dockerfile: Add `sync_perm` command to buster images ([commit](https://github.com/astronomer/ap-airflow/commit/5a28d3f))
- BugFix: Tasks with depends_on_past or task_concurrency are stuck ([commit](https://github.com/astronomer/airflow/commit/381a55009))
- Fix issue with empty Resources in executor_config ([commit](https://github.com/astronomer/airflow/commit/d5b89e88e))
- [AIRFLOW-2809] Fix security issue regarding Flask SECRET_KEY ([commit](https://github.com/astronomer/airflow/commit/91f64a3d1))
- [AIRFLOW-2884] Fix Flask SECRET_KEY security issue in www_rbac ([commit](https://github.com/astronomer/airflow/commit/f0b4547d5))
- [AIRFLOW-2886] Generate random Flask SECRET_KEY in default config ([commit](https://github.com/astronomer/airflow/commit/2efe39197))
- Don't let webserver run with dangerous config ([commit](https://github.com/astronomer/airflow/commit/075d4ddb0))

### Improvements

- [AIRFLOW-3607] Only query DB once per DAG run for TriggerRuleDep ([commit](https://github.com/astronomer/airflow/commit/7693514bb))
- [AIRFLOW-3607] Optimize dep checking when depends on past set and concurrency limit ([commit](https://github.com/astronomer/airflow/commit/63bb7f3ae))
- Dockerfile: Stop running `sync_perm` multiple times for Airflow >= 1.10.7 ([commit](https://github.com/astronomer/ap-airflow/commit/9c10dcf))
- Dockerfile: Bump astronomer_airflow_scripts to 0.0.5 ([commit](https://github.com/astronomer/ap-airflow/commit/42b4169))
- Dockerfile: Use Airflow Constraints file for AC 1.10.12 and 1.10.13 ([commit](https://github.com/astronomer/ap-airflow/commit/e968f12))

Astronomer Certified 1.10.12-1, 2020-09-29
-----------------------------------------------

CHANGELOG for AC `1.10.12+astro.1` from Airflow `1.10.12`:

### Bug Fixes

- Add role-based authentication backend ([commit](https://github.com/astronomer/airflow/commit/49d4840))
- KubernetesPodOperator template fix (#10963) ([commit](https://github.com/astronomer/airflow/commit/259f1b797))
- Fix operator field update for SerializedBaseOperator ([commit](https://github.com/astronomer/airflow/commit/cfc9732d7))
- Fix pod_mutation_hook ([commit](https://github.com/astronomer/airflow/commit/73b5fe1aa))
- Fix formatting of Host information ([commit](https://github.com/astronomer/airflow/commit/4d820744c))

### Improvements

- Adding body as templated field for CloudSqlImportOperator ([commit](https://github.com/astronomer/airflow/commit/18e3a3b))
- Stop showing Import Errors for Plugins in Webserver ([commit](https://github.com/astronomer/airflow/commit/ac17612))
- Restrict 'nteract-scrapbook' to <0.4 ([commit](https://github.com/astronomer/airflow/commit/b4312ef))
- Enable DAG Serialization by default ([commit](https://github.com/astronomer/airflow/commit/8da0ad8))
- Remove deprecation warning from contrib/kubernetes/pod.py ([commit](https://github.com/astronomer/airflow/commit/5721d39))
- Make grace_period_seconds option on KubernetesPodOperator ([commit](https://github.com/astronomer/airflow/commit/236b9b3b2))
- Add on_kill support for the KubernetesPodOperator ([commit](https://github.com/astronomer/airflow/commit/ce94497cc))

### New Features

- Add Secrets backend for Microsoft Azure Key Vault ([commit](https://github.com/astronomer/airflow/commit/908515f13))
