import os
import sys

from setuptools import setup

setup(
    name='Flask-KVSession-For-Me',
    version='1.0.0.dev0',
    url='https://github.com/ubiregiinc/flask-kvsession',
    license='MIT',
    author='Marc Brinkmann',
    description='Transparent server-side session support for flask',
    packages=['flaskext'],
    install_requires=[
        'Flask>=0.8', 'simplekv', 'werkzeug', 'itsdangerous',
    ],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
