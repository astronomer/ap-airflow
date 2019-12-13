**What this PR does / why we need it**:

**Special notes for your reviewer**:

#### Checklist
[Place an '[x]' (no spaces) in all applicable fields. Please remove unrelated fields.]

- [ ] If a new distribution or Airflow verison is added, please add in .circleci/generate_circleci_config.py and run the script
- [ ] If a new distribution or Airflow verison is added, there is an 'onbuild' directory and Dockerfile in all base image directories
- [ ] If a new distribution is added, it is supported by all Airflow versions
- [ ] If a new Airflow version is added, it supports all distributions
- [ ] If changing an image, add applicable test in .circleci/test-airflow-image.py
