# Changelog

Astronomer Certified 2.2.5-3, 2022-06-22
----------------------------------------

### Security

- Updated `libssl1.1` and `openssl` to `1.1.1n-0+deb10u2` to fix [CVE-2022-1292](https://avd.aquasec.com/nvd/cve-2022-1292)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `libpq5` to `11.16-0+deb10u1` to fix [CVE-2022-1552](https://avd.aquasec.com/nvd/cve-2022-1552)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `liblzma5` to `5.2.4-1+deb10u1` to fix [CVE-2022-1271](https://avd.aquasec.com/nvd/cve-2022-1271)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `libldap-2.4-2` and `libldap-common` to `2.4.47+dfsg-3+deb10u7` to fix [CVE-2022-29155](https://avd.aquasec.com/nvd/cve-2022-29155)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `gzip` to `1.9-3+deb10u1` to fix [CVE-2022-1271](https://avd.aquasec.com/nvd/cve-2022-1271)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))
- Updated `dpkg` to `1.19.8` to fix [CVE-2022-1664](https://avd.aquasec.com/nvd/cve-2022-1664)([commit](https://github.com/astronomer/ap-airflow/commit/7e637f4f8ecf8a4c29ad108ef185fe16cb2c4d06))

### Bugfixes

- Fix `email_on_failure` with `render_template_as_native_obj` ([commit](https://github.com/astronomer/airflow/commit/06d8dfb7acebd8eb44362e3b3e66dc7d1ff3a31e))

Astronomer Certified 2.2.5-2, 2022-04-06
----------------------------------------

### Bugfixes

- Pin `apache-airflow-providers-elasticsearch` to `1!2.2.0`

Astronomer Certified 2.2.5-1, 2022-04-04
----------------------------------------

User-facing CHANGELOG for AC 2.2.5+astro.1 from Airflow 2.2.5:

### Bugfixes

- Remove logging of hook connection details ([commit](https://github.com/astronomer/airflow/commit/1b1d0a63ee4669bde0458a65999efe6077cced2e))
- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/ff7eb71fe8aacf8b9665b0e46d0c508f7475787f))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/1c6e3d4e6f1dd98264c0ca8375b0685ea8c5ced1))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/d29644bfb135ce1a8ce128894fb8fd9ec27b92ab))
