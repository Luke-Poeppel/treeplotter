####################################################################################################
# File:     style.py
# Purpose:  Style helpers for the package.
#
# Author:   Luke Poeppel
#
# Location: Kent, 2021
####################################################################################################
import cssutils

from dataclasses import dataclass, asdict
from jinja2 import Template

def write_index_html(background_color, path):
	HTML = """
	<!DOCTYPE html>
	<html>
		<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<meta name="viewport" content="width=device-width">
		<title> Fragment Tree </title>
		<link rel="stylesheet" href="Treant.css">
		<link rel="stylesheet" href="treeplotter.css">

	</head>
	<body>
		<style>
			body {
				height: 100%;
				margin: 0;
				padding: 0;
				background-color: {{color}};
			}
			</style>
		<div class="chart" id="treeplotter"></div>
		<script src="raphael.js"></script>
		<script src="Treant.min.js"></script>
		<script src="bundle.js"></script>
	</body>
	</html>
	"""
	template = Template(HTML)
	with open(path, "w") as index_filepath:
		index_filepath.write(template.render(color=background_color))

def write_treant_css(path):
	TREANT_CSS = """
	.Treant { position: relative; overflow: hidden; padding: 0 !important; }
	.Treant > .node,
	.Treant > .pseudo { position: absolute; display: block; visibility: hidden; }
	.Treant.Treant-loaded .node,
	.Treant.Treant-loaded .pseudo { visibility: visible; }
	.Treant > .pseudo { width: 0; height: 0; border: none; padding: 0; }
	.Treant .collapse-switch {
		width: 3px;
		height: 3px;
		display: block;
		border: 1px solid black;
		position: absolute;
		top: 1px;
		right: 1px;
		cursor: pointer;
	}
	.Treant > .node img {	border: none; float: left; }
	"""
	sheet = cssutils.parseString(TREANT_CSS)
	cssTextDecoded = sheet.cssText.decode("ascii")
	with open(path, "w") as TREANT_CSS_FILEPATH:
		TREANT_CSS_FILEPATH.write(str(cssTextDecoded))

@dataclass
class ConnectorStyle:
	"""
	Wrapper for the RaphaëlJS connector style between Nodes. See the following link for a complete
	description of the available attributes: http://raphaeljs.com/reference.html#Element.attr.

	Allowed values for `arrow_end`: `"classic"`, `"block"`, "`open"`, "`oval"`, "`diamond"`.
	Allowed values for `arrow_width`: "`wide"`, "`narrow"`, "`midium"`.
	Allowed values for `arrow_length`: "`long"`, "`short"`, "`midium"`.
	"""
	stroke: str = "black"
	arrow_end: str = None
	arrow_width: str = None
	arrow_length: str = None
	cursor: str = None
	fill: str = None
	fill_opacity: int = None
	opacity: int = None
	stroke_dasharray: str = None
	stroke_linecap: str = None
	stroke_opacity: int = None
	stroke_width: int = None

	def style(self):
		dict_out = dict()
		for key, val in asdict(self).items():
			if val:
				dict_out[key] = val
		return dict_out

# class NodeStyle:
# 	def __init__(
# 			self,
# 			background_color,
# 			font_family,
# 			font_size,
# 			text_align,
# 			width,
# 			border,
# 			padding,
# 		):
# 		"""
# 		Parameters
# 		----------
# 		background_color : str
# 			The background color of the node, given in hex.
# 		"""
# 		self.background_color = background_color
# 		self.font_family = font_family
# 		self.font_size = font_size
# 		self.text_align = text_align
# 		self.width = width
# 		self.border = border
# 		self.padding = padding

# 	def stylesheet(self):
# 		return {
# 			"backgroun-color": self.background_color,
# 			"text-align": self.text_align,
# 			"font-family": self.font_family,
# 			"font-size": self.font_size
# 		}


# """
# .treeNode {
# 	text-align: center;
# 	padding: 2px;
# 	-webkit-border-radius: 3px;
# 	-moz-border-radius: 3px;
# 	border-radius: 3px;
# 	background-color: #ffffff;
# 	border: 1px solid #000;
# 	width: fit-content;
# 	font-family: Tahoma;
# 	font-size: 12px;
# }
# """

# # class DefaultNodeStyle(NodeStyle):
# # 	def __init__(self):
# # 		super(NodeStyle, self).__init__(

# # 			width="fit-content"
# # 		)