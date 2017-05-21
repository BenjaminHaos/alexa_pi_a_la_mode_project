#!/bin/bash

echo "Television On Script!";

echo on 0 | cec-client -s -d 1
