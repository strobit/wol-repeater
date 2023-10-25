# wol-repeater
Tiny program to broadcast a directed Wake-on-LAN packet.

It will validate that the given packet is structured as a Wake-on-LAN packet before retransmitting on the given broadcast address.

# Example
python3 server.py <arg1:server ip:this system IP 192.168.1.10> <arg2:broadcast ip:192.168.1.255

python3 server.py 192.168.1.10 192.168.1.255

# Tips
Create a launch.sh:

#!/bin/sh

cd /home/strobe/wol-repeater

sudo python3 wol-repeater.py 192.168.1.10 192.168.1.255

cd /

Then setup a cron job.

sudo crontab -e

Which should contain:

@reboot sleep 20 && sh /path/starter.sh
