### Tutorial
Here's an example of a few nodes.
```
>>> root = NaryTree().Node(value = 1.0, name = None) # LEVEL 1
>>> c1 = NaryTree().Node(value = 0.5, name = None) # LEVEL 2
>>> c2 = NaryTree().Node(value = 1.0, name = None)
>>> c3 = NaryTree().Node(value = 3.0, name = 'A')
>>> c3.value
3.0
>>> gc1 = NaryTree().Node(value = 0.5, name = None) # LEVEL 3
>>> gc2 = NaryTree().Node(value = 3.0, name = 'B')
>>> gc3 = NaryTree().Node(value = 2.0, name = 'C')
>>> ggc = NaryTree().Node(value = 1.0, name = 'D') # LEVEL 4
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
```