#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-resource',
    version='0.1.0',
    author='Kazuki Iwata',
    author_email='kazu.0516.k0n0f@gmail.com',
    maintainer='Kazuki Iwata',
    maintainer_email='kazu.0516.k0n0f@gmail.com',
    license='MIT',
    url='https://github.com/kzmake/pytest-resource',
    description='Load resource fixture plugin to use with pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_resource'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['pytest>=3.5.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'resource = pytest_resource',
        ],
    },
)
