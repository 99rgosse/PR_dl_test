#!/usr/env/bin python

from setuptools import setup

setup(
    name='pygitea',
    version='0.0.1',
    description='Gitea API wrapper for python',
    url='http://github.com/jo-nas/pygitea',
    author='Jonas',
    author_email='jonas@steinka.mp',
    install_requires=[
        'parse',
        'requests'
    ],
    license='WTFPL',
    packages=['pygitea']
)
