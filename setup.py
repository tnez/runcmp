#!/usr/bin/python

from glob import glob
import os
import sys
if os.path.exists('MANIFEST'): os.remove('MANIFEST')

#from runcmp import __version__

packages=["runcmp",
#          "runcmp.info",
          "runcmp.subjects"]

package_data={'runcmp':
              ['support_files/*']
              }
################################################################################
if len(set(('develop', 'bdist_egg', 'bdist_rpm', 'bdist', 'bdist_dumb', 
            'bdist_wininst', 'install_egg_info', 'egg_info', 'easy_install',
            )).intersection(sys.argv)) > 0:
    from setup_egg import extra_setuptools_args

# extra_setuptools_args can be defined from the line above, but it can
# also be defined here because setup.py has been exec'ed from
# setup_egg.py.
if not 'extra_setuptools_args' in globals():
    extra_setuptools_args = dict()

def main(**extra_args):
    from distutils.core import setup
    from runcmp.info import __version__

    setup(
        name = "runcmp",
        version = __version__,
        description="""A python wrapper to drive the Connectome Mapper in a gui-less manner"""
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
