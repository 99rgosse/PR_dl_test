#!/usr/env/bin python

from setuptools import setup

setup(
    name='pygitea',
    version='0.0',
    description='Gitea API wrapper for python',
    url='https://github.com/h44z/pygitea',
    author='h44z',
    author_email='h44z@sprinternet.at',
    license='WTFPL',
    packages=['pygitea'],
    zip_safe=False,
    install_requires=[
        'certifi==1,<2',
        'chardet==2',
        'idna==2.6',
        'parse==1.8.2',
        'pkg-resources==0.0.0',
        'requests==2.20.0',
        'urllib3==1.24.2',
    ]
)
