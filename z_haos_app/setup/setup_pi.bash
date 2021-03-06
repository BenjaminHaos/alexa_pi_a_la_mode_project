#!/bin/bash

function setup_pi() {
    local DIR;
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
    sudo bash $DIR/setup_cec_utils.bash
    sudo bash $DIR/setup_lirc.bash
    sudo bash $DIR/change_permissions.bash
    sudo bash $DIR/stop_blanking_of_screen.bash
}

setup_pi;
