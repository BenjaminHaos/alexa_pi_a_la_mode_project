#!/bin/bash

echo "Toggle Off Script!";

echo standby 0 | cec-client -s -d 1
