import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.WARNING)
#logging.basicConfig(level=logging.ERROR)
#logging.basicConfig(level=logging.CRITICAL)

from debounce_handler import debounce_handler

television_on="./scripts/bash/television_on.bash";
television_off="./scripts/bash/television_off.bash";

class device_handler(debounce_handler):
    # Publishes the on/off state requested,
    # and the IP address of the Echo making the request.

    TRIGGERS = {"television": 52000, "stereo": 52001, "computer one": 52002}
    
    def act(self, client_address, state, name):
        if name == 'television':
          if state:
            #write_serial_out(1);
            #print 'Turning %s on!!' % name;
            logging.debug("Turning television on!!");
            subprocess.call(television_on, shell=True);
          else:
            #write_serial_out(2);
            print 'Turning %s off!!' % name;
            subprocess.call(television_off, shell=True);
        elif name == 'stereo':
          if state:
            #write_serial_out(3);
            print '%s on' % name;
          else:
            #write_serial_out(4);
            print '%s off' % name;
        elif name == 'computer one':
          if state:
            #write_serial_out(3);
            print '%s on' % name;
          else:
            #write_serial_out(4);
            print '%s off' % name;
        else:
          return False;        
        
        return True

