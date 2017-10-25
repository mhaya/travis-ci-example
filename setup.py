from setuptools import setup, find_packages
import sys

sys.path.append('./src')
sys.path.append('./tests')

setup_requires = [
    'pytest-runner',
    ]

tests_require = [
    'pytest-cov',
    'pytest',
    ]


setup(
    name = 'App',
    version = '0.1',
    description='This is test codes for travis ci',
    packages = find_packages(),
    setup_requires=setup_requires,
   tests_require=tests_require
)

