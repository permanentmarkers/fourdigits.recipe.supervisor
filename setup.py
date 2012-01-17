# -*- coding: utf-8 -*-
"""
This module contains the tool of fourdigits.recipe.supervisor
"""

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.18dev'

long_description = (
    read('docs', 'README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('docs', 'CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('fourdigits', 'recipe', 'supervisor', 'README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('docs', 'CONTRIBUTORS.txt')
    + '\n' +
    'Download\n'
    '********\n')

entry_point = 'fourdigits.recipe.supervisor:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require = ['zope.testing']

setup(name='fourdigits.recipe.supervisor',
      version=version,
      description="A buildout recipe to install supervisor",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Zope Public License',
        ],
      keywords='buildout recipe supervisor',
      author='Mustapha Benali',
      author_email='mustapha@headnet.dk',
      url='http://pypi.python.org/pypi/fourdigits.recipe.supervisor',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['fourdigits', 'fourdigits.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout',
                        'zc.recipe.egg',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'fourdigits.recipe.supervisor.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
