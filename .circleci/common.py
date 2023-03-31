"""
Common utility functions for CircleCI configurator scripts
"""

import collections
import os


circle_directory = os.path.dirname(os.path.realpath(__file__))
project_directory = os.path.join(circle_directory, "..")


def dev_releases(all_releases):
    """Find dev releases from a list of releases"""
    return [
        release for release in all_releases
        if is_dev_release(release)
    ]


def is_dev_release(version):
    return "dev" in version or is_edge_build(version)


def is_edge_build(version):
    return "main" in version


def get_airflow_version(ac_version):
    """Get Airflow Version from the string containing AC Version"""
    if is_edge_build(ac_version):
        return "main"
    return ac_version.split('-')[0]


IMAGE_MAP = collections.OrderedDict([
    ("2.3.4-11", ["bullseye"]),
    ("2.4.3-6", ["bullseye"]),
])
