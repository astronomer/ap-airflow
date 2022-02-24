# Changelog

Astronomer Certified 1.10.15-5, 2022-02-24
--------------------------------------------

### Security

- Update example DAGs (#21372) to fix [CVE-2022-24288](https://nvd.nist.gov/vuln/detail/CVE-2022-24288) ([commit](https://github.com/astronomer/airflow/commit/982d1c70f1c4d15fc22b7504e802068a1bfd9920))
- Simplify trigger cancel button (#21591) to fix [CVE-2021-45229](https://nvd.nist.gov/vuln/detail/CVE-2021-45229) ([commit](https://github.com/astronomer/airflow/commit/0f94604932cb69a0dbf0edf86f34e860ac2cf035))
- Updated `protobuf` to `3.15.0` to fix [CVE-2021-22570](https://nvd.nist.gov/vuln/detail/CVE-2021-22570) ([commit](https://github.com/astronomer/ap-airflow/commit/50ce8cee18a2660b13542e53471f6b28474645b3))
- Updated `expat` to `2.2.6-2+deb10u3` to fix [DSA-5073-1](https://security-tracker.debian.org/tracker/DSA-5073-1) and [DSA-5085-1](https://security-tracker.debian.org/tracker/DSA-5085-1) ([commit](https://github.com/astronomer/ap-airflow/commit/b875830c3ccb8ad0d232d99e962fecc7ea639bc9), [commit](https://github.com/astronomer/ap-airflow/commit/4ffca19f5428ed2911dd30f1ac10064b8a0bb7ea))

Astronomer Certified 1.10.15-4, 2021-09-24
--------------------------------------------

### Bug Fixes

- [astro] Fix istio sidecar shutdown on newer GKE ([commit](https://github.com/astronomer/airflow/commit/14a4417c1))

Astronomer Certified 1.10.15-3, 2021-07-14
------------------------------------------

## Bug Fixes

- Exclude ``yarn.lock`` from built Python wheel file (#16577) ([commit](https://github.com/astronomer/airflow/commit/6c80e3ff5))
- [backport] Fix bug with `executor_config` and Volumes ([commit](https://github.com/astronomer/airflow/commit/7813076ac))
- Only allow webserver to request from the worker log server (#16754) ([commit](https://github.com/astronomer/airflow/commit/b8db31c19))
- Dockerfile: Add constraint for installed Airflow version (#274) ([commit](https://github.com/astronomer/ap-airflow/commit/60174ec))
- Dockerfile: Upgrade Fab Security Manager to 1.6.0 (#272) ([commit](https://github.com/astronomer/ap-airflow/commit/417fd59))

Astronomer Certified 1.10.15-2, 2021-06-04
------------------------------------------

## Bug Fixes

- KubernetesPodOperator should retry log tailing in case of interruption (#11325) ([commit](https://github.com/astronomer/airflow/commit/8848651ba))
- Correctly parse (and copy) extras with python version to metadist ([commit](https://github.com/astronomer/airflow/commit/176a2a3ec))
- Respect LogFormat when using ES logging with Json Format (#13310) ([commit](https://github.com/astronomer/airflow/commit/0dbd0f3a3))
- Bump JS dependencies & remove unwanted deps ([commit](https://github.com/astronomer/airflow/commit/65a07cf73))

Astronomer Certified 1.10.15-1, 2021-03-19
------------------------------------------

User-facing CHANGELOG for AC `1.10.15+astro.1` from Airflow `1.10.15`:

## Bug Fixes

- Fix `sync-perm` to work correctly when update_fab_perms = False ([commit](https://github.com/astronomer/airflow/commit/950028f93e1220d49629aea10dfbaf1173b8910b))
- Pin SQLAlchemy to <1.4 due to breakage of sqlalchemy-utils ([commit](https://github.com/astronomer/airflow/commit/331f0d23260a77212e7b15707e04bee02bdab1f2))

## Improvements

- Enable DAG Serialization by default ([commit](https://github.com/apache/airflow/commit/cd1961873783389ee51748f7f2a481900cce85b9))
- Stop showing Import Errors for Plugins in Webserver ([commit](https://github.com/apache/airflow/commit/a386fd542fe1c46bd3e345371eed10a9c230f690))
- Add role-based authentication backend ([commit](https://github.com/apache/airflow/commit/16461c3c8dcb1d1d2766844d32f3cdec31c89e69))

## New Features
- Show "Warning" to Users with Duplicate Connections ([commit](https://github.com/apache/airflow/commit/c037d48c9e383a6fd0b1b0d88407489d0ed02194))
