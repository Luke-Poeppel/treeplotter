class Node:
	"""
	A Node object stores an item and references its parent and children. In an Nary tree, a parent
	may have any arbitrary number of children, but each child has only 1 parent.
	"""
	def __init__(self, value, name=None, **kwargs):
		self.value = value
		self.name = name
		self.parent = None

		self.children = set()

	def __repr__(self):
		return '<NODE: value={0}, name={1}>'.format(self.value, self.name)

	def __hash__(self):
		return hash(self.value)

	def __eq__(self, other):
		"""
		Without this, you can add nodes with the same value to the set of children.
		"""
		return (self.value == other.value)

	def __lt__(self, other):
		return (self.value < other.value)

	def __get__(self):
		"""
		TODO: index the node children?
		"""
		raise NotImplementedError

	def add_child(self, child_node):
		self.children.add(child_node)
		return

	def add_children(self, children_nodes=[]):
		if type(children_nodes) != list:
			raise TreeException('Nodes must be contained in a list.')

		for this_child in children_nodes:
			self.add_child(this_child)
		return

	def add_path_of_children(self, path, final_node_name):
		"""
		Adds a path of Nodes through ``self.children``.
		"""
		if path[0] != self.value:
			raise TreeException("First value in the path must be self.value.")

		curr = self
		i = 1
		while i < len(path):
			check = curr.get_child_by_value(path[i])
			if check is not None:
				curr = check
				i += 1
			else:
				if i == len(path) - 1:
					child = NaryTree().Node(value=path[i], name=final_node_name)
				else:
					child = NaryTree().Node(value=path[i])

				curr.add_child(child)
				curr = child
				i += 1

		return

	def remove_child(self, child_node):
		if child_node.item.value not in self.children:
			raise TreeException("This parent does not have that child!")
		self.children.remove(child_node.item.value)
		return

	def remove_children(self, children_nodes):
		for this_child in children_nodes:
			try:
				self.remove_child(this_child)
			except KeyError:
				raise TreeException("One of the values in children_nodes was not found.")
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

	def ordered_children(self):
		"""Returns the children of a node in list format, ordered by value."""
		return sorted([child for child in self.children])

	def write_to_json(self):
		"""Used in the Treant.js visualization of Fragment trees."""
		net_children_data = []
		for this_child in self.children:
			data = {"info": {"name": this_child.name, "value": this_child.value}}
			net_children_data.append(data)

		out = {'info': {'name': self.name, 'value': self.value, 'children': net_children_data}}
		return json.dumps(out)

class Tree:
	"""
	Implementation of an NaryTree. 

	Nodes are hashed by their value and are stored in a set. For demonstration, we will create the
	following tree: (If a string appears next to a node value, this means the path from the root to
	that node is an encoded fragment.)

	>>> root = Tree().Node(value = 1.0, name = None) # LEVEL 1
	>>> c1 = Tree().Node(value = 0.5, name = None) # LEVEL 2
	>>> c2 = Tree().Node(value = 1.0, name = None)
	>>> c3 = Tree().Node(value = 3.0, name = 'A')
	>>> c3.value
	3.0
	>>> gc1 = Tree().Node(value = 0.5, name = None) # LEVEL 3
	>>> gc2 = Tree().Node(value = 3.0, name = 'B')
	>>> gc3 = Tree().Node(value = 2.0, name = 'C')
	>>> ggc = Tree().Node(value = 1.0, name = 'D') # LEVEL 4
	>>> root.parent = None
	>>> root.children = {c1, c2, c3}
	>>> root.children
	{<NODE: value=0.5, name=None>, <NODE: value=1.0, name=None>, <NODE: value=3.0, name=A>}
	>>> c1 in root.children
	True
	>>> root.ordered_children()
	[<NODE: value=0.5, name=None>, <NODE: value=1.0, name=None>, <NODE: value=3.0, name=A>]
	>>> c1.add_children([gc1, gc2])
	>>> c1.num_children
	2
	>>> c2.add_child(gc3)
	>>> gc1.add_child(ggc)
	>>> example_path = [root.value, 4.0, 1.0, 0.5, 2.0]
	>>> root.add_path_of_children(path = example_path, final_node_name = 'Full Path')
	>>> for child in root.children:
	... 	print(child)
	<NODE: value=0.5, name=None>
	<NODE: value=1.0, name=None>
	<NODE: value=3.0, name=A>
	<NODE: value=4.0, name=None>
	>>> # Check for overwriting data...
	>>> example_path_2 = [root.value, 1.0, 2.0, 1.0]
	>>> root.add_path_of_children(path = example_path_2, final_node_name = 'Test Overwrite')
	>>> # We can access children by referencing a node or by calling to its representative value.
	>>> newValue = root.get_child_by_value(4.0)
	>>> newValue.children
	{<NODE: value=1.0, name=None>}
	>>> c2.get_child(gc3)
	<NODE: value=2.0, name=C>
	>>> c2.get_child_by_value(2.0)
	<NODE: value=2.0, name=C>
	>>> c2.get_child_by_value(4.0)
	>>> TestTree = NaryTree()
	>>> TestTree.root = root
	>>> TestTree
	<trees.NaryTree: nodes=13>
	>>> TestTree.is_empty()
	False
	>>> # Calling the size returns the number of nodes in the tree.
	>>> TestTree.size()
	13
	>>> TestTree.all_possible_paths()
	[1.0]
	[1.0, 0.5]
	[1.0, 0.5, 0.5]
	[1.0, 0.5, 0.5, 1.0]
	[1.0, 0.5, 3.0]
	[1.0, 1.0]
	[1.0, 1.0, 2.0]
	[1.0, 1.0, 2.0, 1.0]
	[1.0, 3.0]
	[1.0, 4.0]
	[1.0, 4.0, 1.0]
	[1.0, 4.0, 1.0, 0.5]
	[1.0, 4.0, 1.0, 0.5, 2.0]
	>>> # Get paths of a particular length:
	>>> for this_path in TestTree.all_named_paths(cutoff = 3):
	...     print(this_path)
	B
	C
	>>> # We can search for paths as follows.
	>>> TestTree.search_for_path([1.0, 0.5, 0.5, 1.0])
	'D'
	>>> TestTree.search_for_path([1.0, 0.5, 3.0])
	'B'
	>>> TestTree.search_for_path([1.0, 2.0, 4.0])
	>>> TestTree.search_for_path([1.0, 1.0, 2.0])
	'C'
	>>> # Allow for unnamed paths to be found.
	>>> TestTree.search_for_path([1.0, 0.5, 0.5], allow_unnamed=True)
	[1.0, 0.5, 0.5]
	>>> # Level order traversal
	>>> TestTree.level_order_traversal()
	[[1.0], [0.5, 1.0, 3.0, 4.0], [0.5, 3.0, 2.0, 1.0], [1.0, 1.0, 0.5], [2.0]]
	>>> # We can serialize an NaryTree with NaryTree.serialize()
	"""
	def __init__(self):
		self.root = None

	def __repr__(self):
		return '<trees.NaryTree: nodes={}>'.format(self.size())

	def __iter__(self):
		"""
		Iterates through all named paths in the tree (not nodes), beginning with the shortest paths
		and ending with paths that end at the leaves. Ignores paths that do not end with a name.
		"""
		for this_named_path in self.all_named_paths():
			yield this_named_path

	def _size_helper(self, node):
		"""Helper function for self.size()."""
		num_nodes = 1
		for child in node.children:
			num_nodes += self._size_helper(child)

		return num_nodes

	def size(self):
		"""Returns the number of nodes in the nary tree."""
		return self._size_helper(self.root)

	def is_empty(self) -> bool:
		return (self.size() == 0)

	################################################################################################
	def serialize(self, for_treant=False):
		"""tree=pickled tree will not be needed in the actual tree."""
		def encapsulate(d):
			rv = {}
			value, name, parents, children = d.values()
			# Javascript's JSON.parse has a hard time with nulls.
			if name is None:
				name = ""
			if parents is None:
				parents = ""
			rv['text'] = {'value': value, 'name': name, 'parents': parents}
			rv['children'] = [encapsulate(c) for c in children]
			return rv

		pickled = jsonpickle.encode(self, unpicklable=False)

		if not for_treant:
			loaded = json.loads(pickled)
			return json.dumps(loaded)
		else:
			loaded = json.loads(pickled)
			w_text_field = {"nodeStructure": encapsulate(loaded["root"])}
			return json.dumps(w_text_field)

	################################################################################################
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

	################################################################################################
	# Level-Order Traversal
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

	################################################################################################
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
					return curr.name
				elif (i == len(path_from_root) - 1) and curr.name is not None:
					return curr.name
				else:
					i += 1
			else:
				if (i == len(path_from_root) - 1):
					return path_from_root
				else:
					i += 1

	def ld_search(self, path_from_root, allow_unnamed=False):
		"""
		This is a special use-case in :obj:`~decitala.trees.get_by_ql_array` based on the observation
		that the difference representation of mixed augmentations are linearly dependent. In this search
		tool, rather than checking if a path exists in a tree, we check on a level-order basis
		for a node for which the input is linearly dependent.

		:raises `NotImplementedError`:
		"""
		raise NotImplementedError