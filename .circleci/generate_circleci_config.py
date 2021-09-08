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
    ("1.10.7-19", ["alpine3.10", "buster"]),
    ("1.10.10-9", ["alpine3.10", "buster"]),
    ("1.10.12-5", ["alpine3.10", "buster"]),
    ("1.10.14-4", ["buster"]),
    ("1.10.15-3", ["buster"]),
    ("2.0.0-9", ["buster"]),
    ("2.0.2-5.dev", ["buster"]),
    ("2.1.0-4.dev", ["buster"]),
    ("2.1.1-3.dev", ["buster"]),
    ("2.1.3-1", ["buster"]),
    ("2.2.0-1.dev", ["buster"]),
])

# Airflow Versions for which we don't publish Python Wheels
DEV_ALLOWLIST = []


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
    verify_changelog_entry()

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
        dev_version = False
        airflow_version = get_airflow_version(ac_version)
        ac_version_raw = ac_version
        for distro in distros:
            file_name = os.path.join(project_directory, airflow_version, distro, "Dockerfile")

            if "dev" in ac_version:
                dev_version = True
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
                if dev_version and "-1.dev" in ac_version_raw:
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


def verify_changelog_entry():
    """
    Verify that CHANGELOG.md file has been created for each Airflow version. Also adds
    links for all these CHANGELOG.md files in README.md
    """
    readme_changelog_links = (
        "## Changelog\n\n"
        "All changes applied to available point releases will be documented "
        "in the `CHANGELOG.md` files within each version folder:\n"
    )

    for ac_version, distros in IMAGE_MAP.items():
        airflow_version = get_airflow_version(ac_version)

        if "dev" not in ac_version:
            # Check that Changelog entry for this Airflow Version has been created
            changelog_path = os.path.join(project_directory, airflow_version, "CHANGELOG.md")
            assert os.path.exists(changelog_path), f"Please add the Changelog.md file for {ac_version}"

            with open(changelog_path) as changelog_file:
                changelog_contents = changelog_file.read()

                # Replace AC Version
                assert f"Astronomer Certified {ac_version}" in changelog_contents, \
                    f"Please add Changelog entry for {ac_version} in {changelog_path}"

        # Changelog Readme URL to include
        readme_changelog_links += (
            f"- [{airflow_version} Changelog]"
            f"(https://github.com/astronomer/ap-airflow/blob/master/{airflow_version}/CHANGELOG.md)\n"
        )

    # Update the Changelog URLs in README.md
    with open(os.path.join(project_directory, "README.md"), "r") as readme_file:
        readme_contents = readme_file.read()
        new_readme_text = re.sub(
            r'<!-- CHANGELOG START -->([\s\S]*)<!-- CHANGELOG END -->',
            f'<!-- CHANGELOG START -->\n{readme_changelog_links}<!-- CHANGELOG END -->',
            readme_contents,
            flags=re.MULTILINE
        )

    with open(os.path.join(project_directory, "README.md"), "w") as readme_file:
        readme_file.write(new_readme_text)


if __name__ == "__main__":
    main()
