#!/bin/sh

##sass $1 > $2
##sass "static/css/${1}.sass" > "static/css/${1}.css"
sass "static/css/body.sass" > "static/css/style.css"
echo "Sass has compiled"

