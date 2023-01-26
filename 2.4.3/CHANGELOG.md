# Changelog

Astronomer Certified 2.4.3-3, 2023-01-25
----------------------------------------
### Bugfixes

- Revert "Make DagRun state updates for paused DAGs faster ([#27725](https://github.com/apache/airflow/pull/27725))"
- Fix bad pods pickled in executor_config ([#28454](https://github.com/apache/airflow/pull/28454))
- Be more selective when adopting pods with KubernetesExecutor ([#28899](https://github.com/apache/airflow/pull/28899))
- Only patch single label when adopting pod ([#28776](https://github.com/apache/airflow/pull/28776))
- Update `pip` to `22.3.1`
- Update `wheel` to `0.38.4`
- Update `gcloud-aio-auth` to `4.1.5`

### Security

- Update `setuptools` to `66.1.1` to fix [CVE-2022-40897](https://avd.aquasec.com/nvd/cve-2022-40897)
- Update `future` to `0.18.3` to fix [CVE-2022-40899](https://avd.aquasec.com/nvd/cve-2022-40899)

Astronomer Certified 2.4.3-2, 2022-12-21
----------------------------------------

### Bugfixes

- Make DagRun state updates for paused DAGs faster ([#27725](https://github.com/apache/airflow/pull/27725))
- Fix deadlock when chaining multiple empty mapped tasks ([#27964](https://github.com/apache/airflow/pull/27964))

### Security

- Update `certifi` to `2022.12.7` to fix [CVE-2022-23491](https://avd.aquasec.com/nvd/2022/cve-2022-23491/)
- Update `libtasn1` to `4.16.0-2+deb11u1` to fix [CVE-2021-46848](https://avd.aquasec.com/nvd/2022/cve-2021-46848/)
- Update `mariadb` to `1:10.5.18-0+deb11u1` to fix [a bunch of CVEs](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1024054#37)

Astronomer Certified 2.4.3-1, 2022-11-14
----------------------------------------

User-facing CHANGELOG for AC 2.4.3+astro.1 from Airflow 2.4.3.

### Bugfixes

- Upgrade to Airflow 2.4.3
