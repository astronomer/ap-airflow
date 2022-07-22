# Changelog

Astronomer Certified 2.1.4-9, 2022-07-22
----------------------------------------

### Bug Fixes

- [astro] Fix graph view states([commit](https://github.com/astronomer/airflow/commit/b23be74bb48c2dc4593dacdb2d81b77dac03eae4))

### Security

- Updated `libssl1.1` and `openssl` to `1.1.1n-0+deb10u3` to fix [CVE-2022-2068](https://avd.aquasec.com/nvd/CVE-2022-2068)([commit](https://github.com/astronomer/ap-airflow/commit/5214a321d2f2af21a1184f97ddc1b1eed8397106))

Astronomer Certified 2.1.4-8, 2022-06-22
----------------------------------------
### Security

- Updated `httpx` to `0.20.0` to fix [CVE-2021-41945](https://avd.aquasec.com/nvd/cve-2021-41945)([commit](https://github.com/astronomer/ap-airflow/commit/761a089fcd3bc9ab1227af78a3f4007a5e956270))
- Updated `libssl1.1` and `openssl` to `1.1.1n-0+deb10u2` to fix [CVE-2022-1292](https://avd.aquasec.com/nvd/cve-2022-1292)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `libpq5` to `11.16-0+deb10u1` to fix [CVE-2022-1552](https://avd.aquasec.com/nvd/cve-2022-1552)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `liblzma5` to `5.2.4-1+deb10u1` to fix [CVE-2022-1271](https://avd.aquasec.com/nvd/cve-2022-1271)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `libldap-2.4-2` and `libldap-common` to `2.4.47+dfsg-3+deb10u7` to fix [CVE-2022-29155](https://avd.aquasec.com/nvd/cve-2022-29155)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `gzip` to `1.9-3+deb10u1` to fix [CVE-2022-1271](https://avd.aquasec.com/nvd/cve-2022-1271)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `dpkg` to `1.19.8` to fix [CVE-2022-1664](https://avd.aquasec.com/nvd/cve-2022-1664)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))

Astronomer Certified 2.1.4-7, 2022-04-04
----------------------------------------

### Security

- Updated `mariadb-common` and `libmariadb3` to `1:10.3.34-0+deb10u1` to fix [CVE-2021-43618](https://nvd.nist.gov/vuln/detail/CVE-2021-43618) ([commit](https://github.com/astronomer/ap-airflow/commit/8642c845c719b14faf89d1901fcade24250ff78e))
- Updated `libgmp10` to `2:6.1.2+dfsg-4+deb10u1` to fix [CVE-2021-46667](https://nvd.nist.gov/vuln/detail/CVE-2021-46667), [CVE-2022-24048](https://nvd.nist.gov/vuln/detail/CVE-2022-24048), [CVE-2022-24050](https://nvd.nist.gov/vuln/detail/CVE-2022-24050), [CVE-2022-24051](https://nvd.nist.gov/vuln/detail/CVE-2022-24051), and [CVE-2022-24052](https://nvd.nist.gov/vuln/detail/CVE-2022-24052) ([commit](https://github.com/astronomer/ap-airflow/commit/8642c845c719b14faf89d1901fcade24250ff78e))
- Updated `zlib` to `1:1.2.11.dfsg-1+deb10u1` to fix [CVE-2018-25032](https://nvd.nist.gov/vuln/detail/CVE-2018-25032) ([commit](https://github.com/astronomer/ap-airflow/commit/c10118eb41df281863d6de702dfeefe33b179489))

### Bug Fixes

- Do not log the hook connection details even at DEBUG level ([commit](https://github.com/astronomer/airflow/commit/053e4eb2ddd1c0b2eeae437ea7fec1edf32b90df))

Astronomer Certified 2.1.4-6, 2022-02-24
----------------------------------------

### Bug Fixes

- Upgrade FAB Security Manager to `1.8.4` ([commit](https://github.com/astronomer/ap-airflow/commit/0bd531351cdc37dd0fbd6d76c3b680615b31241e))

Astronomer Certified 2.1.4-5, 2022-02-24
----------------------------------------

### Security

- Simplify trigger cancel button (#21591) to fix [CVE-2021-45229](https://nvd.nist.gov/vuln/detail/CVE-2021-45229) ([commit](https://github.com/astronomer/airflow/commit/4ee86ad2eec68f0c14f077392f75048dcadfb7e0))
- Update example DAGs (#21372) to fix [CVE-2022-24288](https://nvd.nist.gov/vuln/detail/CVE-2022-24288) ([commit](https://github.com/astronomer/airflow/commit/4e1ab17316d2a1ad9e343a10220fcbb63b928747))
- Updated `expat` to `2.2.6-2+deb10u3` to fix [DSA-5073-1](https://security-tracker.debian.org/tracker/DSA-5073-1) and [DSA-5085-1](https://security-tracker.debian.org/tracker/DSA-5085-1) ([commit](https://github.com/astronomer/ap-airflow/commit/b875830c3ccb8ad0d232d99e962fecc7ea639bc9), [commit](https://github.com/astronomer/ap-airflow/commit/4ffca19f5428ed2911dd30f1ac10064b8a0bb7ea))

### Bugfixes

- Do not set `TaskInstance.max_tries` in `refresh_from_task` (#21018) ([commit](https://github.com/astronomer/airflow/commit/70d195a9ab184788a7df0dc466ee088c2daed7b5))


Astronomer Certified 2.1.4-4, 2022-01-19
----------------------------------------

### Security

- Fixes for [CVE-2021-45230](https://nvd.nist.gov/vuln/detail/CVE-2021-45230)
    - Require can_edit on DAG privileges to modify TaskInstances and DagRuns (#16634) ([commit](https://github.com/astronomer/airflow/commit/e9f0f90d1e85259fdfb6aa9e3023dd27daedd7eb))
    - Remove /dagrun/create and disable edit form generated by F.A.B (#17376) ([commit](https://github.com/astronomer/airflow/commit/fa28024bd38cad8d62476e19f595ad1faffa0b1e))
- Updated `Flask-AppBuilder` to `3.4.3` to fix [CVE-2021-41265](https://nvd.nist.gov/vuln/detail/CVE-2021-41265) ([commit](https://github.com/astronomer/ap-airflow/commit/b7ce051b726978691f6f37cb1f2f00a3c88da56f))
- Updated `numpy` to `1.21.5` to fix [CVE-2021-33430](https://nvd.nist.gov/vuln/detail/CVE-2021-33430) ([commit](https://github.com/astronomer/ap-airflow/commit/953ec71d9228f0c6558d4cd9aa74b8ddb5dfd141))

### Bugfixes

- Row lock TI query in SchedulerJob._process_executor_events (#18975) ([commit](https://github.com/astronomer/airflow/commit/d161134d540be46d6a641dd85df1a31a2cd80779))
- Fix labels used to find queued KubeExecutor pods (#19904) ([commit](https://github.com/astronomer/airflow/commit/9cea8217a940dea45d6d3255a1f4284e5efcf150))
- Update [Astronomer FAB Security Manager](https://github.com/astronomer/astronomer-fab-securitymanager) to version [1.8.1](https://github.com/astronomer/astronomer-fab-securitymanager/releases/tag/v1.8.1)

Astronomer Certified 2.1.4-3, 2021-11-05
----------------------------------------

### Bugfixes

- Only mark SchedulerJobs as failed, not any jobs (#19375) ([commit](https://github.com/astronomer/airflow/commit/207154417))

Astronomer Certified 2.1.4-2, 2021-09-24
--------------------------------------------

### Bug Fixes

- [astro] Fix istio sidecar shutdown on newer GKE ([commit](https://github.com/astronomer/airflow/commit/cbd50ef0a))

Astronomer Certified 2.1.4-1, 2021-09-19
----------------------------------------

User-facing CHANGELOG for AC 2.1.4+astro.1 from Airflow 2.1.4:

### Bugfixes

- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/01d3f16))
- [astro]Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/d4dfd21))
