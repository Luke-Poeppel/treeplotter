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

if [ $1 == "force" ]
then
    echo Force installing R and the webshot package...
    install_r
    install_webshot
else
    echo Would you like to install R? [Y/n]
    read resp_R
    if [ $resp_R == "Y" ]
    then 
        install_r
    fi
    
    echo Would you like to install the webshot package? [Y/n]
    read resp_webshot
    if [ $resp_webshot == "Y" ]
    then
        install_webshot
    fi
fi