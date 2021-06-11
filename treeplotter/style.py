####################################################################################################
# File:     style.py
# Purpose:  Style helpers for the package.
#
# Author:   Luke Poeppel
#
# Location: Kent, 2021
####################################################################################################
class ConnectorStyle:
	"""
	Wrapper for the RaphaëlJS connector style between Nodes.
	"""
	def __init__(
			self,
			stroke,
			arrow_end,
			cursor,
			fill,
			fill_opacity,
			opacity,
			stroke_dasharray,
			stroke_linecap,
			stroke_opacity,
			stroke_width
		):
		self.stroke = stroke
		self.arrow_end = arrow_end
		self.cursor = cursor
		self.fill = fill
		self.fill_opacity = fill_opacity
		self.opacity = opacity
		self.stroke_dasharray = stroke_dasharray
		self.stroke_linecap = stroke_linecap
		self.stroke_opacity = stroke_opacity
		self.stroke_width = stroke_width

# : 'black'
# 			arrow-end: {string}
# 			cursor: {string}
# 			fill: {string}
# 			fill-opacity: {number}
# 			opacity: {number}
# 			stroke: {string}
# 			stroke-dasharray: {string}
# 			stroke-linecap: {string}
# 			stroke-opacity: {number}
# 			stroke-width: {number}

class NodeStyle:
	def __init__(
			self,
			background_color,
			font_family,
			font_size,
			text_align,
			width,
			border,
			padding,
		):
		"""
		Parameters
		----------
		background_color : str
			The background color of the node, given in hex.
		"""
		self.background_color = background_color
		self.font_family = font_family
		self.font_size = font_size
		self.text_align = text_align
		self.width = width
		self.border = border
		self.padding = padding

	def stylesheet(self):
		return {
			"backgroun-color": self.background_color,
			"text-align": self.text_align,
			"font-family": self.font_family,
			"font-size": self.font_size
		}


"""
.treeNode {
	text-align: center;
	padding: 2px;
	-webkit-border-radius: 3px;
	-moz-border-radius: 3px;
	border-radius: 3px;
	background-color: #ffffff;
	border: 1px solid #000;
	width: fit-content;
	font-family: Tahoma;
	font-size: 12px;
}
"""

# class DefaultNodeStyle(NodeStyle):
# 	def __init__(self):
# 		super(NodeStyle, self).__init__(

# 			width="fit-content"
# 		)