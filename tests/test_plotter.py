import tempfile
import pytest
import os

from treeplotter.tree import Node, Tree
from treeplotter.plotter import create_tree_diagram
from treeplotter.style import ConnectorStyle, NodeStyle

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
	
	return Tree(root=root, connector_type="straight")

def test_plotter(tutorial_tree):
	with tempfile.TemporaryDirectory() as tmpdir:
		create_tree_diagram(
			tree=tutorial_tree,
			save_path=tmpdir,
			webshot=True,
			verbose=False
		)
		fcount = 0
		for f in os.listdir(tmpdir):
			if not(f.startswith(".")):
				fcount += 1
		assert fcount == 10
		assert os.path.isfile(tmpdir + "/tree.json")
		assert os.path.isfile(tmpdir + "/index.html")
		assert os.path.isfile(tmpdir + "/shot.png")

n1 = Node(name="Cat", image="/Users/lukepoeppel/treeplotter/tests/static/cat_small.jpg")
n2 = Node(name="Friend O' Cat", image="/Users/lukepoeppel/treeplotter/tests/static/owl_small.jpg")
n3 = Node(name="Foe O' Cat", image="/Users/lukepoeppel/treeplotter/tests/static/rabbit_small.jpg")
n1.add_children([n2, n3])

arrow_connector = ConnectorStyle(
	arrow_end="classic",
	arrow_width="wide",
	arrow_length="long"
)
node_style = NodeStyle(
	background_color="#89ADF0",
	border_radius="10px"
)
animal_tree = Tree(
	root=n1,
	connector_type="step",
	connector_style=arrow_connector,
	orientation="west",
	node_style=node_style
)

create_tree_diagram(
	tree=animal_tree,
	save_path="/Users/lukepoeppel/treeplotter/tests/t14",
	background_color="#cf2b2b",
	webshot=True,
	verbose=True
)