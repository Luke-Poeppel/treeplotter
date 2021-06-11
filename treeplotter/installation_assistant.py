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
standard_installer = os.path.dirname(here) + "/treeplotter/standard_installer.zsh"
screenshot_installer = os.path.dirname(here) + "/treeplotter/screenshot_installer.zsh"

def run(
		install=False,
		standard=False,
		screenshot=False,
		force=False,
	):
	"""
	Installation assistant for the treeplotter library.
	"""
	subprocess.run("echo Welcome to the treeplotter installation assistant.", shell=True)
	if install:
		if standard:
			subprocess.run("echo Installing standard requirements...", shell=True)
			subprocess.run(["chmod", "+x", standard_installer])
			os.system(standard_installer)
		if screenshot:
			if force:
				subprocess.run("echo Force installing screenshot requirements...", shell=True)
				subprocess.run(["chmod", "+x", screenshot_installer])
				os.system(screenshot_installer + " forced")  # subprocess didn't work here...
			else:
				subprocess.run("echo Installing screenshot requirements...", shell=True)
				subprocess.run(["chmod", "+x", screenshot_installer])
				os.system(screenshot_installer + " unforced")
	else:
		subprocess.run("echo Exiting", shell=True)