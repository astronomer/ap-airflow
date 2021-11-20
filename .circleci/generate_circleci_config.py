#!/usr/bin/env python3
"""
This script is used to create the circle config file
so that we can stay DRY.
"""

from jinja2 import Environment, FileSystemLoader

from common import (
    circle_directory,
    DEV_ALLOWLIST,
    dev_releases,
    get_airflow_version,
    IMAGE_MAP,
    is_edge_build,
)


def generate_circleci_config():
    """
    Render the Jinja2 template file
    """

    template_env = Environment(loader=FileSystemLoader(searchpath=circle_directory), autoescape=True)
    template_env.filters['dev_releases'] = dev_releases
    template_env.filters['get_airflow_version'] = get_airflow_version
    template_env.filters['is_edge_build'] = is_edge_build
    template = template_env.get_template("config.yml.j2")

    config = template.render(
        image_map=IMAGE_MAP,
        dev_allowlist=DEV_ALLOWLIST,
    )
    print(config)


if __name__ == "__main__":
    generate_circleci_config()
