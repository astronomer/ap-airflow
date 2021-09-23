# Changelog

Astronomer Certified 1.10.14-5, TBC
--------------------------------------------

### Bug Fixes

- [astro] Fix istio sidecar shutdown on newer GKE ([commit](https://github.com/astronomer/airflow/commit/347e6433f))

Astronomer Certified 1.10.14-4, 2021-07-26
------------------------------------------

### Bugfixes

- Exclude ``yarn.lock`` from built Python wheel file (#16577) ([commit](https://github.com/astronomer/airflow/commit/25d46e4e9))
- [backport] Fix bug with `executor_config` and Volumes ([commit](https://github.com/astronomer/airflow/commit/e268afd5c))
- Only allow webserver to request from the worker log server (#16754) ([commit](https://github.com/astronomer/airflow/commit/815dcd5b4))
- Dockerfile: Add constraint for installed Airflow version (#274) ([commit](https://github.com/astronomer/ap-airflow/commit/60174ec))
- Dockerfile: Update / Override PIP version in Env Vars (#263) ([commit](https://github.com/astronomer/ap-airflow/commit/ab60218))
- Dockerfile: Bump Epoch to fix CVEs (#239) ([commit](https://github.com/astronomer/ap-airflow/commit/6522368))
- Dockerfile: Upgrade Fab Security Manager to 1.6.0

Astronomer Certified 1.10.14-3, 2021-03-18
------------------------------------------

### Bugfixes

- Fix `sync-perm` to work correctly when `update_fab_perms = False` (apache#14847) ([commit](https://github.com/astronomer/airflow/commit/c5ea249db4d1a5528118e4168f125da3eadb59ed))
- Webserver: Sanitize string passed to origin param (apache#14738) ([commit](https://github.com/astronomer/airflow/commit/d38d3625540a0d802470177a32efb5991158f70a))
- `KubernetesPodOperator` should retry log tailing in case of interruption (apache#11325) ([commit](https://github.com/astronomer/airflow/commit/0138e6aac25556e2cf44055a7de30351a131dabc))

Astronomer Certified 1.10.14-2, 2021-01-05
-----------------------------------------------

### Bug Fixes

- Bugfix: Unable to import Airflow plugins on Python 3.8 ([commit](https://github.com/astronomer/airflow/commit/b05400d97c3e5286a10a66667b8e14fa499fdcf1)
- Fix error in resolving env_from in KubernetesExecutor ([commit](https://github.com/astronomer/airflow/commit/095f4f4ad0b54fabd03dd82c995511523a9e3b74))
- Continually check if we should shut down istio contaner when running K8sPodOperator ([commit](https://github.com/astronomer/airflow/commit/17b3d2aba321826c2497f36dfb44947e22c61d31))
- Bump ini from 1.3.5 to 1.3.8 in /airflow/www_rbac ([commit](https://github.com/astronomer/airflow/commit/00dd241bbcfcb414490f8d65677862f8220f2774))
- Bump datatables.net from 1.10.21 to 1.10.22 in /airflow/www_rbac ([commit](https://github.com/astronomer/airflow/commit/b8191fa292e36e35293e3a79b6ec5fb3cbef2d3f))
- Include airflow/contrib/executors in the dist package ([commit](https://github.com/astronomer/airflow/commit/6240f44ef90f2dd9588e8ddbe8da7614ca357d6e))
- Respect LogFormat when using ES logging with Json Format ([commit](https://github.com/astronomer/airflow/commit/a6acb4964d6f48a145bb7d56302d81f12ec22b88))

Astronomer Certified 1.10.14-1, 2020-12-10
-----------------------------------------------

User-facing CHANGELOG for AC `1.10.14+astro.1` from Airflow `1.10.14`:

## Improvements

- Enable DAG Serialization by default ([commit](https://github.com/apache/airflow/commit/8a265067e))
- Stop showing Import Errors for Plugins in Webserver ([commit](https://github.com/apache/airflow/commit/ad871021b))
- Add role-based authentication backend ([commit](https://github.com/apache/airflow/commit/540eb0a0e))

## New Features
- Show "Warning" to Users with Duplicate Connections ([commit](https://github.com/apache/airflow/commit/0e40ddd8e))
