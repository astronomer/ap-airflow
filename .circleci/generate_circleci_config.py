#!/usr/bin/env python3
"""
This script is used to create the circle config file
so that we can stay DRY.
"""

import collections
import os
from jinja2 import Environment, FileSystemLoader

IMAGE_MAP = collections.OrderedDict([
    ("1.10.5", ["alpine3.10", "buster", "rhel7"]),
    ("1.10.6", ["alpine3.10", "buster"]),
    ("1.10.7", ["alpine3.10", "buster"]),
    ("1.10.10.dev", ["alpine3.10", "buster"]),
])


def dev_releases(all_releases):
    """Find dev releases from a list of releases"""
    return [release for release in all_releases if "dev" in release]


def main():
    """ Render the Jinja2 template file
    """
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


if __name__ == "__main__":
    main()
