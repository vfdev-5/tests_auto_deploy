import os
import io
import re
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(os.path.join(os.path.dirname(__file__), *names),
                 encoding=kwargs.get("encoding", "utf8")) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


readme = read('README.md')

VERSION = find_version('check_auto_deploy', '__init__.py')

requirements = ['numpy', ]

setup(
    # Metadata
    name='check_auto_deploy',
    version=VERSION,
    author='vfdev-5',
    author_email='vfdev.5@gmail.com',
    url='https://github.com/vfdev-5/tests_auto_deploy/',
    description='A repository to test artifacts auto build/upload on conda and pipy on tagging the code.',
    long_description=readme,
    license='BSD',

    # Package info
    packages=find_packages(exclude=('tests', 'tests.*',)),

    zip_safe=True,
    install_requires=requirements,
)
