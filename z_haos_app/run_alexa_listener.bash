#!/bin/bash

# Wait for pi to boot before running program.
sleep 20;

cd /home/pi/z_haos_app/
python alexa_av_controller.py
