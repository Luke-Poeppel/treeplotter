# Change Log
All important changes to the treeplotter package will be documented here.

The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and the project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.4.0](https://github.com/Luke-Poeppel/treeplotter/tree/v0.4.0) June 11, 2021
#### Added
- Upgraded styling system for the package with the `style.py` module. Created `NodeStyle` and `ConnectorStyle` objects to be used with the `Tree`. We can now customize several different features of the document, tree, and nodes. 

#### Changed
- All of the CSS and HTML templates (exluding the libraries, of course) are gone. They now come from strings (parsed by 
a jinja2 template) made in the style module. 

## [v0.3.1](https://github.com/Luke-Poeppel/treeplotter/tree/v0.3.1) June 11, 2021
#### Fixed
- Image display on PyPi. 

## [v0.3.0](https://github.com/Luke-Poeppel/treeplotter/tree/v0.3.0) June 11, 2021
#### Added
- Added support for `orientation` in `Tree` objects. 
- The package now has two install parameters: `treeplotter install-assist --standard` and `treeplotter install-assist --screenshot`. This allows the user to more carefully choose what they need to use the package. Added an `Installation.md` file with updated details. 

#### Changed
- The use of `R` and `webshot` is now fully optional! The user specifies `webshot=True` in `create_tree_diagram`. This will obviously fail if they don't have `R` installed. 

## [v0.2.0](https://github.com/Luke-Poeppel/treeplotter/tree/v0.2.0) June 11, 2021
#### Added
- Allow displaying images in the node. 
- Added a `show` method to `tree.Tree` objects. 
- Added support for `connector_type` in `Tree` objects. 

#### Removed
- Remove the `get_ordered_children` method for `Node`. It didn't make sense to keep it since nodes need no longer have a value. 
- Remove the `write_to_json` method for `Node`. It was unused anywhere in the package. 

## [v0.1.1](https://github.com/Luke-Poeppel/treeplotter/tree/v0.1.1) June 10, 2021
#### Added
- Added a CHANGELOG.md file.

#### Changed
- The `package_installer.zsh` now asks the user if they want to install `R` and webshot. Due to the versioning constraints of `R`, we don't want to install this without the user being sure!
- Minor tutorial improvements and rewordings.

## [v0.1.0](https://github.com/Luke-Poeppel/treeplotter/tree/v0.1.0) June 9, 2021
First public release