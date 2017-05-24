#!/bin/bash

function setup_pi() {
    local DIR;
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
    sudo bash $DIR/setup_cec_utils.bash
    sudo bash $DIR/setup_lirc.bash

    cd $DIR
    cd ..
    sudo chmod 700 -R ./lib;
    sudo chmod 700 -R ./scripts;
    sudo chmod 700 -R alexa_av_controller.py;
}

setup_pi;
