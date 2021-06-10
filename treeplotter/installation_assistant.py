####################################################################################################
# File:     installation_assistant.py
# Purpose:  Installation assistant for treeplotter.
#
# Author:   Luke Poeppel
#
# Location: Kent, 2021
####################################################################################################
import subprocess
import os

here = os.path.abspath(os.path.dirname(__file__))
executable_file = os.path.dirname(here) + "/treeplotter/package_installer.zsh"

def run(install=False, force=False):
	"""
	Installation assistant for the treeplotter library.
	"""
	subprocess.run("echo Welcome to the treeplotter installation assistant.", shell=True)
	if install:
		subprocess.run("echo Updating brew and installing requirements...", shell=True)
		subprocess.run(["chmod", "+x", executable_file])
		if force:
			subprocess.run([executable_file, "force"])
		else:
			subprocess.run([executable_file])
	else:
		subprocess.run("echo Exiting", shell=True)