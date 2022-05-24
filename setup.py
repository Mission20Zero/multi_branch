from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in multi_branch/__init__.py
from multi_branch import __version__ as version

setup(
	name="multi_branch",
	version=version,
	description="Multiple Branches",
	author="M20Zero",
	author_email="hello@m20zero.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
