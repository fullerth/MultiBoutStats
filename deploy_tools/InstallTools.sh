#!/bin/bash
set -euo pipefail
IFS=$'\n\n'

#install Firefox
echo Installing Firefox...
sudo apt-get install firefox -y

#install xvfb
sudo apt-get install xvfb -y
