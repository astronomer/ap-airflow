# Changelog

Astronomer Certified 1.10.6-3, 2020-04-27
--------------------------------------------

No changes in `astronomer/airflow` repo.

Dockerfile changes are:

- Upgrade sqlite3 packages for Alpine 3.10 [CVE-2020-1967](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2020-1967) ([commit](https://github.com/astronomer/ap-airflow/commit/2f29d493259cddd487bcc306b829a4ec4a74f35e))
- Upgrade OpenSSL to mitigate [CVE-2019-16168](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-16168) ([commit](https://github.com/astronomer/ap-airflow/commit/6de11c2c87e78b7a3171d8fb222c7278fcb673c9))
- Constraint version of WTForms to non-broken version ([commit](https://github.com/astronomer/ap-airflow/commit/3cd34236f8a7214434dc313af525160133520bcb))
- JPype1 0.7.3 no longer installs on Alpline/musl-libc ([commit](https://github.com/astronomer/ap-airflow/commit/44164ba40cd1878cabeec5edc32fe0a7bb7a8e0d))
