import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "VERSION")) as version_file:
	__version__ = version_file.readline()