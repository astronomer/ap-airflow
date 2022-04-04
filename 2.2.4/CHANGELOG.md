# Changelog

Astronomer Certified 2.2.4-4, 2022-04-04
----------------------------------------

### Security

- Updated `glibc` and `locales` to `2.31-13+deb11u3` to fix [CVE-2021-33574](https://nvd.nist.gov/vuln/detail/CVE-2021-33574), [CVE-2022-23218](https://nvd.nist.gov/vuln/detail/CVE-2022-23218), and [CVE-2022-23219](https://nvd.nist.gov/vuln/detail/CVE-2022-23219) ([commit](https://github.com/astronomer/ap-airflow/commit/8642c845c719b14faf89d1901fcade24250ff78e))
- Updated `mariadb-common` and `libmariadb3` to `2.31-13+deb11u3` to fix [CVE-2021-46667](https://nvd.nist.gov/vuln/detail/CVE-2021-46667), [CVE-2022-24048](https://nvd.nist.gov/vuln/detail/CVE-2022-24048), [CVE-2022-24050](https://nvd.nist.gov/vuln/detail/CVE-2022-24050), [CVE-2022-24051](https://nvd.nist.gov/vuln/detail/CVE-2022-24051), and [CVE-2022-24052](https://nvd.nist.gov/vuln/detail/CVE-2022-24052) ([commit](https://github.com/astronomer/ap-airflow/commit/8642c845c719b14faf89d1901fcade24250ff78e))

### Bug Fixes

- Do not log the hook connection details even at DEBUG level ([commit](https://github.com/astronomer/airflow/commit/969f2cd13b31143899c3be6b345f09c7945a4b8c))

Astronomer Certified 2.2.4-3, 2022-03-07
----------------------------------------

### Bug Fixes

- Add Istio patch ([commit](https://github.com/astronomer/ap-airflow/commit/fb837881dd3471609ac42e2d8114411c9400c4c1))

Astronomer Certified 2.2.4-2, 2022-02-25
----------------------------------------

### Security

- Updated `expat` to `2.2.10-2+deb11u2` to fix [DSA-5085-1](https://security-tracker.debian.org/tracker/DSA-5085-1) ([commit](https://github.com/astronomer/ap-airflow/commit/3d7c4127ee46b2e194e9cb8a116f237cf2147429))

### Bug Fixes

- Upgrade FAB Security Manager to `1.8.4` ([commit](https://github.com/astronomer/ap-airflow/commit/0bd531351cdc37dd0fbd6d76c3b680615b31241e))

Astronomer Certified 2.2.4-1, 2022-02-22
----------------------------------------

User-facing CHANGELOG for AC 2.2.4+astro.1 from Airflow 2.2.4:

### Bugfixes

- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/d4211a6132269943840fed2d438f5e2c1a0c03a2))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/20b0bad4595cf45d52dcad32621ccd93506e12c7))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/8a9563812e1e974d18d45745cc253c31b366af34))
