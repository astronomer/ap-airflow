#!/usr/bin/env python3
"""
Verify that CHANGELOG.md file has been created for each Airflow version. Also adds
links for all these CHANGELOG.md files in README.md
"""

import os
import re

from common import get_airflow_version, IMAGE_MAP, project_directory, is_edge_build


def verify_changelog_entries():
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
        if is_edge_build(ac_version):
            # We don't have a Changelog for edge builds
            continue
        airflow_version = get_airflow_version(ac_version)

        if "dev" not in ac_version:
            # Check that Changelog entry for this Airflow Version has been created
            changelog_path = os.path.join(project_directory, airflow_version, "CHANGELOG.md")
            assert os.path.exists(changelog_path), f"Please add the CHANGELOG.md file for {ac_version}"

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
    verify_changelog_entries()
