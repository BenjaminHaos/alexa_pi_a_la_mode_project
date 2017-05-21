### Setup NOTES

#### Basic Setup

##### *Prerequisites*

1. sd card and reader/writer device.
1. Download and install Win32DiskImager.
2. Download and unzip 2017-04-10-raspbian-jessie-lite.zip.


1. Insert sd card into reader/writer device and plug device into computer.
2. Use windows diskpart tool to removes any and all partition or volume formatting from the disk.
3. Run command cmd.exe or open terminal by right clicking start menu button and choosing Command Prompt or Windows PowerShell
    3. ```diskpart```
    4. ```list disk``` *(Find your sd-card disk #)*
    5. ```select disk <sd-card disk #>```
    6. ```clean```
1. Use Win32DiskImager to write iso file to sd card.
2. Create file named ssh in ```/boot``` directory of sd card.[*](https://www.raspberrypi.org/forums/viewtopic.php?t=74176)

#### 
1. Unplug anything plugged into your pi.
3. Plug ethernet into pi.
4. Insert sd card created above.
5. Plug power cord into pi.
5. Use terminal program to ssh into pi.
    6. username is ```pi``` 
    7. password is ```raspberry```.
7. Change password for pi user.[*](https://www.raspberrypi.org/documentation/linux/usage/users.md)
8. ```passwd```


1. Create ssh key pair.
2. Create directory for public ssh key.
    1. ```mkdir .ssh```
3. Create file for public key.
    1. ```printf "<ssh_public_key>"  >> .ssh/authorized_keys```
4. Set permissions for the folders you have just created.[*](https://mediatemple.net/community/products/dv/204644740/using-ssh-keys-on-your-server)
1. ```chmod 700 .ssh/```
2. ```chmod 600 .ssh/authorized_keys```
exit


