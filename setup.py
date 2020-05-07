# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="pythonsample",
    version="0.1.1",
    description="A pip package",
    license="MIT",
    author="aimi,iwase",
    packages=find_packages(),
    install_requires=["requests"],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
