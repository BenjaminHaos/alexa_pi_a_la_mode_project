#!/bin/bash

function modify_permissions() {
    local DIR;
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";

    cd $DIR
    cd ..
    sudo chmod 700 -R ./lib;
    sudo chmod 700 -R ./scripts;
    sudo chmod 700 -R alexa_av_controller.py;
}

modify_permissions;
