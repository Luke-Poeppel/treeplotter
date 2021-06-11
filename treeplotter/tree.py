####################################################################################################
# File:     tree.py
# Purpose:  Simple Python NaryTree objects.
#
# Author:   Luke Poeppel
#
# Location: Kent, 2021
####################################################################################################
import json
import jsonpickle

from collections import deque
from wand.image import Image

from .plotter import create_tree_diagram
from .style import (
	ConnectorStyle,
	NodeStyle
)

class NodeException(Exception):
	pass

class TreeException(Exception):
	pass

class Node:
	"""
	A Node object stores an item and references to its children. A parent may have any
	arbitrary number of children, but each child has only 1 parent. You can also store
	a relative or absolute path to an image in the `image` parameter.
	"""
	def __init__(
			self,
			name=None,
			value=None,
			image=None,
			**kwargs
		):
		"""
		Attributes
		----------

		name : str
			name to be displayed in the node.
		value : class
			value to be displayed in the node.
		image : float
			path to image file to be displayed in the node.
		"""
		self.name = name
		self.value = value
		self.image = image

		self.children = set()

	def __repr__(self):
		return "<tree.Node name={0}>".format(self.name)

	def __hash__(self):
		return hash(str(self.name) + str(self.value) + str(self.image))

	def __eq__(self, other):
		return (self.value == other.value)

	def __lt__(self, other):
		return (self.value < other.value)

	def add_child(self, child_node):
		self.children.add(child_node)
		return

	def add_children(self, children_nodes=[]):
		if type(children_nodes) != list:
			raise NodeException('Nodes must be contained in a list.')

		for this_child in children_nodes:
			self.add_child(this_child)
		return

	def add_path_of_children(self, path, final_node_name):
		"""
		Iterative solution. TODO: recursive.
		"""
		if path[0] != self.value:
			raise NodeException("First value in the path must be self.value.")

		curr = self
		i = 1
		while i < len(path):
			check = curr.get_child_by_value(path[i])
			if check is not None:
				curr = check
				i += 1
			else:
				if i == len(path) - 1:
					child = Node(value=path[i], name=final_node_name)
				else:
					child = Node(value=path[i])

				curr.add_child(child)
				curr = child
				i += 1
		return

	def remove_child(self, child_node):
		if child_node.item.value not in self.children:
			raise NodeException("This parent does not have that child.")
		self.children.remove(child_node.item.value)
		return

	def remove_children(self, children_nodes):
		for this_child in children_nodes:
			try:
				self.remove_child(this_child)
			except KeyError:
				raise NodeException("One of the values in children_nodes was not found.")
		return

	def get_child(self, node):
		"""Given another Node, returns the node in the set of children with the same value."""
		for this_child in self.children:
			if this_child.value == node.value:
				return this_child
		else:
			return None

	def get_child_by_value(self, value):
		for this_child in self.children:
			if this_child.value == value:
				return this_child
		else:
			return None

	@property
	def num_children(self) -> int:
		return len(self.children)

	@property
	def has_children(self) -> bool:
		return (self.num_children != 0)

class Tree:
	"""
	Implementation of an NaryTree.

	Attributes
	----------

	root : tree.Node
		A `tree.Node` object, acting as the root of the tree.
	connector_type : str
		The connector type of the tree, i.e. the Treant style used in the visualization. Common
		options are `"curved"`, `"bCurve"`, `"step"`, and `"straight"`.
	connector_style : style.ConnectorStyle
		An optional `style.ConnectorStyle` object. Comes from the Raphaël package.
	orientation : str
		Orientation of the tree in the visualization. Options are `"north"`, `"east"`,
		`"south"`, and "`west`".
	node_style: style.NodeStyle
		An optional `style.NodeStyle` object. Determines what the nodes in the tree will look like.
	"""
	def __init__(
			self,
			root=None,
			connector_type="curved",
			connector_style=ConnectorStyle(),
			orientation="north",
			node_style=NodeStyle()
		):
		self.root = root
		self.connector_type = connector_type
		self.connector_style = connector_style
		self.orientation = orientation
		self.node_style = node_style

	def __repr__(self):
		return '<tree.Tree nodes={}>'.format(self.size())

	def __iter__(self):
		"""
		Iterates through all named paths in the tree (not nodes), beginning with the shortest paths
		and ending with paths that end at the leaves. Ignores paths that do not end with a name.
		"""
		for this_named_path in self.all_named_paths():
			yield this_named_path

	def size(self) -> int:
		"""Returns the number of nodes in the nary tree."""
		def _size_helper(node):
			"""Helper function for self.size()."""
			num_nodes = 1
			for child in node.children:
				num_nodes += _size_helper(child)
			return num_nodes
		return _size_helper(self.root)

	def is_empty(self) -> bool:
		return (self.size() == 0)

	def serialize(self, for_treant=True) -> str:
		def encapsulate(d):
			data = {}
			name, value, image, children = d.values()
			if not(name):
				name = ""
			if not(value):
				value = ""
			if not image:
				image = ""
			data["text"] = {
				"value": value,
				"name": name,
			}
			data["image"] = image
			data["children"] = [encapsulate(child) for child in children]
			return data

		pickled = jsonpickle.encode(self, unpicklable=False)
		if for_treant:
			loaded = json.loads(pickled)
			with_nodeStructure = {
				"nodeStructure": encapsulate(loaded["root"])}
			return json.dumps(with_nodeStructure)
		else:
			loaded = json.loads(pickled)
			return json.dumps(loaded)

	################################################################################################
	# A few miscellaneous methods for working with trees.
	def _all_possible_paths_helper(self, node, path=[]):
		"""Helper function for self.all_possible_paths()."""
		path.append(node.value)
		print(path)
		if len(node.children) == 0:
			pass
		else:
			for child in node.children:
				self._all_possible_paths_helper(child, path)
		path.pop()

	def all_possible_paths(self):
		"""Returns all possible paths from the root node, not all of which are necesarrily named.
		Currently returns a numpy error."""
		return self._all_possible_paths_helper(self.root)

	def _all_named_paths_helper(self, node, cutoff, path=[]):
		"""Helper function for self.all_named_paths()."""
		path.append(node)

		if path[-1].name is not None:
			p = [node.value for node in path]
			if cutoff != 0:
				if len(p) == cutoff:
					yield path[-1].name
			else:
				if path[-1].name == 'ROOT':
					pass
				else:
					yield path[-1].name
		else:
			pass

		if len(node.children) == 0:
			pass
		else:
			for child in node.children:
				yield from self._all_named_paths_helper(node=child, cutoff=cutoff, path=path)

		path.pop()

	def all_named_paths(self, cutoff=0):
		"""
		Returns all named paths from the root. An optional ``cutoff`` parameter restricts to paths of
		length :math:`n`.
		"""
		for this_named_path in self._all_named_paths_helper(node=self.root, cutoff=cutoff):
			yield this_named_path

	def _subpaths_helper(self, node):
		raise NotImplementedError

	def _subpaths(self, name):
		"""Given a name (hopefully attached to a node), returns a list of the subpaths below that node."""
		raise NotImplementedError

	def _superpaths_helper(self, node):
		raise NotImplementedError

	def _superpaths(self, name):
		"""Given a name (hopefully attached to a node), returns a list of the subpaths above that node."""
		raise NotImplementedError

	def search_for_path(self, path_from_root, allow_unnamed=False):
		"""
		Searches for ``path_from_root`` through the tree for a continuous path to a node.

		:param numpy.array path_from_root: path to search in tree.
		:param bool allow_unnamed: whether or not to allow for unnamed paths to be found.
		:return: either the name of the final node or, if ``allow_unnamed=True``,
				possibly ``path_from_root``.
		:raises `~decitala.trees.TreeException`: when an invalid path or representation type is provided.
		"""
		assert (path_from_root[0] == 0.0 or path_from_root[0] == 1.0), TreeException("{} is an invalid root value.".format(path_from_root[0])) # noqa
		assert len(path_from_root) >= 2, TreeException("Path provided must be at least 2 values long.")

		curr = self.root
		i = 1
		while i < len(path_from_root):
			try:
				curr = curr.get_child_by_value(value=path_from_root[i])
				if curr is None:
					return None
			except AttributeError:
				break

			if allow_unnamed is False:
				if (i == len(path_from_root) - 1) and len(curr.children) == 0:
					return curr
				elif (i == len(path_from_root) - 1) and curr.name is not None:
					return curr
				else:
					i += 1
			else:
				if (i == len(path_from_root) - 1):
					return path_from_root
				else:
					i += 1

	def level_order_traversal(self):
		"""Returns the level order traversal of an NaryTree."""
		if not self.root:
			return []
		queue = deque([self.root])
		result = []
		while len(queue):
			level_result = []
			for i in range(len(queue)):
				node = queue.popleft()
				level_result.append(node.value)
				for child in node.children:
					queue.append(child)
			result.append(level_result)

		return result

	def show(self, save_path, verbose=False):
		"""
		Show the tree object directly from the class
		"""
		pdf_filepath = create_tree_diagram(FragmentTree=self, verbose=verbose)
		img = Image(filename=pdf_filepath)
		if save_path is not None:
			img.save(filename=save_path)
		else:
			return img