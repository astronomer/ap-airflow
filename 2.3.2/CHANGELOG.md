# Changelog

Astronomer Certified 2.3.2-2, 2022-06-22
----------------------------------------

User-facing CHANGELOG for AC 2.3.2+astro.2 from Airflow 2.3.2:

### Bugfixes

- Fix log_template seeding ([commit](https://github.com/astronomer/airflow/commit/a65ad2b4831bc2b0f68bf61579d959579dab14cb))
- Apply per-run log templates to log handlers ([commit](https://github.com/astronomer/airflow/commit/6d6c5aae74f277683271ae5f020cf7f3b3442fff))
- Don't crash scheduler if exec config has old k8s objects ([commit](https://github.com/astronomer/airflow/commit/d7d6f99aa94eadc7a9d2a74162c9e3619f1b46ad))
- Check for run_id for grid group summaries ([commit](https://github.com/astronomer/airflow/commit/3450105a8e02bfa13ec0d43d06e66798cf177ea5))

Astronomer Certified 2.3.2-1, 2022-06-04
----------------------------------------

User-facing CHANGELOG for AC 2.3.2+astro.1 from Airflow 2.3.2:

### Bugfixes

- [astro] seed log_template table (#1497) ([commit](https://github.com/astronomer/airflow/commit/dfec7125e49b055c6c8d4804e1c38c2037fb2208))
- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/26aa422df25efd7252e4c4f38c5d2a4202a1202d))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/7f7e45434b28d3b97a6f76d273db715f51f9618f))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/ba0e71fc5a56f1a7767f0ce697d569dd3570e120))
