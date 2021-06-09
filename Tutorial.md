### Tutorial
#### `Node` and `Tree` classes. 
To make a tree in the `treeplotter` library, we create nodes, create links between them, and finall store them in a tree. To create a node, you need only two values: a `value` and a `name`. (Eventually, this package might support more complex objects.) First, let's import the package and create a root node object. 
```
>>> from treeplotter.tree import Node, Tree
>>> root = Node(value=1.0, name=None)
```
Now lets say this `root` has three initial children, only one of which has a name. Let's create these children and their link to `root`. 
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
We now have a proper tree object. Lastly, there's a method in the package for easily creating several nodes as a "lineage" called the `Node.add_path_of_children` method. Let's add two paths of children from the root. 
```
>>> value_path = [root.value, 4.0, 1.0, 0.5, 2.0]
>>> root.add_path_of_children(path=value_path, final_node_name="Full path")

>>> value_path_2 = [root.value, 1.0, 2.0, 1.0]
>>> root.add_path_of_children(path=value_path_2, final_node_name="Testing overwrite")
```
But now we just have a bunch of nodes... To create a Tree object, just pass the `root` node!
```
>>> tree =  Tree(root=root)
>>> tree
<tree.Tree nodes=13>
```
There are several other properties and methods for working with trees in the package. See the source for these. 

#### Making a Tree Diagram
We now have our awesome `tree` object in the package. But who cares? We want to see it! To do so, 
we use the `plotter.make_tree_diagram` function.
```
>>> from treeplotter.plotter import make_tree_diagram
>>> make_tree_diagram(
...     tree=tree,
...     save_path=...,
...     verbose=True
... )
>>> # This will display some logs and save an image of the tree to your desired directory. 
```
Additionally, you can call `tree.show(save_path, verbose)` to return (and save) a `wand.Image` object. This 
is useful when working with the package in Jupyter, for example. This method will return a file called `shot.png` in the requests
`save_path` directory. The above tree creates the following image:

<img src="tutorial_tree.png" height="250" width="715" style="border: 2px solid">