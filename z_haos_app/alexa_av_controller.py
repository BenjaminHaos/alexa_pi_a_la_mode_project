# Source : https://github.com/toddmedema/echo/blob/master/example-minimal.py
# Source : https://github.com/toddmedema/echo

# Alexa Setup Local : https://alexa.amazon.com/
import sys;

sys.path.insert(0, '/home/pi/alexa_pi_a_la_mode_project/z_haos_app/lib');
sys.path.insert(0, '/home/pi/alexa_pi_a_la_mode_project/z_haos_app/scripts/python');

import fauxmo
import logging
import time

#from debounce_handler import debounce_handler

from device_handler import device_handler

#import subprocess

run_alexa_listener = True;
#run_alexa_listener = False;

logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.WARNING)
#logging.basicConfig(level=logging.ERROR)
#logging.basicConfig(level=logging.CRITICAL)

logging.debug("Alexa AV Controller About to Start!");

if __name__ == "__main__" and run_alexa_listener:
    # Startup the fauxmo server
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)

    # Register the device callback as a fauxmo handler
    d = device_handler()
    
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)

    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception, e:
            logging.critical("Critical exception: " + str(e))
            break
