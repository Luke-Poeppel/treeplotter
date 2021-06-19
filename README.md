# `treeplotter`
[![Actions Status](https://github.com/Luke-Poeppel/treeplotter/workflows/Build/badge.svg)](https://github.com/Luke-Poeppel/treeplotter/actions)
![img](https://img.shields.io/badge/semver-0.4.3-green)

Tree plotting is really hard in Python. The `treeplotter` package aims to make the process easier. It wraps the TreantJS library to plot trees and saves them to a rendered HTML file. This HTML file is then also exported to a high-res PNG by wrapping R's ``webshot`` package. The package requires some complicated installs, but this is the price to pay to not use any R, Javascript, or CSS ;)

### Usage
This library has `Node` and `Tree` classes in the `treeplotter.tree` module. `Node` objects can store various items. We can then specify the node children and parents. A `Tree` is then defined by a root node. From this, we can create tree visualizations. See [here](https://github.com/Luke-Poeppel/treeplotter/blob/master/Tutorial.md) for a complete demo. 

This package is used in the `decitala` package (see [here](https://github.com/Luke-Poeppel/decitala)) to make `FragmentTree` diagrams, like the following one of the Greek Prosodic Feet:

![](https://github.com/Luke-Poeppel/treeplotter/blob/master/images/Prosodic_Tree.png)

![](https://github.com/Luke-Poeppel/treeplotter/blob/master/images/styled_tree.png)

### Installation
The basic package can be installed with
```
$ pip3 install treeplotter
```
To create the tree diagrams, however, some additional installs are required. See [here](https://github.com/Luke-Poeppel/treeplotter/blob/master/Installation.md) for the complete instructions. 