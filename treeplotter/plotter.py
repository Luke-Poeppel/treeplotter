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

from .style import (
	write_index_html,
	write_treant_css,
	write_node_css
)

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

def prepare_arrow(dict_in):
	"""
	Raphaël's arrow formatting is a bit more involved. This parsing is done here.
	"""
	arrow_end = dict_in["arrow_end"]
	arrow_width = dict_in["arrow_width"]
	arrow_length = dict_in["arrow_length"]
	return "-".join([arrow_end, arrow_width, arrow_length])

def _prepare_chart_config(tree):
	chart_config = dict()
	chart_config["container"] = "#treeplotter"

	connector_style_pre = tree.connector_style.style()
	connector_style = dict()
	for key, val in connector_style_pre.items():
		if "_" in key:
			new_key = "-".join(key.split("_"))
			if key == "arrow_end":
				connector_style[new_key] = prepare_arrow(dict_in=connector_style_pre)
			elif key in {"arrow_length" or "arrow_width"}:
				continue
			else:
				connector_style[new_key] = val
		else:
			connector_style[key] = val

	connector_type_dict = {
		"type": tree.connector_type,
		"style": connector_style
	}
	chart_config["connectors"] = connector_type_dict
	chart_config["rootOrientation"] = tree.orientation.upper()

	HTML_dict_obj = {
		"HTMLclass": "treeNode"
	}
	chart_config["node"] = HTML_dict_obj

	dumped = json.dumps(chart_config)
	with open("chart_config.json", "w") as chart_config_file:
		json.dump(dumped, chart_config_file)
	return

def _prepare_docs_and_screenshot(
		path,
		tree,
		serialized_tree,
		background_color,
		webshot,
		logger
	):
	with open("tree.json", "w") as json_file:
		json.dump(serialized_tree, json_file)

	logger.info("-> Copying templates...")
	for this_file in os.listdir(treant_templates):
		shutil.copyfile(treant_templates + "/" + this_file, path + "/" + this_file)

	logger.info("-> Writing index.html...")
	write_index_html(
		background_color=background_color,
		path=path + "/" + "index.html"
	)

	logger.info("-> Writing Treant CSS file...")
	write_treant_css(path=path + "/" + "Treant.css")

	logger.info("-> Writing Node CSS file...")
	write_node_css(
		background_color=tree.node_style.background_color,
		font_family=tree.node_style.font_family,
		font_size=tree.node_style.font_size,
		text_align=tree.node_style.text_align,
		width=tree.node_style.width,
		border=tree.node_style.border,
		padding=tree.node_style.padding,
		border_radius=tree.node_style.border_radius,
		path=path + "/" + "treeplotter.css"
	)

	logger.info("-> Running browserify...")
	parse_data_file = "/".join([path, "parse_data.js"])
	browserified_file = "/".join([path, "bundle.js"])
	os.system(f"browserify {parse_data_file} -o {browserified_file}")

	if webshot:
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

def create_tree_diagram(
		tree,
		background_color="#868DEE",
		save_path=None,
		webshot=False,
		verbose=False
	):
	"""
	This function creates a visualization of a given `tree.Tree` by wrapping the TreantJS library.

	Parameters
	----------
	tree : tree.Tree
		A `tree.Tree` object.
	background_color : str
		Color (given in Hex) of the desired background color of the visualization.
	save_path : str
		Optional path to the directory in which all the relevant files will be saved. Default is `None`.
	webshot : bool
		Whether or not to invoke Rs webshot library to create a high-res screenshot of the tree.
		Default is `False`.
	verbose : bool
		Whether to print logging messages in the plotting process. Useful for debugging.
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
		_prepare_chart_config(tree=tree)
		_prepare_docs_and_screenshot(
			path=save_path,
			tree=tree,
			serialized_tree=serialized,
			background_color=background_color,
			webshot=webshot,
			logger=logger
		)
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