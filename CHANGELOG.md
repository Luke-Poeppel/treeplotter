# Change Log
All important changes to the treeplotter package will be documented here.

The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and the project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.2.0](https://github.com/Luke-Poeppel/treeplotter/tree/v0.2.0) ???
#### Added
- Allow displaying images in the node. 
- Added a `show` method to `tree.Tree` objects. 

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