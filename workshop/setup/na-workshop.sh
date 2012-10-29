#!/bin/bash

## Setup script for Norfolk Academy one day workshop

STARS='********'

echo "You must be connected to the Internet for this script to work..."
read -p

echo "Enter a name for your Raspberry Pi:"
read PINAME

## update apt-get and upgrade.
echo "$STARS Updating software packages $STARS"
echo
echo "Performing general upgrade..."
sudo apt-get -yqq update && sudo apt-get -yqq upgrade

echo "Installing extra system packages..."
# Generally good to have
sudo apt-get -yqq install python-pip git wget gcc mingw32 

# Python dev & GPIO (Req'd for LCD and other projects)
sudo apt-get install -yqq python-dev
sudo apt-get install -yqq python-rpi.gpio

# Packages for the internet of things printer
sudo apt-get -yqq install python-serial python-imaging python-unidecode

# Easy file transfer from Macs
sudo apt-get -yqq install netatalk

echo "Installing Python Modules..."
sudo pip -q install tweepy pygame 

echo "Ignoring bad SSL"
#Note: this is only for firewall situations
git config --global http.sslVerify false

echo "Done with Software."

echo "$STARS Updating Network Settings $STARS"
# Automatically set MAC address.  Replace the 0s with a correct MAC and uncomment
# sudo echo "smsc95xx.macaddr=00:22:19:32:61:38" >> /boot/cmdline.txt

echo "Changing Pi hostname from default"
### TODO

echo "Done with Network Settings"

echo "$STARS Updating Display Settings $STARS"

echo "Forcing HDMI hotplug"
sudo sed -i 's@^#hdmi_force_hotplug=1@hdmi_force_hotplug=1@g' /boot/config.txt
echo "Done with Display Settings

echo "$STARS Downloading Project Files $STARS"

echo "Making Project directory called *projects*"
cd ~ && mkdir projects && cd projects

# Printer Code
git clone -q git://github.com/adafruit/Python-Thermal-Printer

# Code-Pi
git clone -q git://github.com/comp-core/code-pi.git

# Adafruit Python Code
git clone -q git://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git

# LCD Code and settines
sudo apt-get install -yqq python-smbus i2c-tools
(sudo cat /etc/modules && echo "ic2-bcm2708" && echo "ic2-dev") > tmp
sudo mv tmp /etc/modules


# Others?
##  Add them here

echo "Cleaning up..."
sudo apt-get -yqq autoremove

