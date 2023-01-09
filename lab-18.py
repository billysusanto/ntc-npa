#Task 1 - Modularize the Backup Script
#! /usr/bin/env python

from netmiko import ConnectHandler

def connect_to_device(hostname):
    print(f"Connecting to device | {hostname}")
    #Create connection to device
    device = ConnectHandler(
        host=hostname, username="ntc", password="ntc123", device_type="cisco_ios"
    )
    return device

def save_config(device, hostname):
    print(f"Saving configuration | {hostname}")
    #Run the command to write running config to startup config
    device.send_command("wr mem")

def backup_config(device, hostname):
    print(f"Backing up configuration | {hostname}")
    device.send_command("term len 0")
    config = device.send_command("show run")
    #Returning the result of device running configuration
    return config

def write_to_file(hostname, show_run):
    print(f"Writing config to file | {hostname}\n")
    backup_path = "/home/ntc/labs/python/configs"
    #Write the method param into file
    with open(f"{backup_path}/{hostname}.cfg", "w") as config_file:
        config_file.write(show_run)

def main():
    devices = ["csr1", "csr2", "csr3"]

    for device_hostname in devices:
        net_device = connect_to_device(device_hostname)
        #write running to startup config
        save_config(net_device, device_hostname)
        #store the return message from running config into variable
        net_config = backup_config(net_device, device_hostname)
        #pass the variable with running config result into write to file function
        write_to_file(device_hostname, net_config)
        #done, disconnect from the device
        net_device.disconnect()

main()