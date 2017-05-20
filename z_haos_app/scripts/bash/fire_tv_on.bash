#!/bin/bash

echo "Fire TV On Script!";

# Set DIR to the directory this script is in.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Turn on the TV
source $DIR/television_on.bash

# Set TV Source to 2.0.0.0 (FireTV)
echo "tx 1F:82:20:00" | cec-client RPI -s -d 1
