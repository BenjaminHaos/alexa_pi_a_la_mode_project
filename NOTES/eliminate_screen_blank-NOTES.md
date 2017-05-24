* [How to Disable the Blank Screen on Raspberry Pi (Raspbian) | HackLab](http://www.geeks3d.com/hacklab/20160108/how-to-disable-the-blank-screen-on-raspberry-pi-raspbian/)

/etc/lightdm/lightdm.conf

[SeatDefaults]
xserver-command=X -s 0 -dpms

