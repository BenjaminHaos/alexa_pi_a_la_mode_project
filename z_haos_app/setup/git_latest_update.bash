#!/bin/bash

function lose_changes_pull_latest_modify_permissions() {
    local DIR;
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";

    cd $DIR
    cd ..
    cd ..

    git reset --hard HEAD;
    git pull;
    sudo bash $DIR/change_permissions.bash;
}

lose_changes_pull_latest_modify_permissions;
