from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bukubank_integration/__init__.py
from bukubank_integration import __version__ as version

setup(
	name="bukubank_integration",
	version=version,
	description="Integration with BukuBank API",
	author="Sekolah360",
	author_email="aulia@kataba.id",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
