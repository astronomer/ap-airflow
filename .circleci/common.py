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
        if "dev" in release and get_airflow_version(release) not in DEV_ALLOWLIST
    ]


def get_airflow_version(ac_version):
    """Get Airflow Version from the string containing AC Version"""
    return ac_version.split('-')[0]


IMAGE_MAP = collections.OrderedDict([
    ("1.10.10-10", ["alpine3.10", "buster"]),
    ("1.10.12-6", ["alpine3.10", "buster"]),
    ("1.10.14-5", ["buster"]),
    ("1.10.15-4", ["buster"]),
    ("2.0.0-10", ["buster"]),
    ("2.0.2-6", ["buster"]),
    ("2.1.0-5", ["buster"]),
    ("2.1.1-4", ["buster"]),
    ("2.1.3-2", ["buster"]),
    ("2.1.4-2", ["buster"]),
    ("2.2.0-4.dev", ["bullseye", "buster"]),
    ("2.2.1-2.dev", ["bullseye", "buster"]),
])

# Airflow Versions for which we don't publish Python Wheels
DEV_ALLOWLIST = []
