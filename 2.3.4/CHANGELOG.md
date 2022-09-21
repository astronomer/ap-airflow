# Changelog

Astronomer Certified 2.3.4-2, 2022-09-21
----------------------------------------

### Bugfixes

- Properly build URL to retrieve logs independently from system ([#26337](https://github.com/apache/airflow/pull/26337))
- Fix proper joining of the path for logs retrieved from celery worker ([#26493](https://github.com/apache/airflow/pull/26493))
- Fix UI redirect ([#26409](https://github.com/apache/airflow/pull/26409))

### Security

- Updated `pcre2` to `10.36-2+deb11u1` to fix [CVE-2022-1586](https://avd.aquasec.com/nvd/cve-2022-1586) and [CVE-2022-1587](https://avd.aquasec.com/nvd/cve-2022-1587)
- Updated `glibc` to `2.31-13+deb11u4` to fix [CVE-2021-3999](https://avd.aquasec.com/nvd/cve-2021-3999)
- Updated `zlib` to `1:1.2.11.dfsg-2+deb11u2` to fix [CVE-2022-37434](https://avd.aquasec.com/nvd/cve-2022-37434)
- Updated `Mako` to `1.2.1` to fix [CVE-2022-40023](https://avd.aquasec.com/nvd/cve-2022-40023)

Astronomer Certified 2.3.4-1, 2022-08-25
----------------------------------------

User-facing CHANGELOG for AC 2.3.4+astro.1 from Airflow 2.3.4:

### Bugfixes

- fix broken auto-refresh ([#25950](http://github.com/astronomer/airflow/pull/25950))
- [astro] seed log_template table (#1497) ([commit](https://github.com/astronomer/airflow/commit/7587d608ae52eb1d593637a081d4bbe18b774c74))
- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/110a5cedfb9a59d2141e5ec56feaaff193ff03b8))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/7a2127cff859b96febe304cd715c460f060b371a))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/dcc7c87cd01f4c385dad3b1e2bdbc7a1cb47b6a7))
