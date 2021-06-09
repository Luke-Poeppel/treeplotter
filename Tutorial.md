### Tutorial
Here's an example of a few nodes.
```
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
```