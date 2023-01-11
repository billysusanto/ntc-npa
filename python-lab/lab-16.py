#! /usr/bin/env python
#Modify Lab 13, to removing redundant code.

from netmiko import ConnectHandler

#Create a list of devices which want to backed-up
devices = ["csr1", "csr2"]

for device in devices:
    #Target the host, with loop from devices
    net_device = ConnectHandler(
        host=device, username="ntc", password="ntc123", device_type="cisco_ios"
    )
    #Run command to write running config into startup config
    net_device.send_command("wr mem")

    #Set the terminal to disable terminal length
    net_device.send_command("term len 0")
    #Show the running config
    net_config = net_device.send_command("show run")

    #Write the return value of running config into files
    with open(f"/home/ntc/labs/python/configs/{device}.cfg", "w") as config_file:
        config_file.write(net_config)