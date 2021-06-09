# `treeplotter`
Tree plotting is a nightmare in Python. This package aims to make this easier. It wraps the TreantJS library to plot python Tree objects and saves them to a rendered HTML file. This HTML file can then be optionally exported as a high-res PNG by wrapping Rs ``webshot`` package. It requires some installs, but after doing so you'll––ideally––never have to touch javascript or CSS. 

### Usage
This library has `Node` and `Tree` classes in the `treeplotter.tree` module. `Node` objects (currently) store a value and a name (string or `None`). We can then specify the nodes children and parent. A `Tree` is then defined by a root. We can then write an image of this tree (rendered by TreantJS) to an HTML file and save it to PNG via webshot. See `Tutorial.md` to see how it is used. 

This package is used in the `decitala` package (see [here](https://github.com/Luke-Poeppel/decitala)) to make `FragmentTree` diagrams, like the following one:
<img src="Prosodic_Tree.png" height="250" width="715" style="border: 2px solid">

### MacOS Installation
**To plot any tree diagrams, you must follow these instructions!**
I've only tested this on MacOS (Big Sur). If you find this install doesn't work on other platforms, please file an Issue or a Pull Request. This package requires a few installs. Sorry. Hopefully it's worth it. To avoid the complication of requiring the user to install a number of different resources individually, I've created an installation assistant that will run the procedure for you. You can tell the installer to avoid installing any of the packages in the assistant (if, for example, you already have it installed). To begin, run the following in the interpreter:
```
>>> from treeplotter import installation_assistant
>>> installation_assistant.run(install=True)
```

### Troubleshooting
If you're running MacOS and see issues related to R installation, it may help to add the following to your `.zshrc`:
```
export PATH=$PATH:/Library/Frameworks/R.framework/Resources
```