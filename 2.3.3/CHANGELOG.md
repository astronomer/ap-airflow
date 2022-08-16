# Changelog

Astronomer Certified 2.3.3-2, 2022-08-16
----------------------------------------

## Bug Fixes

- Only load distribution of a name once ([#25296](https://github.com/apache/airflow/pull/25296))
- Ensure that zombie tasks for dags with errors get cleaned up ([#25550](https://github.com/apache/airflow/pull/25550))
- Clear next method when clearing TIs ([#23929](https://github.com/apache/airflow/pull/23929))

## Security

- Updated `curl` to `7.74.0-1.3+deb11u2` to fix [DSA-5197](https://www.debian.org/security/2022/dsa-5197)
- Updated `gnutls` to `3.7.1-5+deb11u2` to fix [CVE-2022-2509](https://avd.aquasec.com/nvd/cve-2022-2509)
- Updated `libtirpc` to `1.3.1-1+deb11u1` to fix [CVE-2021-46828](https://avd.aquasec.com/nvd/cve-2021-46828)


Astronomer Certified 2.3.3-1, 2022-07-11
----------------------------------------

User-facing CHANGELOG for AC 2.3.3+astro.1 from Airflow 2.3.3:

### Bugfixes

- Fix zombie task handling with multiple schedulers ([#24906](https://github.com/apache/airflow/pull/24906))
- TriggerDagRunOperator.operator_extra_links is attr ([#24676](https://github.com/apache/airflow/pull/24676))
- [astro] seed log_template table (#1497) ([commit](https://github.com/astronomer/airflow/commit/6d80ff139d07746991653eee682601d04b94ad74))
- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/ce1708d0aadba792a977db82c585776f4fee672e))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/c42ed38f590be13c4ebae2634d83f674e45d394b))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/b9436bb013d8fd02f4f83ba00c56df32a89270ea))
