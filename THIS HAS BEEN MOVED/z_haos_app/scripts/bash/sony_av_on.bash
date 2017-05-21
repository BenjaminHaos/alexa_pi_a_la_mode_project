#!/bin/bash

echo "Sony AV On Script!";

echo "tx 15:44:6D" | cec-client RPI -s -d 1
