# Source : https://github.com/toddmedema/echo/blob/master/example-minimal.py

import fauxmo
import logging
import time

from debounce_handler import debounce_handler

logging.basicConfig(level=logging.DEBUG)

class device_handler(debounce_handler):
    # Publishes the on/off state requested,
    # and the IP address of the Echo making the request.

    TRIGGERS = {"television": 52000, "stereo": 52001}
    
    def act(self, client_address, state, name):
        if name == 'television':
          if state:
            #write_serial_out(1);
            print '%s on' % name;
          else:
            #write_serial_out(2);
            print '%s off' % name;
        elif name == 'stereo':
          if state:
            #write_serial_out(3);
            print '%s on' % name;
          else:
            #write_serial_out(4);
            print '%s off' % name;
        else:
          return False;        
        
        return True

if __name__ == "__main__":
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
