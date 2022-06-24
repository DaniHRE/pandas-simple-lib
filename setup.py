from setuptools import find_packages, setup

setup(
    name='pandassimplecrud',
    packages=find_packages(include=['pandascrud']),
    version='0.1.0',
    description='My first Python library with pandas.',
    author='@DaniHRE',
    license='MIT',
    install_requires=['pandas', 'tabulate'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
