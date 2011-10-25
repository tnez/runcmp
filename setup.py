#!/usr/bin/python

from setuptools import setup, find_packages
#from runcmp import __version__

setup(
    name = "runcmp",
    version = "0.1.1",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    package_data = {
                    # any text files
                    '': ['*.txt'],
                    # any files in support_files
                    'runcmp': ['support_files/*'],
                    },
    entry_points = {
                    'console_scripts': ['runcmp = runcmp.runcmp.main',]
                    },
    # metadata for upload to PyPI
    author = "Travis Nesland",
    author_email = "nesland@musc.edu",
    description = """RunCMP is an additional front-end to the Connectome Mapper""" + \
    """designed to facilitate easy iteration through subject directories""",
    keywords = "connectome connectomemapper cmp script iteration",

    # could also include long_description, download_url, classifiers, etc.
)