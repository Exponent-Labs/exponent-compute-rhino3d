#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='compute-rhino3d',
      version='0.0.1',
      description='Patched version',
      author='Mcneil',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='',
    )