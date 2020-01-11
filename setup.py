#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-testconfig',
    version='0.2.0',
    author='Wojciech Olejarz, Bartlomiej Skrobek',
    author_email='olejarz.wojciech@gmail.com',
    maintainer='Wojciech Olejarz, Bartlomiej Skrobek',
    maintainer_email='olejarz.wojciech@gmail.com',
    license='Apache Software License 2.0',
    url='https://github.com/wojole/pytest-testconfig',
    description='Test configuration plugin for pytest.',
    long_description=read('README.rst'),
    py_modules=['pytest_testconfig'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=['pytest>=3.5.0', 'pyyaml'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'testconfig = pytest_testconfig',
        ],
    },
)
