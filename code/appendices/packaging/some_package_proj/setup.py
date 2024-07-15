from setuptools import find_packages, setup

setup(
    name='some_package',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
