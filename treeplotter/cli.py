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
@click.option("--standard", default=False)
@click.option("--screenshot", default=False)
@click.option("--force", default=False)
def install_assist(standard, screenshot, force):
	"""
	Installation assistant for MacOS.

	Whether to force install R, webshot, and phantomJS without asking for input from the user.
	This is really only intended to be used with github actions.
	"""
	run(
		install=True,
		standard=standard,
		screenshot=screenshot,
		force=force,
	)
