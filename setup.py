#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
from setuptools import setup, find_packages


def readme():
    with open('README.rst') as ff:
        return ff.read()


setup(
    name='pytest-astropy',
    version='0.4.0',
    license='BSD',
    description='Meta-package containing dependencies for testing',
    long_description=readme(),
    author='The Astropy Developers',
    author_email='astropy.team@gmail.com',
    url='https://astropy.org',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    keywords=[ 'pytest', 'py.test', 'remotedata', 'openfiles', 'doctestplus' ],
    python_requires='>=2.7',
    install_requires=[
        'pytest>=3.1.0',
        'pytest-doctestplus>=0.1.3',
        'pytest-remotedata>=0.3.0',
        'pytest-openfiles>=0.3.0',
        # Do not include as dependency until CI issues can be worked out
        #'pytest-mpl',
        'pytest-arraydiff>=0.1'
    ]
)
