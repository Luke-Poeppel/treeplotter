####################################################################################################
# File:     installation_assistant.py
# Purpose:  Installation assistant for treeplotter. 
#
# Author:   Luke Poeppel
#
# Location: Kent, 2021
####################################################################################################
import subprocess

def run():
	"""
	Installation assistant for the treeplotter library. 
	"""
	res = subprocess.getoutput("~ Welcome to the treeplotter installation assistant. You will be asked before each package is installed. Proceed? [Y/n]")
	# if res:
	#     subprocess.run(["chmod", "+x", "package_installer.zsh"])
	#     subprocess.run(["./package_installer.zsh"])
	# else:
	#     subprocess.run(["echo EXITING"])

run()