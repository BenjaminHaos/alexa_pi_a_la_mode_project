#!/bin/bash

echo "Surround Sound OFF Script!";

echo "tx 15:44:6C" | cec-client RPI -s -d 1
