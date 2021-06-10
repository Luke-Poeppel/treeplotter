####################################################################################################
# File:     cli.py
# Purpose:  Command line interface for the treeplotter package.
#
# Author:   Luke Poeppel
#
# Location: Kent, 2021
####################################################################################################
import click

from treeplotter import __version__
from .installation_assistant import run

@click.group()
@click.version_option(__version__, "--version", "-v", message="%(version)s")
def treeplotter():
	"""Returns the version of the module."""
	pass

@treeplotter.command()
@click.option("--force", default=False)
def install_assist(force):
	"""
	Installation assistant for MacOS.
	"""
	run(install=True, force=force)
