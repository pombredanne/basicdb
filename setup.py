#!/usr/bin/env python
# Copyright (c) 2013 Soren Hansen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name='basicdb',
    version='0.1',
    description='Basic database service',
    long_description=open('README.rst', 'r').read(),
    author='Soren Hansen',
    author_email='soren@linux2go.dk',
    url='http://github.com/sorenh/basicdb',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    keywords='basicdb simpledb',
    install_requires=[
        'falcon',
    ],
    test_requires=[
        'boto',
    ],
    test_suite='nose.collector')