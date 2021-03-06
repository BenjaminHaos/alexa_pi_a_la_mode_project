import subprocess
import logging

logging.basicConfig(level=logging.DEBUG);
#logging.basicConfig(level=logging.INFO);
#logging.basicConfig(level=logging.WARNING);
#logging.basicConfig(level=logging.ERROR);
#logging.basicConfig(level=logging.CRITICAL);

from debounce_handler import debounce_handler

app_directory="/home/pi/alexa_pi_a_la_mode_project/z_haos_app";

television_on = app_directory + "/scripts/bash/television_on.bash";
television_off = app_directory + "/scripts/bash/television_off.bash";

stereo_on = app_directory + "/scripts/bash/sony_av_on.bash";
stereo_off = app_directory + "/scripts/bash/sony_av_off.bash";

fire_tv_on = app_directory + "/scripts/bash/fire_tv_on.bash";
fire_tv_off = app_directory + "/scripts/bash/fire_tv_off.bash";

raspberry_pi_on = app_directory + "/scripts/bash/raspberry_pi_on.bash";
raspberry_pi_off = app_directory + "/scripts/bash/raspberry_pi_off.bash";

google_on = app_directory + "/scripts/bash/google_on.bash";
google_off = app_directory + "/scripts/bash/google_off.bash";

surround_sound_on = app_directory + "/scripts/bash/turn_on_surround_sound.bash"
surround_sound_off = app_directory + "/scripts/bash/turn_off_surround_sound.bash"


class device_handler(debounce_handler):
    # Publishes the on/off state requested,
    # and the IP address of the Echo making the request.

    TRIGGERS = {"Television": 52000, "Stereo": 52001, "Fire TV": 52002, "Raspberry Pi": 52003, "Google": 52004, "Surround Sound": 52005}
    
    
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
            subprocess.call(stereo_on);
          else:
            subprocess.call(stereo_off);
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
        elif name == 'Google':
          if state:
            subprocess.call(google_on);
          else:
            subprocess.call(google_off);
        elif name == 'Surround Sound':
          if state:
            subprocess.call(surround_sound_on);
          else:
            subprocess.call(surround_sound_off);
        else:
          return False;        
        
        return True

