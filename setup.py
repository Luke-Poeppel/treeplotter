####################################################################################################
# File:     setup.py
# Purpose:  Setup of the package.
#
# Author:   Luke Poeppel
#
# Location: Kent, CT 2021
####################################################################################################
import os

from setuptools import setup, find_packages

with open(os.path.join("treeplotter", "VERSION")) as version:
	__version__ = version.readline()

setup(
	name="treeplotter",
	version=__version__,
	author="Luke Poeppel",
	author_email="luke.poeppel@gmail.com",
	description="Python package for tree plotting.",
	long_description="Python package for tree plotting.",
	long_description_content_type="text/markdown",
	url="https://github.com/Luke-Poeppel/treeplotter",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
	include_package_data=True,
	package_data={"treeplotter": ["VERSION"]},
	install_requires=[
		"click",
		"flake8",
		"jsonpickle",
		"matplotlib",
		"pre-commit",
		"pytest",
		"Wand",
	],
	entry_points={
		"console_scripts": [
			"treeplotter = treeplotter.cli:treeplotter"
		]
	},
)