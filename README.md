# Alexa Pi à la Mode


{Trello](https://trello.com/b/MZ76eJ5S)


Setup:

```sudo apt-get -y install cec-utils```

Turn off screen blanking [*](http://www.geeks3d.com/hacklab/20160108/how-to-disable-the-blank-screen-on-raspberry-pi-raspbian/)

Modify ```/etc/rc.local``` with ```sudo nano /etc/rc.local```

Adding line ```"/home/pi/z_haos_app/run_alexa_listener.bash" &``` above the ```exit 0``` line.

Uses:

Maker Musings' [fauxmo](https://github.com/makermusings/fauxmo) script.

Todd Medema's [debounce_handler](https://github.com/toddmedema/echo/blob/master/debounce_handler.py) from [echo](https://github.com/toddmedema/echo).

