#!/bin/bash

echo "Raspberry Pi Off Script!";

# Set DIR to the directory this script is in.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Turn off the TV
source $DIR/television_off.bash
