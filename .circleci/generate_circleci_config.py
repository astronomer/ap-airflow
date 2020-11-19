#!/usr/bin/env python3
"""
This script is used to create the circle config file
so that we can stay DRY.
"""

import collections
import os
import re

from jinja2 import Environment, FileSystemLoader

IMAGE_MAP = collections.OrderedDict([
    ("1.10.5-11", ["alpine3.10", "buster", "rhel7"]),
    ("1.10.7-16.dev", ["alpine3.10", "buster"]),
    ("1.10.10-6.dev", ["alpine3.10", "buster"]),
    ("1.10.12-2.dev", ["alpine3.10", "buster"]),
    ("1.10.13-1.dev", ["buster"]),
    ("2.0.0-1.dev", ["buster"]),
])

# Airflow Versions for which we don't publish Python Wheels
DEV_ALLOWLIST = ["1.10.5"]


def dev_releases(all_releases):
    """Find dev releases from a list of releases"""
    return [
        release for release in all_releases
        if "dev" in release and get_airflow_version(release) not in DEV_ALLOWLIST
    ]


def get_airflow_version(ac_version):
    """Get Airflow Version from the string containing AC Version"""
    return ac_version.split('-')[0]


circle_directory = os.path.dirname(os.path.realpath(__file__))
project_directory = os.path.join(circle_directory, "..")


def main():
    """
    Render the Jinja2 template file
    """

    replace_version_info()

    config_path = os.path.join(circle_directory, "config.yml")

    template_env = Environment(loader=FileSystemLoader(searchpath=circle_directory), autoescape=True)
    template_env.filters['dev_releases'] = dev_releases
    template_env.filters['get_airflow_version'] = get_airflow_version
    template = template_env.get_template("config.yml.j2")

    config = template.render(
        image_map=IMAGE_MAP,
        dev_allowlist=DEV_ALLOWLIST,
    )
    warning_header = "# Warning: automatically generated file\n" + \
                     "# Please edit config.yml.j2, and use the script generate_circleci_config.py\n"
    with open(config_path, "w") as circle_ci_config_file:
        circle_ci_config_file.write(warning_header)
        circle_ci_config_file.write(config)
        circle_ci_config_file.write("\n")


def replace_version_info():
    """
    Replace the VERSION in all the Dockerfiles with the corresponding VERSION in IMAGE_MAP
    """
    for ac_version, distros in IMAGE_MAP.items():
        airflow_version = get_airflow_version(ac_version)
        for distro in distros:
            file_name = os.path.join(project_directory, airflow_version, distro, "Dockerfile")

            if "dev" in ac_version:
                if airflow_version not in DEV_ALLOWLIST:
                    ac_version = ac_version.replace("dev", "*")

            with open(file_name) as f:
                file_contents = f.read()

                # Replace AC Version
                new_text = re.sub(
                    r'ARG VERSION=(.*)', f'ARG VERSION="{ac_version}"', file_contents,
                    flags=re.MULTILINE
                )

                # Replace Airflow Version
                new_text = re.sub(
                    r'LABEL io.astronomer.docker.airflow.version=(.*)',
                    f'LABEL io.astronomer.docker.airflow.version="{airflow_version}"',
                    new_text,
                    flags=re.MULTILINE
                )

            with open(file_name, "w") as f:
                f.write(new_text)


if __name__ == "__main__":
    main()
