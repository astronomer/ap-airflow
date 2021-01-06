# Changelog

Astronomer Certified 1.10.10-7, 2021-01-05
--------------------------------------------

### Bug Fixes

- Continually check if we should shut down istio contaner when running K8sPodOperator ([commit](https://github.com/astronomer/airflow/commit/ac71daea657589a45f30912ee3cc13521c077b6e))
- Pin `kubernetes` to a max version of 11.0.0 ([commit](https://github.com/astronomer/airflow/commit/d441d0e79f2f626c95e770499385a67bdfdc06b7))
- Bump ini from 1.3.5 to 1.3.8 in /airflow/www_rbac ([commit](https://github.com/astronomer/airflow/commit/a894d7104ad4d2c2d381ca91ead40e69abb6c344))
- Bump datatables.net from 1.10.21 to 1.10.22 in /airflow/www_rbac ([commit](https://github.com/astronomer/airflow/commit/6f91e2cf12077acda3a72e418fff4f04fab5f236))
- Respect LogFormat when using ES logging with Json Format ([commit](https://github.com/astronomer/airflow/commit/18644b500dce7178c74febda423847d2a666444a))

Astronomer Certified 1.10.10-6, 2020-12-10
--------------------------------------------

### Bug Fixes

- Sync FAB Permissions for all base views ([commit](https://github.com/astronomer/airflow/commit/a9636ef08a91a51b7a53885ec14b74e56b95309c))
- Show Generic Error for Charts & Query View in old UI ([commit](https://github.com/astronomer/airflow/commit/e6112803e6297a4e92eccc61d16b323f80ebd620))
- Webserver: Further Sanitize values passed to origin param ([commit](https://github.com/astronomer/airflow/commit/0f722476bcc4d3b06ee068b87430d3d544c15e56))
- Mask Password in Log table when using the CLI ([commit](https://github.com/astronomer/airflow/commit/a3d676099f022113fd92e0fd877d3805c5db38f7))
- [AIRFLOW-2809] Fix security issue regarding Flask SECRET_KEY ([commit](https://github.com/astronomer/airflow/commit/67de55ef854ede069b71244fa5602dbff7bb95db))
- [AIRFLOW-2884] Fix Flask SECRET_KEY security issue in www_rbac ([commit](https://github.com/astronomer/airflow/commit/b3711ff24059f79c1f89d5b5b3af675b54e18485))
- [AIRFLOW-2886] Generate random Flask SECRET_KEY in default config ([commit](https://github.com/astronomer/airflow/commit/cc91e3acc8a04882e66de21b251c04baff1190b7))
- Don't let webserver run with dangerous config ([commit](https://github.com/astronomer/airflow/commit/b1e2be786bdd74be369bfb3bb19c7cb1c1a067e1))
- Pin marshmallow-sqlalchemy for >= 3.6 ([commit](https://github.com/astronomer/airflow/commit/62572a44ca9495cb4c29c76ffdd0b3cb83dd4bc4))
- Pin marshmallow <= 2.21 ([commit](https://github.com/astronomer/airflow/commit/efa7193f2c5b30e8441e02dd48e0921ddd247cc0))
- Fix empty asctime field in JSON formatted logs ([commit](https://github.com/astronomer/airflow/commit/3d4386c68eacfac53607bac4ebbe5b19db1ced16))

### Improvements

- Dockerfile: Stop running `sync_perm` multiple times for Airflow >= 1.10.7 ([commit](https://github.com/astronomer/ap-airflow/commit/9c10dcf))
- Dockerfile: Bump astronomer_airflow_scripts to 0.0.5 ([commit](https://github.com/astronomer/ap-airflow/commit/42b4169))

Astronomer Certified 1.10.10-5, 2020-09-16
--------------------------------------------

### Bug Fixes

- Use Serialized DAGs to sync permissions when DAG Serialization is enabled ([commit](https://github.com/astronomer/airflow/commit/4f546071712728da3db0afcd9fcdabd5851acfd3))
- Webserver: Sanitize values passed to origin param ([commit](https://github.com/astronomer/airflow/commit/f89a3cfd7ef1d45a17b1354ba60711bc2539839d))
- Update JS packages to latest versions ([commit](https://github.com/astronomer/airflow/commit/655c7707c228fbf7bb3d2e6bd00515c9acb301f8))
- Avoid sharing session with RenderedTaskInstanceFields write and delete ([commit](https://github.com/astronomer/airflow/commit/46c6c43c7889b5df7d58ead33e5843b0ea98a9f6))
- Fix the trigger_dag api in the case of nested subdags ([commit](https://github.com/astronomer/airflow/commit/8c4c4979ca39441e0ce057f02d01f8dfe1773693))

Astronomer Certified 1.10.10-4, 2020-08-04
--------------------------------------------

### Bug Fixes

- Fix broken `/landing_times` View ([commit](https://github.com/astronomer/airflow/commit/a55b8f6))
- Run Kubernetes Worker Pods as astro user ([commit](https://github.com/astronomer/ap-airflow/commit/f6819a4))
- **Dockerfile**: Exactly match `apache-airflow` in `requirements.txt` to restrict installation of 'apache-airflow' ([commit](https://github.com/astronomer/ap-airflow/commit/c2536db))
- **Astro Version Check Plugin**: Only show warnings on old versions ([commit](https://github.com/astronomer/astronomer-airflow-version-check/commit/24ad49e))
- **Astro Version Check Plugin**: Make the plugin MySQL compatible ([commit](https://github.com/astronomer/astronomer-airflow-version-check/commit/0210f60))
- Fix Broken PapermillOperator ([commit](https://github.com/astronomer/astronomer-airflow-version-check/commit/811cc75))

Astronomer Certified 1.10.10-3, 2020-06-17
--------------------------------------------

### Bug Fixes

- [AIRFLOW-6959] Use NULL as dag.description default value ([commit](https://github.com/astronomer/airflow/commit/548f4be32))
- Block people from upgrading Airflow in the image ([commit](https://github.com/astronomer/ap-airflow/commit/bf517ea))

### Improvements

- Add man directories to buster images to fix jre install problems ([commit](https://github.com/astronomer/ap-airflow/commit/551995e))
- Fix Celery default to no longer allow pickle ([commit](https://github.com/astronomer/airflow/commit/45a2a3315))
- Don't use the `|safe` filter in code, it's risky ([commit](https://github.com/astronomer/airflow/commit/774a34e12))
- Further validation that only task commands are run by executors ([commit](https://github.com/astronomer/airflow/commit/c96af8e3f))
- Add note about using dag_run.conf in BashOperator ([commit](https://github.com/astronomer/airflow/commit/2591294df))
- Validate only task commands are run by executors ([commit](https://github.com/astronomer/airflow/commit/4aea266a6))

Astronomer Certified 1.10.10-2, 2020-06-03
--------------------------------------------

### Bug Fixes

- Fix pip install issue caused by Python3.7.7 packages on Alpine-based images
- BugFix: DAG trigger via UI error in RBAC UI ([commit](https://github.com/astronomer/airflow/commit/356b7b1))
- Remove duplicate error message on chart connection failure ([commit](https://github.com/astronomer/airflow/commit/c4ff230))
- Correctly deserialize dagrun_timeout field on DAGs ([commit](https://github.com/astronomer/airflow/commit/1f12f3f))
- Correctly store non-default Nones in serialized tasks/dags ([commit](https://github.com/astronomer/airflow/commit/2bf89bf))
- Correctly restore upstream_task_ids when deserializing Operators ([commit](https://github.com/astronomer/airflow/commit/bf04e3e))
- Make loading plugins from entrypoint fault-tolerant ([commit](https://github.com/astronomer/airflow/commit/35c068c))
- Stop showing Import Errors for Plugins in Webserver ([commit](https://github.com/astronomer/airflow/commit/ef70c9c))
- Azure storage 0.37.0 is not installable any more ([commit](https://github.com/astronomer/airflow/commit/072f947))
- Pin Version of Azure Cosmos to <4 ([commit](https://github.com/astronomer/airflow/commit/684653d))

Astronomer Certified 1.10.10-1, 2020-04-22
-----------------------------------------------

CHANGELOG for AC `1.10.10+astro.1` from Airflow `1.10.10`:


### New Features

- Add support for AWS Secrets Manager as Secrets Backend ([commit](https://github.com/apache/airflow/commit/75156fb23))
- [AIRFLOW-7049] Persistent display/filtering of DAG status ([commit](https://github.com/apache/airflow/commit/830987fd7))


### Bug Fixes

- [AIRFLOW-6576] Fix scheduler crash caused by deleted task with sla misses ([commit](https://github.com/apache/airflow/commit/))
- [AIRFLOW-6381] Remove styling based on DAG id from DAGs page ([commit](https://github.com/apache/airflow/commit/))
- Move `DAG._schedule_interval` logic out of `DAG.__init__` ([commit](https://github.com/apache/airflow/commit/a354cc3a1))
- Fix non updating DAG code by checking against last modification time ([commit](https://github.com/apache/airflow/commit/9166df5ef))
- RBAC ui: Fix missing task runs being rendered as circles instead ([commit](https://github.com/apache/airflow/commit/cd763cd1f))
- RBAC ui: Fix missing Y-axis labels with units in plots ([commit](https://github.com/apache/airflow/commit/1c5a1c121))
- [AIRFLOW-6697] fix modal_backdrop z-index ([commit](https://github.com/apache/airflow/commit/4066447f7))
- Fix Extra Links in Gannt View ([commit](https://github.com/apache/airflow/commit/504c711a6))
- WTForms 2.3.0 break our Flask apps ([commit](https://github.com/apache/airflow/commit/bb48dafe9))


### Improvements

- Improve add_dag_code_table migration ([commit](https://github.com/apache/airflow/commit/3dded72db))
- Consistent formatting in CSS files ([commit](https://github.com/apache/airflow/commit/b261516c8))
- [AIRFLOW-4235] Add table-hover css class to DAGs table ([commit](https://github.com/apache/airflow/commit/324954c7d))
- [AIRFLOW-7019] Show un/pause errors in dags view. ([commit](https://github.com/apache/airflow/commit/a99520180))
- [AIRFLOW-4038] Restructure database queries on /home ([commit](https://github.com/apache/airflow/commit/63260c995))
- [AIRFLOW-6351] Security - Add Cross Site Scripting defence ([commit](https://github.com/apache/airflow/commit/afa4b11fd))
- Make Gantt tooltip the same as Tree and Graph view ([commit](https://github.com/apache/airflow/commit/94757dd55))
- [AIRFLOW-6320] Add quarterly to crontab presets ([commit](https://github.com/apache/airflow/commit/5d1aaa90b))
- [AIRFLOW-6885] Delete worker on success ([commit](https://github.com/apache/airflow/commit/14ddf04b8))
- [AIRFLOW-6885] Change delete-on-success to delete-on-failure ([commit](https://github.com/apache/airflow/commit/27dc6c299))
