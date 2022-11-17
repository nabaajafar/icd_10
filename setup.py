from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in icd_10/__init__.py
from icd_10 import __version__ as version
setup(
	name="icd_10",
	version=version,
	description="ICD-10",
	author="Nabaa Busbaih",
	author_email="nabaajafar3@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
