from netmiko import ConnectHandler

#Task 1 - Introduction to Functions
#Step 1-1
#Create file in /home/ntc/labs/python/functions.py

#Step 1-2
#Open text editor

#Step 1-3
#Create a function that return hard-coded list of VLANs
def get_vlans():
    return [1, 5, 10, 20]
vlans = get_vlans()
print(vlans)

#Step 1-4
#Run the script
#output: [1, 5, 10, 20]

#Step 1-5
#Create another function called vlan_exists
def get_vlans():
    return [1, 5, 10, 20]
def vlan_exists(vlan_id):
    return vlan_id in get_vlans()
vlans = get_vlans()
print(vlans)
print(vlan_exists(10))
print(vlan_exists(12))

#Step 1-6
# output: 
# [1, 5, 10, 20]
# True
# False

#Task 2 - Use Functions to Connect to Network Devices
def ez_cisco(hostname, show_command, username="ntc", password="ntc123"):
    platform = "cisco_ios"
    device = ConnectHandler(
        ip=hostname, username=username, password=password, device_type=platform
    )

    output = device.send_command(show_command)
    device.disconnect()

    return output


response = ez_cisco("csr1", "show version")
print(response)

response = ez_cisco("csr2", "show ip int brief")
print(response)

response = ez_cisco("csr3", "show run | inc snmp")
print(response)

