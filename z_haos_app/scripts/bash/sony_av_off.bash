#!/bin/bash

echo "Sony AV Off Script!";

echo "tx 15:44:6C" | cec-client RPI -s -d 1
