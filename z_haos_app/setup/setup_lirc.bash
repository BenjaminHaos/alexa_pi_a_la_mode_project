#!/bin/bash

# Re-synchronize the package index files from their sources.
sudo apt-get update

# Install lirc
sudo apt-get -y install lirc

# Append lines for lirc to end of modules files
cat << 'EOF' >> /etc/modules

lirc_dev
lirc_rpi gpio_in_pin=23 gpio_out_pin=22

EOF

# Change hardware file.

cat << 'EOF' > /etc/lirc/hardware.conf

########################################################
# /etc/lirc/hardware.conf
#
# Arguments which will be used when launching lircd
LIRCD_ARGS="--uinput"

# Don't start lircmd even if there seems to be a good config file
# START_LIRCMD=false

# Don't start irexec, even if a good config file seems to exist.
# START_IREXEC=false

# Try to load appropriate kernel modules
LOAD_MODULES=true

# Run "lircd --driver=help" for a list of supported drivers.
DRIVER="default"
# usually /dev/lirc0 is the correct setting for systems using udev
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"

# Default configuration files for your hardware if any
LIRCD_CONF=""
LIRCMD_CONF=""
########################################################

EOF


# Append lines to config file.
cat << 'EOF' >> /boot/config.txt

dtoverlay=lirc-rpi,gpio_in_pin=23,gpio_out_pin=22

EOF

cat << 'EOF' > /etc/lirc/lircd.conf
#
# this config file was automatically generated
# using lirc-0.8.5(commandir) on Sun Jul 26 19:34:37 2009
#
# contributed by
#
# brand:                       SONY
# model no. of remote control: RM-AAU014
# devices being controlled by this remote: SONY Stereo Receiver
#

begin remote

  name  SONY_RM-AAU014
  bits           15
  flags SPACE_ENC|CONST_LENGTH
  eps            30
  aeps          100

  header       2486   498
  one          1291   502
  zero          693   502
  gap          40006
  min_repeat      1
  toggle_bit_mask 0x0

      begin codes
          BTN_STANDBY              0x7620
          BTN_POWER                0x540C
          BTN_VIDEO1               0x220C
          BTN_VIDEO2               0x3C0C
          BTN_VIDEO3               0x210C
          BTN_DVD                  0x5F0C
          BTN_SAT                  0x600D
          BTN_TV                   0x2B0C
          BTN_SA_CD                0x520C
          BTN_TUNER                0x420C
          BTN_2CH                  0x410D
          BTN_AFD                  0x210D
          BTN_MOVIE                0x610D
          BTN_MUSIC                0x490D
          KEY_1                    0x000C
          KEY_2                    0x400C
          KEY_3                    0x200C
          BTN_AMP_MENU             0x770D
          KEY_4                    0x600C
          KEY_5                    0x100C
          KEY_6                    0x500C
          KEY_7                    0x300C
          KEY_8                    0x700C
          KEY_9                    0x080C
          KEY_0                    0x480C
          BTN_DVD_MENU             0x5A0D
          BTN_DISPLAY              0x690C
          BTN_MUTING               0x140C
          BTN_LEFT                 0x2F0D
          BTN_UP                   0x0F0D
          BTN_RIGHT                0x6F0D
          BTN_DOWN                 0x4F0D
          BTN_SELECT               0x180C
          BTN_VOLUME_UP            0x240C
          BTN_VOLUME_DOWN          0x640C
      end codes

end remote
EOF

