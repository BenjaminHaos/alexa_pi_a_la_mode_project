# Alexa Pi à la Mode

*version 2.0*

## WAT?

This simple app allows an Amazon Alexa to control functions of a home A/V system.

Control is facilitated through two avenues. 

* The Consumer Electronics Control(CEC) feature of the High-Definition Multimedia Interface(HDMI).
* IR Signal Generation.


### Voice Controlled Abilities

* Turn one or more components on and/or off.
* Switch TV monitor to different inputs.
* Request website displayed to TV.

### Example Commands

* "Alexa, turn on TV."
    * Television turns on.
* "Alexa, turn off TV."
    * Television turns off.
* "Alexa, turn on/off Surround Sound."
    * A/V Reciever turns on and switches input to TV or turns off.
* "Alexa, turn on/off Google."
    * TV turns on and google search page is displayed or TV turns off and search is deleted.

## HOW?

### Setup and Testing

Although the repo is coded for an example system, it is easily understood and should be simple enough to make useful for most any system.

#### Example System

* **Raspberry Pi** *(Controls HDIM and CEC)*
* **Samsung TV** *(Controlled by HDIM CEC)*
* **Sony Receiver** *(Controlled by HDIM CEC and IR)*
* **FireTV Component** *(Controlled by HDIM CEC)*
* **Chromecast Component** *(Controlled by HDIM CEC)*

### Clone repo and setup Pi

Using a freshly imaged Pi, open a terminal and run these commands:

```
git clone https://github.com/BenjaminHaos/alexa_pi_a_la_mode_project.git
cd alexa_pi_a_la_mode_project
git checkout version_2.0
cd ..
bash alexa_pi_a_la_mode_project/z_haos_app/setup/setup_pi.bash
sudo reboot
```
### Run App

Once the above commands successfully been ran, open a terminal and run this command:
```
python alexa_pi_a_la_mode_project/z_haos_app/alexa_av_controller.py
```

### IR Ciruit

Read over [this tutorial]() if you'd like to setup the IR part of the project.

* [Setting up LIRC on the RaspberryPi - alexba.in](http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/)


## WHY?

Because it is needed?


## Libraries and Resources Used:

##### HDMI
* [LIRC - Linux Infrared Remote Control](http://www.lirc.org/)

##### WeMo Emulation
* Maker Musings' [fauxmo](https://github.com/makermusings/fauxmo) script.
* Todd Medema's [debounce_handler](https://github.com/toddmedema/echo/blob/master/debounce_handler.py) from [echo](https://github.com/toddmedema/echo).

##### IR
* Linux Infrared Remote Control [LIRC](http://www.lirc.org/)

* Trello [Board](https://trello.com/b/MZ76eJ5S)

