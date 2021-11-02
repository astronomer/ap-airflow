# Changelog

Astronomer Certified 2.2.1-1, 2021-11-02
----------------------------------------

User-facing CHANGELOG for AC 2.2.1+astro.1 from Airflow 2.2.1:

### Bugfixes

- Add `DagRun.logical_date` as a property (apache#19198) ([commit](https://github.com/astronomer/airflow/commit/77140e981405ab5d732f9b0b82f666d4c26e5886))
- Fix Unexpected commit error in `SchedulerJob` (apache#19213) ([commit](https://github.com/astronomer/airflow/commit/fdb0aefcffd0e2a966c33ee6641987aa8f8fa33b))
- Bugfix: Check next run exists before reading data interval (apache#19307) ([commit](https://github.com/astronomer/airflow/commit/0cca4bfb6922e54f940ae8e8fd415c9cf96e21ef))
- [astro] [AIRFLOW-5448] Handle istio-proxy for Kubernetes Pods ([commit](https://github.com/astronomer/airflow/commit/d56ba747a8b7263d0bfe83e3ac46b77a4ec0d113))
- [astro] Reconcile orphan holding table handling ([commit](https://github.com/astronomer/airflow/commit/98f53fa7ccf0c441b04e223d8ce6f4f365965eb9))
- [astro] Override UI with Astro theme, add AC version in footer ([commit](https://github.com/astronomer/airflow/commit/15c339b563e5d93e79c0bc4534c05e44aface42a))
