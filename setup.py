from setuptools import setup, find_packages

import api

setup(
    name='tookan_api',
    version=api.__VERSION__,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests', 'pycrypto'],
    test_suite='nose.collector',
    tests_require=['nose', 'mock'],
)