#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- encoding: utf-8 -*-

from setuptools import setup


def readme():
    with open('README.rst') as ff:
        return ff.read()


setup(
    name='pytest-astropy',
    version='0.7.0',
    license='BSD',
    description='Meta-package containing dependencies for testing',
    long_description=readme(),
    author='The Astropy Developers',
    author_email='astropy.team@gmail.com',
    url='https://astropy.org',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Framework :: Pytest',
        'Framework :: Hypothesis',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    keywords=['pytest', 'py.test', 'remotedata', 'openfiles', 'doctestplus'],
    python_requires='>=3.6',
    install_requires=[
        'pytest>=4.6',
        'pytest-doctestplus>=0.2.0',
        'pytest-remotedata>=0.3.1',
        'pytest-openfiles>=0.3.1',
        'pytest-astropy-header',
        # Do not include as dependency until CI issues can be worked out
        # 'pytest-mpl',
        'pytest-arraydiff>=0.1',
        # Bump hypothesis to >=5.0 in early Jan 2020
        'hypothesis>=4.53'
    ]
)
