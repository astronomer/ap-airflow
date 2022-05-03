# Changelog

Astronomer Certified 2.3.0-3, 2022-05-03
----------------------------------------

### Bug Fixes

- Optimize 2.3.0 pre-upgrade check queries ([commit](https://github.com/astronomer/airflow/commit/3b014735a6d67ed0f324628361d39869503d13dd))
- Add logs after successful connection to DB in the entrypoint ([commit](https://github.com/astronomer/ap-airflow/commit/c8753d2e4643868a0fe6199cdab8e8d0fd3f79c7))

Astronomer Certified 2.3.0-2, 2022-05-02
----------------------------------------

### Bug Fixes

- Upgrade FAB Security Manager to `1.9.2` ([commit](https://github.com/astronomer/ap-airflow/commit/9e4f204961258e773e835414b9fefc73d0c3de60))

Astronomer Certified 2.3.0-1, 2022-04-30
----------------------------------------

User-facing CHANGELOG for AC 2.3.0+astro.1 from Airflow 2.3.0:

### Bugfixes
- Don't show grid actions if server would reject with permission denied ([commit](https://github.com/astronomer/airflow/commit/62ebd1ebab6fb65353d90fadc5dc4553555bb6f1))
- Use run_id for ti.mark_success_url ([commit](https://github.com/astronomer/airflow/commit/405e57ce5a52474a26c5c18a2e724b070230cfa6))
- Fix broken task instance link in xcom list ([commit](https://github.com/astronomer/airflow/commit/72c6c438d3d8b74671fd2dd1a91b298cff4dd0ba))
- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/b595c1e84ef77d296cb006fbc4841646b6890db4))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods (#62) ([commit](https://github.com/astronomer/airflow/commit/be1ede151e1e28b66585d00490a26dccad08a240))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/300ed94ed8a0cb6118525ac81fc05c2190437820))
