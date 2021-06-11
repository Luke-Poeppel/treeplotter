### MacOS Installation
**Disclaimer**: I've only tested this on MacOS (Big Sur 11.2.2 and Catalina 10.15). If you find this install doesn't work on other versions and OSs, please file an Issue or a Pull Request! 

First, install `treeplotter` with:
```
$ pip3 install treeplotter
```
To plot tree diagrams in HTML files, the basic requirements are: `homebrew`, `imagemagick`, `node`, and `browserify`. You can either install these requirements individually, or you can use the built-in `treeplotter` installation assistant. Simply run: 
```
$ treeplotter install-assist --standard True
```
If you'd like to also be able to save screenshots of the trees as high-res PNGs, you will also need `phantomJS`, `R`, and `webshot`. Again, you can either install these requirements individually or use the `install-assistant` with:
```
$ treeplotter install-assist screenshot
```

Now, `create_tree_diagram` will save screenshots of the tree to the directory.  

### Troubleshooting
If you're running MacOS and see issues related to R installation, it may help to add the following to your `.zshrc`:
```
export PATH=$PATH:/Library/Frameworks/R.framework/Resources
```