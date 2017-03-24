![Circuit Diagram](/docs/img/circuit_diagram.png)

# Alexa Pie à la Mode!

# [WAT?](http://haos.info/alexa_pi_a_la_mode_project/slides/index.html "CLICK TO VIEW PRESENTATION!")

A basic example that give your Amazon Echo the ability to turn on and off devices controlled by an IR Remote.

#### Say "Alexa, turn on the television" and have the TV turn on. Say "Alexa, turn on the stereo" and have the stereo turn on. Saying "Alexa, turn off <device>" turns off said device.

A few simple bits of code that allows a Raspberry Pi to accept communications from an Amazon Echo and in turn signal an Arduino to flash an IR led (or several.) Although it works, it is a bit hacky and is only setup for a basic proof of concept. As is right now, it turns on my TV and or my stereo.

### Supplies

#### Hardware

* Arduino
* Raspberry PI
* Amazon Echo
* Router

#### Electrical Bits

* IR LED(s)
* Resistors
* Wires
* Breadboard (optional)


# HOW?

An Alexa signals to a Raspberry pi that in turn sends signal to an Arduino that flashes an ir led to turn on your tv.

#### Arduino Circuit

![Circuit Diagram](/docs/img/circuit_diagram.jpg)

[Source](https://circuits.io/circuits/4368694-alexa-pi-a-la-mode-arduino-portion)

*note* Although the circuit is available online, running the simulation does not work at time of writing. I suspect the IRremote.h library is not being included correctly.

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


## Notes

* http://www.aftvnews.com/controlling-the-amazon-fire-tv-with-the-amazon-echo/
