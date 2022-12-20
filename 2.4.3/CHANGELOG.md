# Changelog

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
