#!/usr/env/bin python

from setuptools import setup

setup(
    name='pygitea',
    version='0.0',
    description='Gitea API wrapper for python',
    url='https://github.com/h44z/pygitea',
    author='Jonas',
    author_email='jonas@steinka.mp',
    install_requires=[
        'parse',
        'requests'
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    license='WTFPL',
    packages=['pygitea']
)
