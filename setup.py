from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-extendsearch',
    version=version,
    description="Extends Ckan dataset search",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Stuart Gough',
    author_email='stuart@xvt.com.au',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.extendsearch'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
	    [ckan.plugins]
  	    extendsearch=ckanext.extendsearch.plugin:ExtendSearchPlugin
	''',
)
