http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html

http://cosmolinux.no-ip.org/raconetlinux2/boot.html


```bash
#! /bin/sh
# /etc/init.d/alexa_listener_script

### BEGIN INIT INFO
# Provides:          alexa_listener
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Script to startup Python Alexa Listener.
# Description:       A simple script from www.stuffaboutcode.com which will start / stop a program a boot / shutdown.
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting Alexa Listener"
    # run application you want to start
    python /home/pi/z_haos_app/alexa_av_controller.py &
    ;;
  stop)
    echo "Stopping Alexa Listener"
    # kill application you want to stop
    #killall alexa_av_controller.py
    sudo pkill -9 -f alexa_av_controller.py;
    ;;
  *)
    echo "Usage: /etc/init.d/alexa_listener_script {start|stop}"
    exit 1
    ;;
esac

exit 0
```

sudo update-rc.d alexa_listener_script defaults
