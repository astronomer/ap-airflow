#!/usr/bin/env python3
"""
This script is used to update the VERSION in all Dockerfiles with the corresponding VERSION in IMAGE_MAP
"""

import os
import re

from common import DEV_ALLOWLIST, get_airflow_version, IMAGE_MAP, project_directory


def update_dockerfiles():
    """
    Replace the VERSION in all the Dockerfiles with the corresponding VERSION in IMAGE_MAP
    """
    for ac_version, distros in IMAGE_MAP.items():
        dev_version = False
        airflow_version = get_airflow_version(ac_version)
        arg_ac_version = ac_version
        if "dev" in ac_version:
            dev_version = True
            if airflow_version not in DEV_ALLOWLIST:
                arg_ac_version = ac_version.replace("dev", "*")

        for distro in distros:
            file_name = os.path.join(project_directory, airflow_version, distro, "Dockerfile")

            with open(file_name, 'r') as f:
                file_contents = f.read()

            # Replace AC Version
            new_text = re.sub(
                r'ARG VERSION=(.*)', f'ARG VERSION="{arg_ac_version}"', file_contents,
                flags=re.MULTILINE
            )

            # Replace Airflow Version
            new_text = re.sub(
                r'ARG AIRFLOW_VERSION=(.*)',
                f'ARG AIRFLOW_VERSION="{airflow_version}"',
                new_text,
                flags=re.MULTILINE
            )

            # Replace Moving Constraints Version to a tag for "non-dev" version (e.g constraints-2.1.0)
            # For Dev versions we use a moving constraints branch (e.g constraints-2-1)
            # We only do this for all buster images
            # If it is the first post-fix version in AC / Airflow series use constraints-branch, if not
            # use the constraints from Airflow Version tag.
            if dev_version and "-1.dev" in ac_version:
                branch = "-".join(airflow_version.split(".", 3)[0:2])
                constraints_url = (
                    f'https://raw.githubusercontent.com/apache/airflow/constraints-{branch}/'
                    'constraints-${PYTHON_MAJOR_MINOR_VERSION}.txt'
                )
            else:
                constraints_url = (
                    'https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/'
                    'constraints-${PYTHON_MAJOR_MINOR_VERSION}.txt'
                )
            if "alpine3.10" not in distros:
                new_text = re.sub(
                    r'https://raw.githubusercontent.com/apache/airflow/constraints-(.*)/constraints-(.*).txt',
                    constraints_url,
                    new_text,
                    flags=re.MULTILINE
                )

            with open(file_name, "w") as f:
                f.write(new_text)


if __name__ == "__main__":
    update_dockerfiles()
