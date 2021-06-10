#!/bin/zsh
echo Updating or installing homebrew...
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo Updating or installing imagemagick...
brew install imagemagick

echo Updating or installing node...
brew install node

echo Updating or installing phantomJS...
brew install phantomjs

echo Installing browserify...
npm install -g browserify

##### 
function install_r {
    echo Installing R and the webshot package...
    brew install r
}

function install_webshot {
    echo Installing R and the webshot package...
    Rscript -e 'install.packages("webshot", repos="https://cloud.r-project.org")'
}

FORCED="forced"
YES="Y"

if [ "$1" = "$FORCED" ]; then
    echo Force installing R and the webshot package...
    install_r
    install_webshot
else
    echo -n  "Would you like to install R? [Y/n]: "
    read REPLY_R

    echo $REPLY_R
    if [ "$REPLY_R" = "$YES" ]; then
        install_r
    fi
    
    echo -n "Would you like to install the webshot package? [Y/n]: "
    read REPLY_WEBSHOT

    if [ "$REPLY_WEBSHOT" = "$YES" ]; then
        install_webshot
    fi
fi