#!/bin/bash

echo "Google On Script!";

# Set DIR to the directory this script is in.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Turn on the TV
source $DIR/raspberry_pi_on.bash

##### **Allow Command Line to [Open Windows on Remote Machine](https://askubuntu.com/questions/405916/open-a-window-in-a-remote-machine) :**  
export DISPLAY=:0

##### **Opens Chromium Browser Process to Google with No Country Redirect(/ncr) in Kiosk Mode (Full Screen, No Exit)**  
chromium-browser --kiosk https://www.google.com/ncr &
