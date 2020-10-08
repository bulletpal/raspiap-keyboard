#!/bin/bash
nmap -sn 10.3.141.0/24 > ip_addresses
./get_ip

cat found_ip
