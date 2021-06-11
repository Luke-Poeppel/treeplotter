# `treeplotter`
[![Actions Status](https://github.com/Luke-Poeppel/treeplotter/workflows/Build/badge.svg)](https://github.com/Luke-Poeppel/treeplotter/actions)
![img](https://img.shields.io/badge/semver-0.3.0-green)

Tree plotting is really hard in Python. This package aims to make the process easier. It wraps the TreantJS library to plot trees and saves them to a rendered HTML file. This HTML file is then also exported to a high-res PNG by wrapping R's ``webshot`` package. The package requires some complicated installs, but this is the price to pay to not use any R, Javascript, or CSS ;)

### Usage
This library has `Node` and `Tree` classes in the `treeplotter.tree` module. `Node` objects store a value and a name (string or `None`). We can then specify the nodes children and parent. A `Tree` is then defined by a root node. We can then create a tree visualization. See `Tutorial.md` for a complete demo. 

This package is used in the `decitala` package (see [here](https://github.com/Luke-Poeppel/decitala)) to make `FragmentTree` diagrams, like the following one of the Greek Prosodic Feet:

![](https://github.com/Luke-Poeppel/treeplotter/blob/master/images/Prosodic_Tree.png)

Images can be added to `Node` objects, and we can customize tree properties with connector types and orientation. 

![](https://github.com/Luke-Poeppel/treeplotter/blob/master/images/flipped_tree.png)

<!-- <img src="images/Prosodic_Tree.png" height="250" width="715" style="border: 2px solid"> -->
<!-- <img src="images/flipped_tree.png" height="250" width="715" style="border: 2px solid"> -->