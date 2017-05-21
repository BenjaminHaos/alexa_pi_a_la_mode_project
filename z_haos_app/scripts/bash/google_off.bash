#!/bin/bash

echo "Google Off Script!";

# Set DIR to the directory this script is in.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Kill All Chromium Browsers
sudo pkill chromium

# Turn off the TV
source $DIR/television_off.bash
