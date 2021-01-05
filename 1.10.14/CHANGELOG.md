# Changelog

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
