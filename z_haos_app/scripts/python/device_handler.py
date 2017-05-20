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

audio_on="./scripts/bash/sony_av_on.bash";
audio_off="./scripts/bash/sony_av_off.bash";

fire_tv_on="./scripts/bash/fire_tv_on.bash";
fire_tv_off="./scripts/bash/fire_tv_off.bash";

raspberry_pi_on="./scripts/bash/raspberry_pi_on.bash";
raspberry_pi_off="./scripts/bash/raspberry_pi_off.bash";

class device_handler(debounce_handler):
    # Publishes the on/off state requested,
    # and the IP address of the Echo making the request.

    TRIGGERS = {"Television": 52000, "Stereo": 52001, "Fire TV": 52002, "Raspberry Pi": 52003}
    
    
    def act(self, client_address, state, name):
        
        def device_handler_log(state, name):
            if state:
              logging.debug('Turning %s on.' % name);
            else:
              logging.debug('Turning %s off.' % name);
            return;
        
        device_handler_log(state, name);

        if name == 'Television':
          if state:
            subprocess.call(television_on);
          else:
            subprocess.call(television_off);
        elif name == 'Stereo':
          if state:
            subprocess.call(audio_on);
          else:
            subprocess.call(audio_off);
        elif name == 'Fire TV':
          if state:
            subprocess.call(fire_tv_on);
          else:
            subprocess.call(fire_tv_off);
        elif name == 'Raspberry Pi':
          if state:
            subprocess.call(raspberry_pi_on);
          else:
            subprocess.call(raspberry_pi_off);
        else:
          return False;        
        
        return True

