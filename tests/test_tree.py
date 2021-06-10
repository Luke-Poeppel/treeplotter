import pytest

from treeplotter.tree import (
	Node,
	Tree
)

@pytest.fixture
def tutorial_tree():
	root = Node(value=1.0)

	child1 = Node(value=0.5)
	child2 = Node(value=1.0)
	child3 = Node(name="A", value=3.0)

	granchild1 = Node(value=0.5)
	granchild2 = Node(name="B", value=3.0)
	granchild3 = Node(name="C", value=2.0)

	greatgrandchild = Node(name="D", value=1.0)

	root.children = {child1, child2, child3}

	child1.add_children([granchild1, granchild2])
	child2.add_child(granchild3)
	
	granchild1.add_child(greatgrandchild)

	value_path = [root.value, 4.0, 1.0, 0.5, 2.0]
	root.add_path_of_children(path=value_path, final_node_name="Full path")

	value_path_2 = [root.value, 1.0, 2.0, 1.0]
	root.add_path_of_children(path=value_path_2, final_node_name="Testing overwrite")
	
	return Tree(root=root)

class TestTutorialTree:
	def test_num_nodes(self, tutorial_tree):
		assert tutorial_tree.size() == 13

	def test_empty(self, tutorial_tree):
		assert tutorial_tree.is_empty() == False

	def test_node_repr(self, tutorial_tree):
		c1 = tutorial_tree.root.get_child_by_value(0.5)
		assert c1.__repr__() == "<tree.Node name=None>"

	def test_root_name_and_value(self, tutorial_tree):
		assert tutorial_tree.root.value == 1
		assert tutorial_tree.root.name == None

	def test_root_children(self, tutorial_tree):
		values = [node.value for node in tutorial_tree.root.children]
		assert set(values) == {0.5, 1.0, 3.0, 4.0}

	def test_root_ordered_children(self, tutorial_tree):
		ordered_children = tutorial_tree.root.ordered_children()
		return [Node(value=0.5), Node(value=1.0), Node(name="A", value=3.0)]

	def test_child1_in_root_children(self, tutorial_tree):
		c1 = Node(value=0.5)
		assert c1 in tutorial_tree.root.children

	def test_get_child_by_value(self, tutorial_tree):
		assert tutorial_tree.root.get_child_by_value(value=3.0).name == "A"

	def test_search_for_path_B(self, tutorial_tree):
		final_node = tutorial_tree.search_for_path([1.0, 0.5, 3.0])
		assert final_node.name == "B"

	def test_search_for_path_C(self, tutorial_tree):
		final_node = tutorial_tree.search_for_path([1.0, 1.0, 2.0])
		assert final_node.name == "C"

	def test_search_for_path_D(self, tutorial_tree):
		final_node = tutorial_tree.search_for_path([1.0, 0.5, 0.5, 1.0])
		assert final_node.name == "D"

	def test_search_unnamed_path(self, tutorial_tree):
		path = tutorial_tree.search_for_path([1.0, 0.5, 0.5], allow_unnamed=True)
		assert path == [1.0, 0.5, 0.5] # If not found in tree, would return None
