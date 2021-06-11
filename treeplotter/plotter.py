####################################################################################################
# File:     plotter.py
# Purpose:  Plotting module.
#
# Author:   Luke Poeppel
#
# Location: Kent, 2021
####################################################################################################
import logging
import os
import json
import sys
import subprocess
import shutil
import tempfile

here = os.path.abspath(os.path.dirname(__file__))
treant_templates = here + "/templates"

def get_logger(name, print_to_console=True, write_to_file=None):
	"""
	A simple helper for logging. Copied from my `decitala` package.
	"""
	logger = logging.getLogger(name)
	if not len(logger.handlers):
		logger.setLevel(logging.INFO)

		if write_to_file is not None:
			file_handler = logging.FileHandler(write_to_file)
			logger.addHandler(file_handler)
		if print_to_console:
			stdout_handler = logging.StreamHandler(sys.stdout)
			logger.addHandler(stdout_handler)

	return logger

def _prepare_chart_config(tree):
	chart_config = dict()
	chart_config["container"] = "#treeplotter"
	connector_type_dict = {
		"type": tree.connector_type
	}
	chart_config["connectors"] = connector_type_dict
	HTML_dict_obj = {
		"HTMLclass": "treeNode"
	}
	chart_config["node"] = HTML_dict_obj
	dumped = json.dumps(chart_config)
	with open("chart_config.json", "w") as chart_config_file:
		json.dump(dumped, chart_config_file)
	return

def _prepare_docs_and_screenshot(path, serialized_tree, logger):
	with open("tree.json", "w") as json_file:
		json.dump(serialized_tree, json_file)

	logger.info("-> Copying .js files...")
	for this_file in os.listdir(treant_templates):
		shutil.copyfile(treant_templates + "/" + this_file, path + "/" + this_file)

	logger.info("-> Running browserify...")
	parse_data_file = "/".join([path, "parse_data.js"])
	browserified_file = "/".join([path, "bundle.js"])
	os.system(f"browserify {parse_data_file} -o {browserified_file}")

	logger.info("-> Creating webshot with R...")
	webshot_string = "webshot::webshot(url={0}, file={1}, zoom=3, selector={2})".format(
		"'" + path + "/index.html" + "'",
		"'" + path + "/shot.png" + "'",
		"'" + ".Treant" + "'"
	)
	subprocess.call(
		[
			f"""Rscript -e "{webshot_string}" """
		],
		shell=True
	)

def create_tree_diagram(tree, save_path=None, verbose=False):
	"""
	This function creates a visualization of a given :obj:`~decitala.trees.FragmentTree`
	using the Treant.js library. If a path is provided, all the files will be stored there. Otherwise,
	they will be stored in a tempfile for the display.
	"""
	if verbose:
		logger = get_logger(name=__name__, print_to_console=True)
	else:
		logger = get_logger(name=__name__, print_to_console=False)

	serialized = tree.serialize(for_treant=True)

	logger.info("-> Creating directory and writing tree to JSON...")
	if save_path:
		if not(os.path.isdir(save_path)):
			os.mkdir(save_path)
		os.chdir(save_path)
		_prepare_chart_config(tree)
		_prepare_docs_and_screenshot(save_path, serialized_tree=serialized, logger=logger)
		logger.info("Done ✔")
		return save_path
	else:
		with tempfile.TemporaryDirectory() as tmpdir:
			os.chdir(tmpdir)
			_prepare_docs_and_screenshot(tmpdir, serialized_tree=serialized, logger=logger)
			logger.info("Done ✔")
			with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
				shutil.copyfile(tmpdir + "/shot.png", tmpfile.name)
				return tmpfile.name