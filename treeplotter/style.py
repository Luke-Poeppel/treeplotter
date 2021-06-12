####################################################################################################
# File:     style.py
# Purpose:  Style helpers for the package.
#
# Author:   Luke Poeppel
#
# Location: Kent, 2021
####################################################################################################
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
	template = Template(TREANT_CSS)
	with open(path, "w") as css_filepath:
		css_filepath.write(template.render())

def write_node_css(
		background_color,
		font_family,
		font_size,
		text_align,
		width,
		border,
		padding,
		border_radius,
		path
	):
	NODE_CSS = """
	body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,form,fieldset,
		input,textarea,p,blockquote,th,td { margin:0; padding:0; }
	table { border-collapse:collapse; border-spacing:0; }
	fieldset,img { border:0; }
	address,caption,cite,code,dfn,em,strong,th,var { font-style:normal; font-weight:normal; }
	caption,th { text-align:left; }
	h1,h2,h3,h4,h5,h6 { font-size:100%; font-weight:normal; }
	q:before,q:after { content:''; }
	abbr,acronym { border:0; }

	body { background: #fff; }
	/* optional Container STYLES */
	.chart { height: 100%; margin: 5px; width: 100%; }
	.Treant > .node {  }
	.Treant > p {
		font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue",
					Helvetica, Arial, "Lucida Grande", sans-serif;
		font-weight: bold;
		font-size: 12px;
	}
	.node-name { font-weight: bold;}

	.treeNode {
		text-align: {{ text_align }};
		padding: {{ padding }};
		-webkit-border-radius: 3px;
		-moz-border-radius: 3px;
		border-radius: {{ border_radius }};
		background-color: {{ background_color }};
		border: {{ border }};
		width: {{ width }};
		font-family: {{ font_family }};
		font-size: {{ font_size }};
	}
	.treeNode:active {
		box-shadow: inset 1px 1px 1px rgba(0,0,0,.1);
		margin: 1px 0 0 1px;
		border: 2px solid #D3D3CB;
	}
	.node.big-commpany .node-name {
		line-height: 30px;
		color: #9B9B9B;
	}
	.treeNode:hover .node-name {
		color: #8B8B8B;
		text-shadow: 1px 1px rgba(0,0,0,.15);
	}

	.treeNode img {
		margin-right:  10px;
		margin-left: 10px;
	}
	"""
	template = Template(NODE_CSS)
	with open(path, "w") as node_filepath:
		rendered = template.render(
			background_color=background_color,
			font_family=font_family,
			font_size=font_size,
			text_align=text_align,
			width=width,
			border=border,
			padding=padding,
			border_radius=border_radius,
		)
		node_filepath.write(rendered)

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

@dataclass
class NodeStyle:
	background_color: str = "#ffffff"
	font_family: str = "Times"
	font_size: str = "12px"
	text_align: str = "center"
	width: str = "fit-content"
	border: str = "1px solid #000"
	padding: str = "2px"
	border_radius: str = "3px"

	def style(self):
		return asdict(self)