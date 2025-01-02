#!/usr/bin/env python
##from distutils.core import setup, Extension
from setuptools import setup, find_packages

import numpy

setup(name= "pyFWI",
      version = "1.0",
      author = "Reid  Sawtell",
      author_email="rwsawtel@mtu.edu",
      url="http://code.google.com/p/pyfwi/",
      description="Functions for computing FWI parameters and DMC % moisture",
      packages = find_packages(),
      package_dir = {"pyFWI": "pyFWI"},
      scripts = ["scripts/FWI.py"]
      )
