#!/usr/bin/env python3

"""
Download, and repackage Apache Airflow provider packages to change dependency
from apache-airflow to astronomer-certified instead.
"""

from argparse import ArgumentParser
import os
import shutil
import re
from glob import glob
from tempfile import TemporaryDirectory

from email.message import Message
from email.parser import Parser
from urllib.parse import urljoin
from wheel.wheelfile import WheelFile, WHEEL_INFO_RE
from wheel.cli.pack import pack as pack_wheel
from wheel.cli.unpack import unpack as unpack_wheel
from zipfile import ZIP_DEFLATED, ZipInfo, ZipFile

import requests
from bs4 import BeautifulSoup


def wheel_urls_from_listing(url):
    listing = requests.get(url)
    listing.raise_for_status()

    soup = BeautifulSoup(listing.text, 'html.parser')

    relative_wheels = [
        a['href'] for a in soup.find_all('a') if a['href'].endswith('.whl')
    ]

    for rel in relative_wheels:
        yield urljoin(listing.url, rel)


def download_wheel(url, destdir):
    local_filename = os.path.basename(url)
    path = os.path.join(destdir, local_filename)

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        r.raw.decode_content = True
        with open(path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return path

def repack_wheel(output: str, url: str):
    with TemporaryDirectory() as tmp:
        src_filename = download_wheel(url, tmp)

        match = WHEEL_INFO_RE.match(src_filename)
        namever = match.group('namever')
        ver = match.group('ver')
        destination = os.path.join(tmp, namever)

        # We can't use WheelFile to unpack it, as the filename doesn't match
        # always the contents (rc vs not)
        with ZipFile(src_filename) as wf:
            wf.extractall(destination)

        real_name = update_metadata(destination, '1!' + ver)

        os.unlink(src_filename)
        output = os.path.join(output, real_name)
        os.mkdir(output)
        pack_wheel(destination, output, None)


def update_metadata(unpacked_folder, ver: str):
    """
    Update the METADATA in the unpacked wheel folder, replacing requirements on
    ``apache-airflow`` with ``astronomer-certified``.

    If we are repackging the Apache Airflow RCs from dist.apache.org, the
    filename will contain rc1, but the version in the wheel will not match.
    This will update the version contained in the wheel to include the matching
    release candidate/pre-release version suffix
    """
    dist_info_path = glob(os.path.join(unpacked_folder, "*.dist-info"))[0]

    with open(os.path.join(dist_info_path, 'METADATA')) as fh:
        metadata = Parser().parse(fh, headersonly=True)

    metadata_ver = metadata['Version']

    new_metadata = Message()

    # The order matters, so we iterate over the old items, and set them on the
    # new metadata, after adjusting any Requires-Dist on apache-airflow
    for key, val in metadata.items():
        if key == 'Requires-Dist':
            val = re.sub(r'^apache-airflow(\s|$)', r'astronomer-certified\1', val)
        if key == 'Version':
            val = ver

        new_metadata[key] = val

    new_metadata.set_payload(metadata.get_payload())

    #import difflib, sys
    #sys.stdout.writelines(difflib.context_diff(metadata.as_string().splitlines(keepends=True), new_metadata.as_string().splitlines(keepends=True)))

    with open(os.path.join(dist_info_path, 'METADATA'), 'w') as fh:
        fh.write(new_metadata.as_string())

    if metadata_ver != ver:
        # Update the version in the .dist-info/ folder name, as this is what
        # `wheel pack` uses to create the filename
        folder = os.path.basename(dist_info_path)
        folder = folder.replace(metadata_ver, ver)
        os.rename(dist_info_path, os.path.join(unpacked_folder, folder))

    return metadata['Name']

#repack_wheel('https://dist.apache.org/repos/dist/dev/airflow/backport-providers/2020.6.24rc1/apache_airflow_backport_providers_amazon-2020.6.24rc1-py3-none-any.whl')

def main():
    parser = ArgumentParser()

    parser.add_argument(
        "--keep-rcs",
        action="store_true",
    )
    parser.add_argument(
        "--http_root",
        default="https://dist.apache.org/repos/dist/dev/airflow/backport-providers/",
        help="Root folder containing versioned release folders, for example "
             "https://dist.apache.org/repos/dist/dev/airflow/backport-providers/"
    )

    parser.add_argument(
        "--output",
        help="Folder underwhich to create output folders, suitable for uploading to a PEP-503 compatible repository",
        default="tmp-packages",
    )

    parser.add_argument(
        "version",
        help="Version to download and repackage",
    )

    args = parser.parse_args()

    os.mkdir(args.output)

    wheels = wheel_urls_from_listing(os.path.join(args.http_root, args.version))
    for wheel in wheels:
        repack_wheel(args.output, wheel)

if __name__ == "__main__":
    main()
