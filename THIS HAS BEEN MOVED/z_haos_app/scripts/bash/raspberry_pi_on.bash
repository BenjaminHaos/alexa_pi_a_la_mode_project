#!/bin/bash

echo "Raspberry Pi On Script!";

# Set DIR to the directory this script is in.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Turn on the TV
source $DIR/television_on.bash

# Set TV Source to 3.0.0.0 (Raspberry Pi)
echo "tx 1F:82:30:00" | cec-client RPI -s -d 1
