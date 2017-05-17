# Show Available Commands

echo h | cec-client -s -d 1 # https://raspberrypi.stackexchange.com/questions/9142/commands-for-using-cec-client

================================================================================
Available commands:

[tx] {bytes}              transfer bytes over the CEC line.
[txn] {bytes}             transfer bytes but don't wait for transmission ACK.
[on] {address}            power on the device with the given logical address.
[standby] {address}       put the device with the given address in standby mode.
[la] {logical address}    change the logical address of the CEC adapter.
[p] {device} {port}       change the HDMI port number of the CEC adapter.
[pa] {physical address}   change the physical address of the CEC adapter.
[as]                      make the CEC adapter the active source.
[is]                      mark the CEC adapter as inactive source.
[osd] {addr} {string}     set OSD message on the specified device.
[ver] {addr}              get the CEC version of the specified device.
[ven] {addr}              get the vendor ID of the specified device.
[lang] {addr}             get the menu language of the specified device.
[pow] {addr}              get the power status of the specified device.
[name] {addr}             get the OSD name of the specified device.
[poll] {addr}             poll the specified device.
[lad]                     lists active devices on the bus
[ad] {addr}               checks whether the specified device is active.
[at] {type}               checks whether the specified device type is active.
[sp] {addr}               makes the specified physical address active.
[spl] {addr}              makes the specified logical address active.
[volup]                   send a volume up command to the amp if present
[voldown]                 send a volume down command to the amp if present
[mute]                    send a mute/unmute command to the amp if present
[self]                    show the list of addresses controlled by libCEC
[scan]                    scan the CEC bus and display device info
[mon] {1|0}               enable or disable CEC bus monitoring.
[log] {1 - 31}            change the log level. see cectypes.h for values.
[ping]                    send a ping command to the CEC adapter.
[bl]                      to let the adapter enter the bootloader, to upgrade
                          the flash rom.
[r]                       reconnect to the CEC adapter.
[h] or [help]             show this help.
[q] or [quit]             to quit the CEC test client and switch off all
                          connected CEC devices.
================================================================================

cec-client -h

cec-client {-h|--help|-l|--list-devices|[COM PORT]}

parameters:
  -h --help                   Shows this help text
  -l --list-devices           List all devices on this system
  -t --type {p|r|t|a}         The device type to use. More than one is possible.
  -p --port {int}             The HDMI port to use as active source.
  -b --base {int}             The logical address of the device to which this
                              adapter is connected.
  -f --log-file {file}        Writes all libCEC log message to a file
  -r --rom                    Read persisted settings from the EEPROM
  -sf --short-log-file {file} Writes all libCEC log message without timestamps
                              and log levels to a file.
  -d --log-level {level}      Sets the log level. See cectypes.h for values.
  -s --single-command         Execute a single command and exit. Does not power
                              on devices on startup and power them off on exit.
  -o --osd-name {osd name}    Use a custom osd name.
  -m --monitor                Start a monitor-only client.
  -i --info                   Shows information about how libCEC was compiled.
  [COM PORT]                  The com port to connect to. If no COM
                              port is given, the client tries to connect to the
                              first device that is detected.

Type 'h' or 'help' and press enter after starting the client to display all
available commands


================================================================================
Available commands:

[tx] {bytes}              transfer bytes over the CEC line.
[txn] {bytes}             transfer bytes but don't wait for transmission ACK.
[on] {address}            power on the device with the given logical address.
[standby] {address}       put the device with the given address in standby mode.
[la] {logical address}    change the logical address of the CEC adapter.
[p] {device} {port}       change the HDMI port number of the CEC adapter.
[pa] {physical address}   change the physical address of the CEC adapter.
[as]                      make the CEC adapter the active source.
[is]                      mark the CEC adapter as inactive source.
[osd] {addr} {string}     set OSD message on the specified device.
[ver] {addr}              get the CEC version of the specified device.
[ven] {addr}              get the vendor ID of the specified device.
[lang] {addr}             get the menu language of the specified device.
[pow] {addr}              get the power status of the specified device.
[name] {addr}             get the OSD name of the specified device.
[poll] {addr}             poll the specified device.
[lad]                     lists active devices on the bus
[ad] {addr}               checks whether the specified device is active.
[at] {type}               checks whether the specified device type is active.
[sp] {addr}               makes the specified physical address active.
[spl] {addr}              makes the specified logical address active.
[volup]                   send a volume up command to the amp if present
[voldown]                 send a volume down command to the amp if present
[mute]                    send a mute/unmute command to the amp if present
[self]                    show the list of addresses controlled by libCEC
[scan]                    scan the CEC bus and display device info
[mon] {1|0}               enable or disable CEC bus monitoring.
[log] {1 - 31}            change the log level. see cectypes.h for values.
[ping]                    send a ping command to the CEC adapter.
[bl]                      to let the adapter enter the bootloader, to upgrade
                          the flash rom.
[r]                       reconnect to the CEC adapter.
[h] or [help]             show this help.
[q] or [quit]             to quit the CEC test client and switch off all
                          connected CEC devices.
================================================================================

CEC bus information
===================
device #0: TV
address:       0.0.0.0
active source: no
vendor:        Samsung
osd string:    TV
CEC version:   unknown
power status:  standby
language:      eng


device #1: Recorder 1
address:       3.0.0.0
active source: no
vendor:        Pulse Eight
osd string:    CECTester
CEC version:   1.4
power status:  on
language:      eng

device #4: Playback 1
address:       2.0.0.0
active source: no
vendor:        Toshiba
osd string:    Amazon FireTV
CEC version:   1.4
power status:  on
language:      ???



device #5: Audio
address:       1.0.0.0
active source: no
vendor:        Sony
osd string:    AV AMP
CEC version:   1.4
power status:  standby
language:      ???


device #8: Playback 2
address:       1.3.0.0
active source: no
vendor:        Google
osd string:    Chromecast
CEC version:   1.4
power status:  on
language:      ???



