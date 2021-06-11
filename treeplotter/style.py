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

def write_treant_css(background_color, path):
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
	.Treant .collapsed .collapse-switch { background-color: %s; }
	.Treant > .node img {	border: none; float: left; }
	""" % background_color
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