#/bin/bash
echo "ros" |sudo -S apt-get install python-pip&&libzbar0
pip install --user --upgrade pip
echo "ros" |sudo -S pip install --user baidu-aip
pip install --user pyserial
echo "ros" |sudo -S pip install --user pyzbar
echo "ros" |sudo apt-get install sox
echo "ros" |sudo apt-get install sox libsox-fmt-all

