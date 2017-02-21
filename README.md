# Alexa Pi Arduino ir Remote

A basic example for making your echo turn on your tv.

# WAT?

Say "Alexa, turn on the television" and have the TV turn on.

* A simple Python app that allows the Pi to accept comm. from an Alex Echo. (works, but hacky)

# HOW?

An Alexa signals to a Raspberry pi that in turn sends signal to an Arduino that flashes an ir led to turn on your tv.

## To Use:

* Download Raspian Lite [Image](https://www.raspberrypi.org/downloads/raspbian/).
* Download [Win32DiskImage](https://sourceforge.net/projects/win32diskimager/) tool.
* Download the files in this repository.
* Modify [setup_pi_part_1.bash](https://github.com/EntropyHaos/z_haos_raspberry_pi_home_server_setup_script_set/blob/master/setup_pi_part_1.bash) variables with your new user name and ssh public key.
* Write Image to SD card.
* Copy blank file with name 'ssh' to SD card.
* Boot pi.
* SSH into pi using 
    * login id : 'pi'
    * password : 'raspberry'
* Add modified setup_pi_part_1.bash script to pi user directory.
* Run script with 'sudo bash etup_pi_part_1.bash'
* Exit login with 'exit' command.
* Login with username modified above using ssh key.
* Run bash script ```delete_default_pi_user.bash``` to delete default pi user.
* Add setup_pi_part_2.bash script to user directory.
* Run script.
* Flash arduino with file ```pi_serial_receive_basic.ino```
* Connect ir led and resistor in series to pin 3 of arduino.
* Add files in alexa_app directory to pi.
* Run app on pi with ```sudo python alexa_pi_arduino_ir_remote.py```
* The app should startup and communicate that it has found the arduino.
* Say "Alexa find devices" or use Alexa UI at [http://alexa.amazon.com/](http://alexa.amazon.com/) to find devices.
* Running script with ```sudo nohup python ~/alexa_app/alexa_pi_arduino_ir_remote.py &``` will allow the app to keep running after logging out of terminal.

# WHY?

*Because i can?* No, really, because i've done this too many times and wanted to stream line it.

Because i can't find my remote and it'd be nice if the tv was on while i was looking for it.

# WEN?

*Spring 2017*

Version : 0.0001 (Use at your own risk!)

Right now. Takes a few hours at the most to setup.

# WER?

In your home.

# WHO?

Anyone who has an Amazon Echo, a Raspberry Pi, an Arduino Uno, a ir led, a resistor, and some wires.