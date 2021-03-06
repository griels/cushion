#!/usr/bin/env python
"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from distutils.core import setup

setup(
    name='cushion',
    version='1.0.0',
    description='Simple Couchbase object wrapper',
    author='Jeremy Kelley',
    author_email='jeremy@33ad.org',
    url="http://github.com/leveler/cushion/",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    install_requires=['iso8601', 'couchbase==2.0.2']
)
