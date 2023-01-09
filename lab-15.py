#Task 1 - Print Data with a For Loop
#Step 1-1
#Preparing a list
commands = ['interface Eth2/1', 'description Configured by Python', 'speed 100', 'duplex full']

#Step 1-2
#Loop through the elements of commands
for command in commands:
    print(command)
#output:
# interface Eth2/1
# description Configured by Python
# speed 100
# duplex full

#Step 1-3
#Another way to do the loop, with item
for item in commands:
    print(item)
#output:
# interface Eth2/1
# description Configured by Python
# speed 100
# duplex full


#Step 1-4
#Create a list of routers and loop through them printing the following status message for each device:
routers = ['csr1', 'csr2', 'csr3']

for router in routers:
    print("Connecting to device | {}".format(router))
#output:
# Connecting to device | csr1
# Connecting to device | csr2
# Connecting to device | csr3


#Step 1-5
#Uppercase the hostname
for router in routers:
    print("Connecting to device | {}".format(router.upper()))
#output:
# Connecting to device | CSR1
# Connecting to device | CSR2
# Connecting to device | CSR3


#Task 2 - Loop over a Dictionary
#Step 2-1
interface = {}
interface['duplex'] = 'full'
interface['speed'] = '100'
interface['description'] = 'Configured by Python'
print(interface)
{'duplex': 'full', 'speed': '100', 'description': 'Configured by Python'}

#Step 2-2
#Print the keys
for key in interface.keys():
    print(key)
#output:
# duplex
# speed
# description


#Step 2-3
#Print the values
for value in interface.values():
    print(value)
#output:
# full
# 100
# Configured by Python

#Step 2-4
#Print the keys and values
for key, value in interface.items():
    print(key, '--->', value)
#output:
# duplex ---> full
# speed ---> 100
# description ---> Configured by Python

#Task 3 - Loop over a List of Dictionaries
#Step 3-1
#Create the Dict
vlan10 = {'name': 'web', 'id': '10'}
vlan20 = {'name': 'app', 'id': '20'}
vlan30 = {'name': 'db', 'id': '30'}

#Step 3-2
#Create the list of VLANs
vlans = [vlan10, vlan20, vlan30]

#Step 3-3
print(vlans)
#output: [{'name': 'web', 'id': '10'}, {'name': 'app', 'id': '20'}, {'name': 'db', 'id': '30'}]


#Step 3-4
import json
print(json.dumps(vlans, indent=4))
#output: 
# [
#     {
#         "name": "web",
#         "id": "10"
#     },
#     {
#         "name": "app",
#         "id": "20"
#     },
#     {
#         "name": "db",
#         "id": "30"
#     }
# ]


#Step 3-5
for vlan in vlans:
    print(vlan)
#output: 
# {'name': 'web', 'id': '10'}
# {'name': 'app', 'id': '20'}
# {'name': 'db', 'id': '30'}


#Step 3-6
for vlan in vlans:
    print(vlan)
    print(type(vlan))
#output: 
# {'name': 'web', 'id': '10'}
# <class 'dict'>
# {'name': 'app', 'id': '20'}
# <class 'dict'>
# {'name': 'db', 'id': '30'}
# <class 'dict'>


#Step 3-7
for vlan in vlans:
    print("vlan {}".format(vlan['id']))
    print(" name {}".format(vlan['name']))
#output: 
# vlan 10
#  name web
# vlan 20
#  name app
# vlan 30
#  name db