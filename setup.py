#! /usr/bin/env python
import os, sys

from setuptools import setup, find_packages

# from Cython.Build import cythonize
from distutils.extension import Extension
import versioneer

try:
    import model_metadata
except ImportError:
    def get_cmdclass(*args, **kwds):
        return kwds.get("cmdclass", None)
    def get_entry_points(*args):
        return None
else:
    from model_metadata.utils import get_cmdclass, get_entry_points




packages = find_packages(include=["pymt_frost_number_geo"])
pymt_components = [
    (
        "FrostnumberGeoMethod=permamodel.components.frost_number_Geo:FrostnumberGeoMethod",
        "meta",
    )
]

setup(
    name="pymt_frost_number_geo",
    author="Eric Hutton",
    description="PyMT plugin frost_number_geo",
    version=versioneer.get_version(),

    packages=packages,
    cmdclass=get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass()),
    entry_points=get_entry_points(pymt_components),
)
