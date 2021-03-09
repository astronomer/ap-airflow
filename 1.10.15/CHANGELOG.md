# Changelog

Astronomer Certified 1.10.15-1.dev, 
-----------------------------------------------

### Bug Fixes

- Fix-duplicate-Code ([commit](https://github.com/apache/airflow/00fff8d90bf0e8142f2d0a3dd794bf58e6cc557a))
- BugFix-fix-the-delete_dag-function-of-json_client-14441 ([commit](https://github.com/apache/airflow/2ea5881e696ef7738d135067bf78e6012d4e4a99))
- Fixed-deprecation-message-for-variables-command-14457 ([commit](https://github.com/apache/airflow/75b2fa22b75b9879bafe607b15f900b46c4828bc))
- Add-airflow-variables-list-command-for-1.10.x-transition-version-14462 ([commit](https://github.com/apache/airflow/7a5f0e1cd1cb0651a8306580088626f4303f6ab9))
Fix-permission-error-on-non-POSIX-filesystem-13121-14383 ([commit](https://github.com/apache/airflow/e8008f5f67f448c280935320471606d6a6a84a73))
- Fix-airflow-tasks-clear-cli-command-wirh-yes-14188 ([commit](https://github.com/apache/airflow/3709503ecf180bd8c85190bcc7e5e755b60d9bfb))
- Ensure-all-statsd-timers-use-millisecond-values.-10633 ([commit](https://github.com/apache/airflow/48daabce99476c218b6d0d1a5ed5c6941074497c))
- StreamLogWriter-Provide-no-op-close-method-10885 ([commit](https://github.com/apache/airflow/07f6f30153a5c842e854043389e10faea290bd36))
- KubernetesExecutor-should-accept-images-from-executor_config-13074 ([commit](https://github.com/apache/airflow/ee88f5f46ef32d2eb5e9be56e723de58b6736375))
- Scheduler-should-acknowledge-active-runs-properly-13803 ([commit](https://github.com/apache/airflow/b4de6beb47d2de777e371bfb20321c3feedd6bbd))
- Moved-boto3-limitation-to-snowflake-13286 ([commit](https://github.com/apache/airflow/022f9e2234e22ea556013bc7b6e5cb15d41cbf11))
- Fix-airflow-db-upgrade-to-upgrade-db-as-intended-13267 ([commit](https://github.com/apache/airflow/a1f5b08dbd40d38fce066b13f8d6998bc4d185df))
- Fix-broken-airflow-upgrade_check-command-14137 ([commit](https://github.com/apache/airflow/e76c7433c9a32c752ab9ed94f0dfe5cec5031758))
- Include-airflow-contrib-executors-in-the-dist-package ([commit](https://github.com/apache/airflow/60ac8df046f34e23f9abba82516baf5d6314b880))