#Task 1 - Update the Modularized Script
#Step 1-1
#touch /home/ntc/labs/python/configs/snmp.cfg
#cd /home/ntc/labs/python/configs/
#echo snmp-server community networktocode RO >> snmp.cfg
#echo snmp-server community public RO >> snmp.cfg
#echo snmp-server community ntcrw RW >> snmp.cfg
#echo snmp-server community supersecret RW >> snmp.cfg
#echo snmp-server location new_york >> snmp.cfg
#echo snmp-server contact jane_smith >> snmp.cfg

#Step 1-2
#touch /home/ntc/labs/python/lab-19-01.py
from netmiko import ConnectHandler
from getpass import getpass

#Step 2-2
import argparse

def print_logger(message, hostname):
    print(f"{message} | {hostname}")

def connect_to_device(hostname, username, password, device_type):
    print_logger("Connecting to device", hostname)
    device = ConnectHandler(
        host=hostname,
        username=username,
        password=password,
        device_type=device_type,
    )
    return device

def deploy_commands(device, hostname, config_file):
    print_logger("Sending commands from file", hostname)
    device.send_config_from_file(config_file)

def main(device_hostname, username, password, device_type):
    config_file = "./configs/snmp.cfg"

    net_device = connect_to_device(
        device_hostname, username, password, device_type
    )

    deploy_commands(net_device, device_hostname, config_file)

    print_logger("Disconnecting from device", device_hostname)
    net_device.disconnect()

#Step 1-3
device = input("Please enter the hostname or IP: ")
username = input("Please enter the username: ")
device_type = input("Please enter the device type: ")

#Step 1-5,6
password = getpass("Please enter the password: ")
main(device, username, password, device_type)

#Step 1-4
#run: python /home/ntc/labs/python/lab-19-01.py
#input:
# Please enter the hostname or IP: csr1
# Please enter the username: ntc
# Please enter the password: ntc123
# Please enter the device type: cisco_ios
# Connecting to device | csr1
# Sending commands from file | csr1
# Disconnecting from device | csr1

#Step 1-7
#run: python /home/ntc/labs/python/lab-19-01.py
#input:
# Please enter the hostname or IP: csr1
# Please enter the username: ntc
# Please enter the password: 
# Please enter the device type: cisco_ios
# Connecting to device | csr1
# Sending commands from file | csr1
# Disconnecting from device | csr1