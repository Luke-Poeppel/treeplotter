import pytest

from treeplotter.tree import (
	Node,
	Tree
)

@pytest.fixture
def tutorial_tree():
	root = Node(value = 1.0, name = None)

	child1 = Node(value = 0.5, name = None)
	child2 = Node(value = 1.0, name = None)
	child3 = Node(value = 3.0, name = "A")

	granchild1 = Node(value = 0.5, name = None)
	granchild2 = Node(value = 3.0, name = "B")
	granchild3 = Node(value = 2.0, name = "C")

	greatgrandchild = Node(value = 1.0, name = "D")

	root.children = {child1, child2, child3}

	child1.add_children([granchild1, granchild2])
	child2.add_child(granchild3)
	
	granchild1.add_child(greatgrandchild)

	value_path = [root.value, 4.0, 1.0, 0.5, 2.0]
	root.add_path_of_children(path = value_path, final_node_name = "Full path")

	# >>> for child in root.children:
	# ... 	print(child)
	# <NODE: value=0.5, name=None>
	# <NODE: value=1.0, name=None>
	# <NODE: value=3.0, name=A>
	# <NODE: value=4.0, name=None>
	# >>> # Check for overwriting data...
	# >>> example_path_2 = [root.value, 1.0, 2.0, 1.0]
	# >>> root.add_path_of_children(path = example_path_2, final_node_name = 'Test Overwrite')
	# >>> # We can access children by referencing a node or by calling to its representative value.
	# >>> newValue = root.get_child_by_value(4.0)
	# >>> newValue.children
	# {<NODE: value=1.0, name=None>}
	# >>> c2.get_child(gc3)
	# <NODE: value=2.0, name=C>
	# >>> c2.get_child_by_value(2.0)
	# <NODE: value=2.0, name=C>
	# >>> c2.get_child_by_value(4.0)
	
	tree = Tree(root=root)

	# >>> TestTree
	# <trees.NaryTree: nodes=13>
	# >>> TestTree.is_empty()
	# False
	# >>> # Calling the size returns the number of nodes in the tree.
	# >>> TestTree.size()
	# 13
	# >>> TestTree.all_possible_paths()
	# [1.0]
	# [1.0, 0.5]
	# [1.0, 0.5, 0.5]
	# [1.0, 0.5, 0.5, 1.0]
	# [1.0, 0.5, 3.0]
	# [1.0, 1.0]
	# [1.0, 1.0, 2.0]
	# [1.0, 1.0, 2.0, 1.0]
	# [1.0, 3.0]
	# [1.0, 4.0]
	# [1.0, 4.0, 1.0]
	# [1.0, 4.0, 1.0, 0.5]
	# [1.0, 4.0, 1.0, 0.5, 2.0]
	# >>> # Get paths of a particular length:
	# >>> for this_path in TestTree.all_named_paths(cutoff = 3):
	# ...     print(this_path)
	# B
	# C
	# >>> # We can search for paths as follows.
	# >>> TestTree.search_for_path([1.0, 0.5, 0.5, 1.0])
	# 'D'
	# >>> TestTree.search_for_path([1.0, 0.5, 3.0])
	# 'B'
	# >>> TestTree.search_for_path([1.0, 2.0, 4.0])
	# >>> TestTree.search_for_path([1.0, 1.0, 2.0])
	# 'C'
	# >>> # Allow for unnamed paths to be found.
	# >>> TestTree.search_for_path([1.0, 0.5, 0.5], allow_unnamed=True)
	# [1.0, 0.5, 0.5]
	# >>> # Level order traversal
	# >>> TestTree.level_order_traversal()
	# [[1.0], [0.5, 1.0, 3.0, 4.0], [0.5, 3.0, 2.0, 1.0], [1.0, 1.0, 0.5], [2.0]]
	# >>> # We can serialize an NaryTree with NaryTree.serialize()
	return tree

"""
# >>> root.children
# {<NODE: value=0.5, name=None>, <NODE: value=1.0, name=None>, <NODE: value=3.0, name=A>}
# >>> c1 in root.children
# True
# >>> root.ordered_children()
# [<NODE: value=0.5, name=None>, <NODE: value=1.0, name=None>, <NODE: value=3.0, name=A>]
"""

class TestTutorialTree:
	def test_num_nodes(self, tutorial_tree):
		print(tutorial_tree.size() == 13)
		assert tutorial_tree.size() == 13

	def test_root_name_and_value(self, tutorial_tree):
		assert tutorial_tree.root.value == 1
		assert tutorial_tree.root.name == None

	def test_root_children(self, tutorial_tree):
		values = [node.value for node in tutorial_tree.root.children]
		assert set(values) == {0.5, 1.0, 3.0}

	def test_get_child_by_value(self, tutorial_tree):
		assert tutorial_tree.root.get_child_by_value(value=3.0).name == "A"

	# def test_child1_num_children(self, tutorial_tree):
	# 	assert 
# 