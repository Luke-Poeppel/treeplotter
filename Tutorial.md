### Tutorial
#### `Node` and `Tree` classes. 
To make a tree in the `treeplotter` library, we create nodes, links between them, and finally store them in a tree. First, let's import the package and create a root node object. 
```
>>> from treeplotter.tree import Node, Tree
>>> root = Node(value=1.0, name=None)
```
Now lets say this `root` has three initial children, only one of which has a name. Let's create these children and then set their relationship to `root`. 
```
>>> child1 = Node(value=0.5, name=None)
>>> child2 = Node(value=1.0, name=None)
>>> child3 = Node(value=3.0, name="A")
>>> root.children = {child1, child2, child3}
>>> root.children
{<tree.Node value=0.5, name=None>, <tree.Node value=1.0, name=None>, <tree.Node value=3.0, name=A>}
```
Let's now create some grandchildren and a single great-grandchild in the tree:
```
>>> granchild1 = Node(value=0.5, name=None)
>>> granchild2 = Node(value=3.0, name="B")
>>> granchild3 = Node(value=2.0, name="C")
>>> greatgrandchild = Node(value=1.0, name="D")
```
We can add a list of children to a given node via the `Node.add_children` method. We can also add a single child with ther `Node.add_child` method. 
```
>>> child1.add_children([granchild1, granchild2])
>>> child2.add_child(granchild3)
>>> granchild1.add_child(greatgrandchild)
```
Also included in `treeplotter` is a method for easily creating several nodes as a "lineage" called `Node.add_path_of_children`. The values provided will then automatically create nodes and set their relationships. Let's add two paths of children from the root. 
```
>>> value_path = [root.value, 4.0, 1.0, 0.5, 2.0]
>>> root.add_path_of_children(path=value_path, final_node_name="Full path")

>>> value_path_2 = [root.value, 1.0, 2.0, 1.0]
>>> root.add_path_of_children(path=value_path_2, final_node_name="Testing overwrite")
```
To create a Tree object, just pass the `root` node!
```
>>> tree = Tree(root=root)
>>> tree
<tree.Tree nodes=13>
```
There are several other properties and methods for working with trees in the package. See the source for these. 

#### Making a Tree Diagram
We now have our `tree` object in the package. But who cares? We want to see it! To do so, use the 
`plotter.make_tree_diagram` function. Pass our `tree` to the `tree` parameter. The `save_path` is a path 
to a **folder which will be created upon running the function**. For instance, if I wanted to save the visualization to
a folder called `mytree` in my home directory, I would use:
```
>>> from treeplotter.plotter import make_tree_diagram
>>> make_tree_diagram(
...     tree=tree,
...     save_path="/Users/lukepoeppel/mytree",
...     verbose=True
... )
>>> # This will display some logs and save an image of the tree to your desired directory. 
```
Additionally, you can call `tree.show(save_path, verbose)` to return (and save) a `wand.Image` object. This 
is useful when working with the package in Jupyter, for example. This method will return a file called `shot.png` in the requests
`save_path` directory. The above tree creates the following image:

<img src="images/tutorial_tree.png" height="250" width="715" style="border: 2px solid">

#### Image support
Beginning in v0.2.0, you can attach an image to a node object to display it in the visualization. 
```
>>> n1 = Node(name="Cat", image="/Users/lukepoeppel/treeplotter/tests/static/cat_small.jpg")
>>> n2 = Node(name="Friend O' Cat", image="/Users/lukepoeppel/treeplotter/tests/static/owl_small.jpg")
>>> n3 = Node(name="Foe O' Coat", image="/Users/lukepoeppel/treeplotter/tests/static/rabbit_small.jpg")
>>> n1.add_children([n2, n3])
>>> animal_tree = Tree(root=n1)
>>> create_tree_diagram(
...     tree=animal_tree,
...     save_path="/Users/lukepoeppel/treeplotter/tests/t6",
...     verbose=True
... )
```
This creates the following image:
<img src="images/image_nodes.png" height="250" width="715" style="border: 2px solid">
