#!/usr/bin/env python
import os

from distutils.core import setup
from setuptools import find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('requirements.txt') as fh:
    install_requires = fh.read().splitlines()

with open('VERSION') as fh:
    version = fh.read().strip()

setup(
    name='freebie',
    version=version,
    description='A free database of news resources for information extraction',
    author='Aleksandar Savkov',
    packages=find_packages(exclude=('test',)),
    zip_safe=True,
    include_package_data=False,
    license='GPL3',
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Information Extraction Researchers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP'
    ],
    package_data={
        'freebie.news': ['rss_feeds.csv', 'websources.csv'],
        'freebie.twitter': ['twitter_handles.csv']
    },
)