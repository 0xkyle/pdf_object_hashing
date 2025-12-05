#!/usr/bin/env python3
"""
setup script for pdf object hashing
"""

from setuptools import setup, find_packages

setup(
    name="pdf-object-hashing",
    version="0.2.0",
    description="PDF analysis library for generating structural hashes of PDF objects.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Kyle Eaton",
    license="Apache 2.0",
    python_requires=">=3.7",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pdf-obj-hash=pdf_object_hashing.pdf_obj_hash:main",
        ],
    },
    url="https://github.com/0xkyle/pdf_object_hashing",
    project_urls={
        "Homepage": "https://www.proofpoint.com/us/blog/threat-insight/proofpoint-releases-innovative-detections-threat-hunting-pdf-object-hashing",
        "Repository": "https://github.com/0xkyle/pdf_object_hashing",
        "Upstream Repository": "https://github.com/EmergingThreats/pdf_object_hashing",
    },
)
