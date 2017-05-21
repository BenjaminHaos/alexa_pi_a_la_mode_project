# Initial Setup for Raspberry Pi HDMI CEC Using Windows Machine.


*This has been tested on a Windows 10 machine.*


##### *Devices and Software Used*

1. Windows 10 PC
1. Rasberry Pi3 Model B 
1. CEC capable television.
1. HDMI cable.
1. Ethernet network connecting Pi and PC.
1. [MobaXterm](http://mobaxterm.mobatek.net/) *you could probably use putty*.
1. sd card and reader/writer device.
1. Download and install Win32DiskImager.
1. Download and unzip 2017-04-10-raspbian-jessie-lite.zip.

#### Create Bootable SD Card for Pi on Windows Machine

1. Insert sd card into reader/writer device and plug device into computer.
1. Use windows diskpart tool to removes any and all partition or volume formatting from the disk.
1. Run command cmd.exe or open terminal by right clicking start menu button and choosing Command Prompt or Windows PowerShell
    1. ```> diskpart```
    1. ```> list disk``` *(Find your sd-card disk #)*
    1. ```> select disk <sd-card disk #>```
    1. ```> clean```
1. Use Win32DiskImager to write iso file to sd card.
    1. In Image File section, select image file from unzipped download.
    1. In Device section choose drive letter for your previously cleaned sd card.
    1. Click the ```Write``` button.
    1. Confirm overwrite making sure you have selected your drive. **BE CARFULL!**
    1. Wait for ```Write Successful.``` popup and click ```OK```.
    1. You might get a notifier to format the disk before or after doing the above, ignore with ```Cancel```.
1. Create empty file named ssh in root directory of sd card.[*](https://www.raspberrypi.org/forums/viewtopic.php?t=74176)
    1. Right click on desktop, click ```New >```, and click ```Text Document```.
    1. Rename the text document to ```ssh``` making sure to remove the ```.txt``` file extension.
    1. Ignore the warning about changing the file extension.
    1. Drag the file you just created to the ssd card which should be titled ```boot```.
1. Eject sd card in file-explorer and after safety notifcation, remove reader/writer device from computer.
1. Remove sd card from reader/writer device.

#### First Boot.

1. Unplug anything plugged into your pi.
1. Plug ethernet into pi.
1. Insert sd card created above.
1. Plug power cord into pi.
1. Use terminal program to ssh into pi.
    1. username is ```pi``` 
    1. password is ```raspberry```.
1. Change password for ```pi``` user.[*](https://www.raspberrypi.org/documentation/linux/usage/users.md)
1. ```$ passwd``` and follow prompts.

#### Modify ```pi``` Username

1. Disable tty automatically logging in the pi user.[*]()
    1. ```$ sudo raspi-config```
    1. Highlight ```3 Boot Options         Configure options for start-up``` using arrow keys and select with return key. 
    1. ```B1 Desktop / CLI            Choose whether to boot into a desktop environment or the command line```.
    1. ```B1 Console           Text console, requiring user to login```.
    1. You should be returned to the first menu.
    1. Highlight ```<Finish>``` using right arrow key and select with return key.
    1. Do not reboot pi.
1. Give root user a password with ```$ sudo passwd root```
1. Modify ```sshd_config``` file.[*](https://raspberrypi.stackexchange.com/questions/48056/login-as-root-not-possible)
    1. Edit file with ```$ sudo nano /etc/ssh/sshd_config```.
    1. Comment-out line ```PermitRootLogin without-password``` with ```#PermitRootLogin without-password```.
    1. Add line ```PermitRootLogin yes``` below commented out line.
    1. Save file with ```ctrl-o``` and hitting return.
    1. Exit with ```ctrl-x```.
1. Reboot pi with ```$ sudo reboot```
1. Login as ```root``` using password created above.
1. Change pi username with ```$ usermod -l <newname> pi```.
11. Change user previously named pi's home directory name with ```$ usermod -m -d /home/<newname> <newname>```
1. Reboot pi with ```$ sudo reboot```
1. Login with your new username and the password for pi user.
1. Test that you have sudo rights with ```$ sudo apt-get update```. You will have to enter your password.
11. If you have sudo rights
    1. Lock the root user's password with ```$ sudo passwd -l root```.
    1. Remove the modifications done to the ```sshd_config``` file above.
        1. Edit file with ```$ sudo nano /etc/ssh/sshd_config```.
        1. Change line ```#PermitRootLogin without-password``` to ```PermitRootLogin without-password```.
        1. Remove line ```PermitRootLogin yes```.
        1. Save file with ```ctrl-o``` and hitting return.
        1. Exit with ```ctrl-x```.
    1. Restart sshd service with ```$ sudo /etc/init.d/ssh restart```.

1. Create ssh key pair on the Windows machine used for ssh access to the Pi.
1. Create directory for public ssh key with ```$ mkdir .ssh```.
1. Create file for public key with ```$ printf "<ssh_public_key>"  >> .ssh/authorized_keys```
1. Set permissions for the folders you have just created.[*](https://mediatemple.net/community/products/dv/204644740/using-ssh-keys-on-your-server)
    1. ```$ chmod 700 .ssh```
    1. ```$ chmod 600 .ssh/authorized_keys```
1. Reboot pi with ```sudo reboot```

### Create Terminal Session with Username and SSH Key

1. In MobaXterm click session button.
2. Click ssh button.
3. Add Pi ip address in ```Remote host *``` field.
1. Select ```Specify username``` radio button.
1. Add new username  ```Specify username``` in field.
1. Click ```Advanced SSH settings``` tab.
1. Click ```Use private key``` radio button.
1. Click file navigator icon in ```Use private key``` field.
1. Navigate to your keyset and choose the private key. *(It should have a ```.ppk``` extension)* 
1. Click the ```OK``` button on the bottom of the ```Session settings``` window.
1. A terminal tab should open and you should login with no username or password requested.
1. Shotdown pi with ```sudo poweroff```
1. Disconnect power-supply to Pi.
1. With television turned off, connect HDMI cable.
1. Reconnect power-supply to Pi.
1. Your television should turn on and 

### Modify Pi Startup Behavior

1. Modify ```raspi-config``` file.
    1. Open editor with ```$ sudo nano /usr/bin/raspi-config```.
    1. Use ```ctrl-w``` to start a 'whereis' style search.[*](https://wiki.gentoo.org/wiki/Nano/Basics_Guide)
    1. Enter string ```do_boot_beh``` and hit return. The editor should move to the start of the ```do_boot_behaviour()``` function.
    1. Scroll down slightly to find the case statement on ```$BOOTOPT``` it should read something like ```case "$BOOTOPT" in```.
    1. In that case statement, find the switch for ```B4*``` which looks like ``` B4*)```.
    1. Substituting your new user name for ```<new user name>```, modify these two lines.
        1. ```if id -u pi > /dev/null 2>&1; then``` to ```if id -u <new user name> > /dev/null 2>&1; then```
        1. ```sed /etc/lightdm/lightdm.conf -i -e "s/^\(#\|\)autologin-user=.*/autologin-user=pi/"``` to ```sed /etc/lightdm/lightdm.conf -i -e "s/^\(#\|\)autologin-user=.*/autologin-user=<new user name>/"```

### Install and Test the CEC Adaptor Communication Library ```cec-utils```

1. Install, skipping prompt, with ```sudo apt-get install -y cec-utils```.[*](https://timleland.com/raspberry-pi-turn-tv-onoff-cec/)
1. Test install and show available commands with ```echo h | cec-client -s -d 1```.[*](https://raspberrypi.stackexchange.com/questions/9142/commands-for-using-cec-client)
1. Scan all devices connected to the HDMI bus with ```echo scan | cec-client -s -d 1```.
1. Turn device on with ```echo on <device number> | cec-client -s -d 1```, substituting <device number> with the device you want to turn on.
1. Standby device with ```echo standby <device number> | cec-client -s -d 1```, substituting <device number> with the device you want to turn on.
