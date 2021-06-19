####################################################################################################
# File:     setup.py
# Purpose:  Setup of the package.
#
# Author:   Luke Poeppel
#
# Location: Kent, CT 2021
####################################################################################################
from setuptools import setup, find_packages

VERSION = "0.4.3"

with open('README.md') as f:
	long_description = f.read()

setup(
	name="treeplotter",
	version=VERSION,
	author="Luke Poeppel",
	author_email="luke.poeppel@gmail.com",
	description="Python package for tree plotting.",
	long_description=long_description,
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
		"jsonpickle",
		"jinja2",
		"Wand",
	],
	extras_require={
		"dev": [
			"flake8",
			"pre-commit",
			"pytest",
		]
	},
	entry_points={
		"console_scripts": [
			"treeplotter = treeplotter.cli:treeplotter"
		]
	},
)