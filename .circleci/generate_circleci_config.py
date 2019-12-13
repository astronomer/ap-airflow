#!/usr/bin/env python3
"""
This script is used to create the circle config file
so that we can stay DRY.
"""

import os
from jinja2 import Template

AIRFLOW_VERSIONS = ["1.10.5", "1.10.6"]
DISTRIBUTIONS = ["alpine", "rhel7", "buster"]

def main():
    """ Render the Jinja2 template file
    """
    circle_directory = os.path.dirname(os.path.realpath(__file__))
    config_template_path = os.path.join(circle_directory, "config.yml.j2")
    config_path = os.path.join(circle_directory, "config.yml")

    with open(config_template_path, "r") as circle_ci_config_template:
        templated_file_content = circle_ci_config_template.read()
    template = Template(templated_file_content)
    config = template.render(
        airflow_versions=AIRFLOW_VERSIONS,
        distributions=DISTRIBUTIONS
    )
    warning_header = "# Warning: automatically generated file\n" + \
                     "# Please edit config.yml.j2, and use the script generate_circleci_config.py\n"
    with open(config_path, "w") as circle_ci_config_file:
        circle_ci_config_file.write(warning_header)
        circle_ci_config_file.write(config)

if __name__ == "__main__":
    main()
