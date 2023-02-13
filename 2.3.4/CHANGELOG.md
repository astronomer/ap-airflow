# Changelog

Astronomer Certified 2.3.4-10, TBD
----------------------------------

### Bugfixes

- Use time not tries for queued & running re-checks ([#28586](https://github.com/apache/airflow/pull/28586))

### Security

- Update `apache-airflow-providers-mysql` to `4.0.0` and `apache-airflow-providers-common-sql` to `1.3.3` to fix [CVE-2023-22884](https://avd.aquasec.com/nvd/2022/cve-2023-22884/). This update includes a breaking change for the MySQL provider, see the [4.0.0 MySQL provider changelog](https://airflow.apache.org/docs/apache-airflow-providers-mysql/4.0.0/index.html#changelog) for details.
- Update `curl` to `7.74.0-1.3+deb11u5` to fix [CVE-2022-32221](https://avd.aquasec.com/nvd/cve-2022-32221)
- Update `openssl` to `1.1.1n-0+deb11u4` to fix [CVE-2023-0286](https://avd.aquasec.com/nvd/cve-2023-0286)

Astronomer Certified 2.3.4-9, 2023-01-26
----------------------------------------

### Bugfixes

- Annotate KubernetesExecutor pods that we don't delete ([#28844](https://github.com/apache/airflow/pull/28844))

Astronomer Certified 2.3.4-8, 2023-01-26
----------------------------------------

### Bugfixes

- Fix bad pods pickled in executor_config ([#28454](https://github.com/apache/airflow/pull/28454))
- Be more selective when adopting pods with KubernetesExecutor ([#28899](https://github.com/apache/airflow/pull/28899))
- Only patch single label when adopting pod ([#28776](https://github.com/apache/airflow/pull/28776))
- Don't re-patch pods that are already controlled by current worker ([#26778](https://github.com/apache/airflow/pull/26778))
- Fix  backfill  queued  task getting reset to scheduled state ([#23720](https://github.com/apache/airflow/pull/23720))
- Update `pip` to `22.3.1`
- Update `wheel` to `0.38.4`

### Security

- Update `setuptools` to `66.1.1` to fix [CVE-2022-40897](https://avd.aquasec.com/nvd/cve-2022-40897)
- Update `future` to `0.18.3` to fix [CVE-2022-40899](https://avd.aquasec.com/nvd/cve-2022-40899)

Astronomer Certified 2.3.4-7, 2022-12-21
----------------------------------------

### Bugfixes

- Fix deadlock when chaining multiple empty mapped tasks ([#27964](https://github.com/apache/airflow/pull/27964))

### Security

- Change the template to use human readable task_instance description ([#25960](https://github.com/apache/airflow/pull/25960))
- Update `certifi` to `2022.12.7` to fix [CVE-2022-23491](https://avd.aquasec.com/nvd/2022/cve-2022-23491/)
- Update `libtasn1` to `4.16.0-2+deb11u1` to fix [CVE-2021-46848](https://avd.aquasec.com/nvd/2022/cve-2021-46848/)
- Update `mariadb` to `1:10.5.18-0+deb11u1` to fix [a bunch of CVEs](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1024054#37)

Astronomer Certified 2.3.4-6, 2022-11-09
----------------------------------------

### Bugfixes

- Make tracebacks opt-in ([#27059](https://github.com/apache/airflow/pull/27059))
- Avoid 500 on dag redirect ([#27064](https://github.com/apache/airflow/pull/27064))

### Security

- Don't overwrite connection extra with invalid json ([#27142](https://github.com/apache/airflow/pull/27142))
- Simplify origin string cleaning ([#27143](https://github.com/apache/airflow/pull/27143))
- Update `libexpat1` to `2.2.10-2+deb11u5` to fix [CVE-2022-43680](https://avd.aquasec.com/nvd/2022/cve-2022-43680/)

Astronomer Certified 2.3.4-5, 2022-10-28
----------------------------------------

### Bugfixes

- Fix backporting issue with faulty executor config serialization logic
- Fix warning when using xcomarg dependencies ([#26801](https://github.com/apache/airflow/pull/26801))

Astronomer Certified 2.3.4-4, 2022-10-17
----------------------------------------

### Bugfixes

- Revert "Cache the custom secrets backend so the same instance gets re-used" ([#25556](https://github.com/apache/airflow/pull/25556))

Astronomer Certified 2.3.4-3, 2022-10-06
----------------------------------------

### Bugfixes

- Remove TaskFail duplicates check (#26714) ([commit](https://github.com/astronomer/airflow/commit/b94db52c3497e04747e63fce85dc08dd7f4657fc))
- Fix faulty executor config serialization logic (#26191) ([commit](https://github.com/astronomer/airflow/commit/6831e7824e11c43061d200f55f2e013382d61f46))

### Security

- Updated `expat` to `2.2.10-2+deb11u` to fix [CVE-2022-40674](https://avd.aquasec.com/nvd/cve-2022-40674)

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
