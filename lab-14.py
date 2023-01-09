import json
#Task 1 - Introduction to the IF Statement
#Step 1-1
#Checking the hostname is as we except in conditional block
hostname = "nxos-spine1"
if hostname == "nxos-spine1":
    print("The hostname is correct.")
#output: The hostname is correct.

#Step 1-2
#Preparing a list to be used in conditional,
#Try to find is there a 'catalist' in the platforms list
platforms = ['nexus', 'catalyst', 'asa', 'csr', 'aci']
if 'catalyst' in platforms:
    print("Catalyst has been found in the network.")
#output: Catalyst has been found in the network.

#Step 1-3
#Preparing a list to be used in the loop,
supported_platforms = ['nexus', 'catalyst']
for platform in platforms:
    if platform in supported_platforms:
        print("Platform {}  -- SUPPORTED".format(platform))
#output:
# Platform nexus  -- SUPPORTED
# Platform catalyst  -- SUPPORTED

#Step 1-4
for platform in platforms:
    if platform in supported_platforms:
        print("Platform {}  -- SUPPORTED".format(platform))
    else:
        print("Platform {}  -- NOT SUPPORTED".format(platform))
#output:
# Platform nexus  -- SUPPORTED
# Platform catalyst  -- SUPPORTED
# Platform asa  -- NOT SUPPORTED
# Platform csr  -- NOT SUPPORTED
# Platform aci  -- NOT SUPPORTED

#Step 1-5
vlans = [{'name': 'web', 'id': 10}, {'name': 'app', 'id': 20}, {'name': 'db', 'id': 30}]

#Step 1-6
for item in vlans:
    if item['id'] == 20:
        print("VLAN NAME: {}".format(item['name']))
#output: VLAN NAME: app

#Step 1-7
for item in vlans:
    vlan_id = item['id']
    name = item['name']
    print("vlan {}".format(vlan_id))
    print(" name {}".format(name))
#output:
# vlan 10
#  name web
# vlan 20
#  name app
# vlan 30
#  name db

#Step 1-8
vlans[1].pop('name')
#output: 'app'

#Step 1-9
#Repeat step 6
#Does it work?

#Step 1-10
for item in vlans:
    vlan_id = item['id']
    name = item.get('name')
    print("vlan {}".format(vlan_id))
    if name:
        print(" name {}".format(name))
#output:
# vlan 10
#  name web
# vlan 20
# vlan 30
#  name dbs

#Step 1-11
devices = [{'platform': 'nexus', 'hostname': 'nycr01'}, {'platform': 'catalyst', 'hostname': 'nycsw02'}, {'platform': 'mx', 'hostname': 'nycr03'}, {'platform': 'srx', 'hostname': 'nycfw01'}, {'platform': 'asa', 'hostname': 'nycfw02'}]
print(json.dumps(devices, indent=4))
[
    {
        "platform": "nexus",
        "hostname": "nycr01"
    },
    {
        "platform": "catalyst",
        "hostname": "nycsw02"
    },
    {
        "platform": "mx",
        "hostname": "nycr03"
    },
    {
        "platform": "srx",
        "hostname": "nycfw01"
    },
    {
        "platform": "asa",
        "hostname": "nycfw02"
    }
]

#Step 1-12
for item in devices:
    platform = item.get('platform')
    if platform == "nexus":
        print("Vendor is Cisco")
    elif platform == "catalyst":
        print("Vendor is Cisco")
    elif platform == "aci":
        print("Vendor is Cisco")
    elif platform == "srx" or platform == "mx":
        print("Vendor is Juniper")
    else:
        print("Unknown Vendor")
#output:
# Vendor is Cisco
# Vendor is Cisco
# Vendor is Juniper
# Vendor is Juniper
# Unknown Vendor

#Step 1-13
cisco_platforms = ['catalyst', 'nexus', 'aci']
juniper_platforms = ['mx', 'srx']

for item in devices:
    platform = item.get('platform')
    if platform in cisco_platforms:
        print("Vendor is Cisco")
    elif platform in juniper_platforms:
        print("Vendor is Juniper")
    else:
        print("Unknown Vendor")
#output:
# Vendor is Cisco
# Vendor is Cisco
# Vendor is Juniper
# Vendor is Juniper
# Unknown Vendor