# hello_raspberry_pi_cec

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

### Setup NOTES


### Browswer Dump *(Saturday)*

* [CEC (Consumer Electronics Control) over HDMI - eLinux.org](http://elinux.org/CEC_(Consumer_Electronics_Control)_over_HDMI)
* [raspberry pi cec - Google Search](https://www.google.com/search?q=raspberry+pi+cec&oq=raspberry+pi+cec&aqs=chrome..69i57j0l5.3503j0j7&sourceid=chrome&ie=UTF-8)
* [Raspberry Pi • View topic - Turn on / off TV via HDMI CEC](https://www.raspberrypi.org/forums/viewtopic.php?f=35&t=15749&sid=56b085cf9c2c1f4103a075c7f8fbb47e&start=25)
* [hdmi - Commands for using cec-client - Raspberry Pi Stack Exchange](https://raspberrypi.stackexchange.com/questions/9142/commands-for-using-cec-client)
* [Using cec-client to Control HDMI Devices | End Point Blog](http://blog.endpoint.com/2012/11/using-cec-client-to-control-hdmi-devices.html)
* [Raspberry Pi • View topic - Use RPi to change HDMI-Input to non-CEC device](https://www.raspberrypi.org/forums/viewtopic.php?f=35&t=15593&p=158409&hilit=cec_client#p158409)
* [raspberry pi cec - Google Search](https://www.google.com/search?q=raspberry+pi+cec&oq=raspberry+pi&aqs=chrome.0.69i59j69i57j0j69i59j0l2.2303j0j8&sourceid=chrome&ie=UTF-8)


* [Download Raspbian for Raspberry Pi](https://www.raspberrypi.org/downloads/raspbian/)
* [Win32 Disk Imager download | SourceForge.net](https://sourceforge.net/projects/win32diskimager/?source=typ_redirect)
* [pi_n_cec_note_taker - Cloud9](https://ide.c9.io/benjaminhaos/pi_n_cec_note_taker#openfile-README.md)

### Browswer Dump *(Sunday)*

* [What are your favorite tips and tricks for storage/access/use of arduino and all its parts? : arduino](https://www.reddit.com/r/arduino/comments/6b048t/what_are_your_favorite_tips_and_tricks_for/)
* [tackle box - Walmart.com](https://www.walmart.com/search/?query=tackle%20box)
* [Plano Medium Pro-Latch Organizer - Walmart.com](https://www.walmart.com/ip/Plano-Medium-Pro-Latch-Organizer/16351075?action=product_interest&action_type=title&beacon_version=1.0.2&bucket_id=irsbucketdefault&client_guid=f7ffe036-6574-418f-8fd3-8ea796ca3398&config_id=2&customer_id_enc&findingMethod=p13n&guid=f7ffe036-6574-418f-8fd3-8ea796ca3398&item_id=16351075&parent_anchor_item_id=16326925&parent_item_id=16326925&placement_id=irs-2-m2&reporter=recommendations&source=new_site&strategy=PWVAV&visitor_id=fNvWsBHNa7cQa-zCK5Xn78)
* [raspberry pi hdmi cec - Google Search](https://www.google.com/search?q=raspberry+pi+hdmi+cec&rlz=1CAACAT_enUS715US717&ei=gRAYWbLMB-jcjwTR87O4CQ&start=20&sa=N&biw=1318&bih=678)
* [Raspberry Pi Owners, Check Your TV Supports CEC Before You Spend | Lifehacker Australia](https://www.lifehacker.com.au/2015/04/raspberry-pi-owners-check-your-tv-supports-cec-before-you-spend/)
* [hdmi - Commands for using cec-client - Raspberry Pi Stack Exchange](https://raspberrypi.stackexchange.com/questions/9142/commands-for-using-cec-client)
* [CEC (Consumer Electronics Control) over HDMI - eLinux.org](http://elinux.org/CEC_(Consumer_Electronics_Control)_over_HDMI)
* [Controlling your TV with voice and Raspberry Pi – Tzahi Vidas – This is not for you](https://kazuar.github.io/raspberry_pi_voice_recognition/)
* [Pulse-Eight/libcec: USB CEC Adapter communication Library http://libcec.pulse-eight.com/](https://github.com/Pulse-Eight/libcec)
* [libcec/README.linux.md at master · Pulse-Eight/libcec](https://github.com/Pulse-Eight/libcec/blob/master/docs/README.linux.md)
* [libcec/README.raspberrypi.md at master · Pulse-Eight/libcec](https://github.com/Pulse-Eight/libcec/blob/master/docs/README.raspberrypi.md)
* [cec 0.2.3 : Python Package Index](https://pypi.python.org/pypi/cec/0.2.3)
* [Editing hello_raspberry_pi_cec/README.md at master · BenjaminHaos/hello_raspberry_pi_cec](https://github.com/BenjaminHaos/hello_raspberry_pi_cec/edit/master/README.md)
* [LibCEC on Raspberry Pi - Viva La Vida](http://oopsmonk.github.io/blog/2015/11/03/libcec-on-raspberry-pi)
* [CEC adventures on the Raspberry Pi | An external memory dump](https://drgeoffathome.wordpress.com/2014/08/08/cec-adventures-on-the-raspberry-pi/)
* [Gordon Turner » Using cec-client on a Raspberry Pi](https://blog.gordonturner.com/2016/12/14/using-cec-client-on-a-raspberry-pi/)
* [Raspberry Pi Turn Tv On/Off CEC – Tim Leland](https://timleland.com/raspberry-pi-turn-tv-onoff-cec/)
* [hdmi - Commands for using cec-client - Raspberry Pi Stack Exchange](https://raspberrypi.stackexchange.com/questions/9142/commands-for-using-cec-client)
* [trainman419/python-cec](https://github.com/trainman419/python-cec)

* [BenjaminHaos/alexa_pi_a_la_mode_project: Programmed functionality for IR remote that bridges control from Amazon Echo to A/V system.](https://github.com/BenjaminHaos/alexa_pi_a_la_mode_project)
* [raspberry pi cec - Google Search](https://www.google.com/search?q=raspberry+pi+cec-client&oq=raspberry+pi+cec-client&aqs=chrome..69i57j0l3.5719j0j4&sourceid=chrome&ie=UTF-8#q=raspberry+pi+cec)
* [hdmi - Commands for using cec-client - Raspberry Pi Stack Exchange](https://raspberrypi.stackexchange.com/questions/9142/commands-for-using-cec-client)
* [cec-client install - Google Search](https://www.google.com/search?q=cec-client&oq=cec-client&aqs=chrome..69i57j69i60l2&sourceid=chrome&ie=UTF-8#q=cec-client+install)
* [Using cec-client to Control HDMI Devices | End Point Blog](http://blog.endpoint.com/2012/11/using-cec-client-to-control-hdmi-devices.html)
* [CEC-O-MATIC](http://www.cec-o-matic.com/)
* [ubuntu shutdown - Google Search](https://www.google.com/search?q=ubuntu+shutdown&oq=ubuntu+shutdown&aqs=chrome..69i57j0l5.3071j0j8&sourceid=chrome&ie=UTF-8)
* [[SOLVED] How to launch google chrome from the command line](https://ubuntuforums.org/showthread.php?t=1385182)
* [ssh - Open a window in a remote machine - Ask Ubuntu](https://askubuntu.com/questions/405916/open-a-window-in-a-remote-machine)
* [How to launch google-chrome/chromium application shortcut in fullscreen/kiosk mode - Ask Ubuntu](https://askubuntu.com/questions/358898/how-to-launch-google-chrome-chromium-application-shortcut-in-fullscreen-kiosk-mo)
* [Haos Info](http://haos.info/)
* [Google Updates Hangouts, Lets You Adjust Bandwidth Used With A Slider, Adds Audio-Only Mode | TechCrunch](https://techcrunch.com/2013/02/07/google-updates-hangouts-lets-you-adjust-bandwidth-used-with-a-slider-adds-audio-only-mode/)
* [Disable screensaver and screen blanking Raspberry Pi - ETCwiki](http://www.etcwiki.org/wiki/Disable_screensaver_and_screen_blanking_Raspberry_Pi)
* [Python Script execute commands in Terminal - Stack Overflow](http://stackoverflow.com/questions/3730964/python-script-execute-commands-in-terminal)
* [Hello, World! - Learn Python - Free Interactive Python Tutorial](https://www.learnpython.org/en/Hello%2C_World%21)
* [A security update for Raspbian PIXEL - Raspberry Pi](https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/)
* [Copy All Urls - Chrome Web Store](https://chrome.google.com/webstore/detail/copy-all-urls/djdmadneanknadilpjiknlnanaolmbfk?hl=en)

### Browswer Dump *(Monday)*

* [raspberry pi change pi username - Google Search](https://www.google.com/search?q=raspberry+pi+change+pi+username&oq=raspberry+pi+change+pi+username&aqs=chrome..69i57j0l2.9287j0j8&sourceid=chrome&ie=UTF-8)
* [Linux users - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/linux/usage/users.md)
* [ModMyPi | How to Change the Default Account Username and Password](https://www.modmypi.com/blog/how-to-change-the-default-account-username-and-password)
* [Raspberry Pi • View topic - How to create a ISO from a customised raspbian system ?](https://www.raspberrypi.org/forums/viewtopic.php?t=49503&p=385472)

### Browswer Dump *(Tuesday)*

* [raspberry pi cec frames - Google Search](https://www.google.com/search?q=raspberry+pi+cec+frames&oq=raspberry+pi+cec+frames&aqs=chrome..69i57.5967j0j9&sourceid=chrome&ie=UTF-8)
* [Tips for using cec-client on a Raspberry Pi : raspberry_pi](https://www.reddit.com/r/raspberry_pi/comments/5ihbei/tips_for_using_cecclient_on_a_raspberry_pi/)
* [Gordon Turner » Using cec-client on a Raspberry Pi](https://blog.gordonturner.com/2016/12/14/using-cec-client-on-a-raspberry-pi/)
