# `treeplotter`
I wasn't a huge fan of any of the available methods for tree plotting in Python. This package aims to make this easier. It wraps the TreantJS library to plot the trees and save them to a rendered HTML file. This HTML file can then be optionally exported as a high-res PNG by wrapping Rs webshot package.

### Usage
This library has `Node` and `Tree` classes in the `treeplotter.tree` module. 

### MacOS Installation
**Disclaimer**
I haven't tested this on anything other than MacOS (Big Sur). If you find this install works (or doesn't!) on other platforms, please file an issue or a Pull Request. 

This package requires a few installs. Sorry. Hopefully it's worth it. If all works, you should be able to copy-paste these commands into command line. 

1. Install homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Install `imagemagick`:
```
brew install imagemagick
```
3. Install `R`:
```
brew install r
```
4. Install `webshot`
```
Rscript installPkgs.R "webshot"
```
phantom js...