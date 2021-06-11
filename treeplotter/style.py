####################################################################################################
# File:     style.py
# Purpose:  Style helpers for the package.
#
# Author:   Luke Poeppel
#
# Location: Kent, 2021
####################################################################################################
from dataclasses import dataclass, asdict

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