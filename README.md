# raspiap-keyboard

Put these files inside /etc/tv-keyboard-ctrl/<br>
Create a service to start service-start.sh<br>
Put tv mac address in tv_mac<br>
Put kb mac address in bt_connection_listener.py<br>
Put local subnet in get_ip.sh

# Process
service-start.sh starts bt_connection_listener.py<br>
bt_connection_listener.py waits for bt connection with kb, then starts btctrl.py<br>
btctrl.py sends keypresses to tv using ip found in found_ip<br>
pressing ctrl+f runs get_ip.sh and rereads found_ip<br>
get_ip.sh scans network and prints output to ip_addresses<br>
get_ip.sh runs get_ip<br>
get_ip reads tv_mac, searches for it in ip_addresses, prints it to found_ip<br>
