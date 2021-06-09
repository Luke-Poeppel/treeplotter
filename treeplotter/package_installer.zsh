#!/bin/zsh
echo Updating or installing homebrew...
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo Updating or installing imagemagick...
brew install imagemagick

echo Updating or installing node...
brew install node

echo Updating or installing phantomJS
brew tap homebrew/cask
brew cask install phantomjs

echo Installing browserify (JS library)
npm install -g browserify

# Installing R???!!
# brew install r
# Rscript installPkgs.R "webshot"