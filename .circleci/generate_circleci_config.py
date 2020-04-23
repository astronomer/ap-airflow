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
    ("1.10.5-6", ["alpine3.10", "buster", "rhel7"]),
    ("1.10.6-2", ["alpine3.10", "buster"]),
    ("1.10.7-8", ["alpine3.10", "buster"]),
    ("1.10.10-1", ["alpine3.10", "buster"]),
])


def dev_releases(all_releases):
    """Find dev releases from a list of releases"""
    return [release for release in all_releases if "dev" in release]


def main():
    """
    Render the Jinja2 template file
    """

    replace_version_info()

    circle_directory = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(circle_directory, "config.yml")

    template_env = Environment(loader=FileSystemLoader(searchpath="./"), autoescape=True)
    template_env.filters['dev_releases'] = dev_releases
    template = template_env.get_template("config.yml.j2")

    config = template.render(
        image_map=IMAGE_MAP
    )
    warning_header = "# Warning: automatically generated file\n" + \
                     "# Please edit config.yml.j2, and use the script generate_circleci_config.py\n"
    with open(config_path, "w") as circle_ci_config_file:
        circle_ci_config_file.write(warning_header)
        circle_ci_config_file.write(config)


def replace_version_info():
    """
    Replace the VERSION in all the Dockerfiles with the corresponding VERSION in IMAGE_MAP
    """

    for ac_version, distros in IMAGE_MAP.items():
        airflow_version = ac_version.split('-')[0]
        for distro in distros:
            file_name = os.path.join("..", airflow_version, distro, "Dockerfile")

            if "dev" in ac_version:
                ac_version = ac_version.replace("dev", "*")

            with open(file_name) as f:
                file_contents = f.read()

                new_text = re.sub(
                    r'ARG VERSION=(.*)', f'ARG VERSION="{ac_version}"', file_contents,
                    flags=re.MULTILINE
                )

            with open(file_name, "w") as f:
                f.write(new_text)


if __name__ == "__main__":
    main()
