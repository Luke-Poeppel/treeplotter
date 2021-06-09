# `treeplotter`
Tree plotting is a nightmare in Python. This package aims to make this easier. It wraps the TreantJS library to plot `Tree` objects and saves them to a rendered HTML file. This HTML file is then exported to a high-res PNG by wrapping R's ``webshot`` package. It requires some complicated installs, but this is the price to pay to not use any R, Javascript, or CSS ;)

### Usage
This library has `Node` and `Tree` classes in the `treeplotter.tree` module. `Node` objects store a value and a name (string or `None`). We can then specify the nodes children and parent. A `Tree` is then defined by a root node. We can then create an image of this tree (rendered by TreantJS) to an HTML file and save it to PNG via webshot. See `Tutorial.md` for a complete demo. 

This package is used in the `decitala` package (see [here](https://github.com/Luke-Poeppel/decitala)) to make `FragmentTree` diagrams, like the following one of the Greek Prosodic Feet:
<img src="images/Prosodic_Tree.png" height="250" width="715" style="border: 2px solid">

### MacOS Installation
**To plot any tree diagrams, you must follow these instructions!**
I've only tested this on MacOS (Big Sur). If you find this install doesn't work on other platforms, please file an Issue or a Pull Request. This package requires some complicated installs. Sorry. Hopefully it's worth it. To avoid the complication of requiring the user to install a number of different resources _individually_, I've created an installation assistant that will run the procedure for you. To begin, run the following in the interpreter:
```
>>> from treeplotter import installation_assistant
>>> installation_assistant.run(install=True)
```

### Troubleshooting
If you're running MacOS and see issues related to R installation, it may help to add the following to your `.zshrc`:
```
export PATH=$PATH:/Library/Frameworks/R.framework/Resources
```