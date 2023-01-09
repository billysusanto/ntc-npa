#Task 1 - Nested Dictionary Objects
#Step 1-1
#Create a list of dictionary
facts_list = [{'customer': 'acme', 'vendor': 'arista', 'hostname': 'APAC1', 'location': 'Sydney', 'device_type': 'switch', 'model': '7050', 'os': 'eos'}, {'customer': 'acme', 'vendor': 'juniper', 'hostname': 'EMEA1', 'location': 'London', 'device_type': 'switch', 'model': 'mx', 'os': 'junos'}, {'customer': 'acme', 'vendor': 'cisco', 'hostname': 'nycr01', 'location': 'new_york', 'device_type': 'switch', 'model': 'catalyst', 'os': 'ios'}]

#Step 1-2
import json
print(json.dumps(facts_list, indent=4))
#output: 
# [
#     {
#         "customer": "acme",
#         "vendor": "arista",
#         "hostname": "APAC1",
#         "location": "Sydney",
#         "device_type": "switch",
#         "model": "7050",
#         "os": "eos"
#     },
#     {
#         "customer": "acme",
#         "vendor": "juniper",
#         "hostname": "EMEA1",
#         "location": "London",
#         "device_type": "switch",
#         "model": "mx",
#         "os": "junos"
#     },
#     {
#         "customer": "acme",
#         "vendor": "cisco",
#         "hostname": "nycr01",
#         "location": "new_york",
#         "device_type": "switch",
#         "model": "catalyst",
#         "os": "ios"
#     }
# ]

#Step 1-3
#fasts_list is list or dict? continue to 1-4

#Step 1-4
type(facts_list)
#output: <class 'list'>

#Step 1-5
len(facts_list)
#output: 3

#Step 1-6
#Inside the list, yes its a dict
type(facts_list[0])
#output: <class 'dict'>
#OR
first = facts_list[0]
type(first)
#output: <class 'dict'>

#Step 1-7
print(facts_list[0])
#output: {'customer': 'acme', 'vendor': 'arista', 'hostname': 'APAC1', 'location': 'Sydney', 'device_type': 'switch', 'model': '7050', 'os': 'eos'}

#Step 1-8
print(facts_list[0]['location'])
#output: Sydney

#Step 1-9
neighbor1 = {'neighbor_interface': 'Eth1/2', 'local_interface': 'Eth1/1', 'neighbor': 'R1'}
neighbor2 = {'neighbor_interface': 'Eth1/4', 'local_interface': 'Eth1/2', 'neighbor': 'R2'}

#Step 1-10
#Create a list with neighbor1&2 inside it
neighbors = [neighbor1, neighbor2]

#Step 1-11
print(neighbors)
#output: [{'neighbor_interface': 'Eth1/2', 'local_interface': 'Eth1/1', 'neighbor': 'R1'}, {'neighbor_interface': 'Eth1/4', 'local_interface': 'Eth1/2', 'neighbor': 'R2'}]

print(json.dumps(neighbors, indent=4))
[
    {
        "neighbor_interface": "Eth1/2",
        "local_interface": "Eth1/1",
        "neighbor": "R1"
    },
    {
        "neighbor_interface": "Eth1/4",
        "local_interface": "Eth1/2",
        "neighbor": "R2"
    }
]


#Step 1-12
#Insert a dictionary inside a dictionaty
facts_list[0]['neighbors'] = neighbors

#Step 1-13
print(json.dumps(facts_list, indent=4))
#output: 
# [
#     {
#         "customer": "acme",
#         "vendor": "arista",
#         "hostname": "APAC1",
#         "location": "Sydney",
#         "device_type": "switch",
#         "model": "7050",
#         "os": "eos",
#         "neighbors": [
#             {
#                 "neighbor_interface": "Eth1/2",
#                 "local_interface": "Eth1/1",
#                 "neighbor": "R1"
#             },
#             {
#                 "neighbor_interface": "Eth1/4",
#                 "local_interface": "Eth1/2",
#                 "neighbor": "R2"
#             }
#         ]
#     },
#     {
#         "customer": "acme",
#         "vendor": "juniper",
#         "hostname": "EMEA1",
#         "location": "London",
#         "device_type": "switch",
#         "model": "mx",
#         "os": "junos"
#     },
#     {
#         "customer": "acme",
#         "vendor": "cisco",
#         "hostname": "nycr01",
#         "location": "new_york",
#         "device_type": "switch",
#         "model": "catalyst",
#         "os": "ios"
#     }
# ]

#Step 1-14
print(facts_list[0]['neighbors'][1]['neighbor'])
#output: R2

#Task 2 - Work with a Nested Facts Dictionary Object
#Step 2-1
import json

#Step 2-2
content = {'output': {'ansible_facts': {'fan_info': [{'status': 'Ok', 'model': None, 'hw_ver': '0.0', 'name': 'ChassisFan1'}, {'status': 'None', 'model': None, 'hw_ver': '0.0', 'name': 'ChassisFan2'}, {'status': 'Ok', 'model': '--', 'hw_ver': '--', 'name': 'Fan_in_PS1'}, {'status': 'Failure', 'model': '--', 'hw_ver': '--', 'name': 'Fan_in_PS2'}], 'ansible_net_model': 'NX-OSv Chassis', 'ansible_net_interfaces': {'Ethernet2/13': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/12': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/11': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/10': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/15': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/14': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/1': {'macaddress': '2cc2.604f.feb2', 'state': 'up', 'mode': 'routed', 'duplex': 'full', 'speed': '1000 Mb/s', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}}, 'ansible_net_all_ipv4_addresses': ['10.0.0.71'], 'ansible_net_hostname': 'nxos-spine1', 'hostname': 'nxos-spine1', 'ansible_net_serialnum': 'TM6017D760B', 'interfaces_list': ['mgmt0', 'Ethernet2/1', 'Ethernet2/2', 'Ethernet2/3', 'Ethernet2/4', 'Ethernet2/5', 'Ethernet2/6', 'Ethernet2/7', 'Ethernet2/8', 'Ethernet2/9', 'Ethernet2/10', 'Ethernet2/11', 'Ethernet2/12', 'Ethernet2/13', 'Ethernet2/14', 'Ethernet2/15'], 'ansible_net_gather_subset': ['hardware', 'default', 'interfaces', 'legacy'], 'power_supply_info': [{'status': 'Ok', 'model': 'DS-CAC-845W', 'number': 1}, {'status': 'Absent', 'model': '------------', 'number': 2}], 'platform': 'NX-OSv Chassis', 'ansible_net_version': '7.3(1)D1(1) [build 7.3(1)D1(0.10)]', 'module': [{'status': 'active *', 'model': 'N7K-SUP1', 'type': 'NX-OSv Supervisor Module', 'ports': 0}, {'status': 'ok', 'model': 'N7K-F248XP-25', 'type': 'NX-OSv Ethernet Module', 'ports': 48}, {'status': 'ok', 'model': 'N7K-F248XP-25', 'type': 'NX-OSv Ethernet Module', 'ports': 48}, {'status': 'ok', 'model': 'N7K-F248XP-25', 'type': 'NX-OSv Ethernet Module', 'ports': 48}], 'ansible_net_all_ipv6_addresses': [], 'ansible_net_memtotal_mb': 3908, 'ansible_net_filesystems': ['bootflash:'], 'ansible_net_image': 'bootflash:///titanium-d1.7.3.1.D1.0.10.bin', 'os': '7.3(1)D1(1) [build 7.3(1)D1(0.10)]', 'vlan_list': [1]}}}

#Step 2-3
print(json.dumps(content, indent=4))
#output: {
#     "output": {
#         "ansible_facts": {
#             "fan_info": [
#                 {
#                     "status": "Ok",
#                     "model": null,
#                     "hw_ver": "0.0",
#                     "name": "ChassisFan1"
#                 },
#                 {
#                     "status": "None",
#                     "model": null,
#                     "hw_ver": "0.0",
#                     "name": "ChassisFan2"
#                 },
#                 {
#                     "status": "Ok",
#                     "model": "--",
#                     "hw_ver": "--",
#                     "name": "Fan_in_PS1"
#                 },
#                 {
#                     "status": "Failure",
#                     "model": "--",
#                     "hw_ver": "--",
#                     "name": "Fan_in_PS2"
#                 }
#             ],
#             "ansible_net_model": "NX-OSv Chassis",
#             "ansible_net_interfaces": {
#                 "Ethernet2/13": {
#                     "macaddress": "2cc2.604f.feb2",
#                     "state": "down",
#                     "mode": "routed",
#                     "duplex": "auto",
#                     "speed": "auto-speed",
#                     "type": "Ethernet",
#                     "bandwidth": 1000000,
#                     "mtu": "1500"
#                 },
#                 "Ethernet2/12": {
#                     "macaddress": "2cc2.604f.feb2",
#                     "state": "down",
#                     "mode": "routed",
#                     "duplex": "auto",
#                     "speed": "auto-speed",
#                     "type": "Ethernet",
#                     "bandwidth": 1000000,
#                     "mtu": "1500"
#                 },
#                 "Ethernet2/11": {
#                     "macaddress": "2cc2.604f.feb2",
#                     "state": "down",
#                     "mode": "routed",
#                     "duplex": "auto",
#                     "speed": "auto-speed",
#                     "type": "Ethernet",
#                     "bandwidth": 1000000,
#                     "mtu": "1500"
#                 },
#                 "Ethernet2/10": {
#                     "macaddress": "2cc2.604f.feb2",
#                     "state": "down",
#                     "mode": "routed",
#                     "duplex": "auto",
#                     "speed": "auto-speed",
#                     "type": "Ethernet",
#                     "bandwidth": 1000000,
#                     "mtu": "1500"
#                 },
#                 "Ethernet2/15": {
#                     "macaddress": "2cc2.604f.feb2",
#                     "state": "down",
#                     "mode": "routed",
#                     "duplex": "auto",
#                     "speed": "auto-speed",
#                     "type": "Ethernet",
#                     "bandwidth": 1000000,
#                     "mtu": "1500"
#                 },
#                 "Ethernet2/14": {
#                     "macaddress": "2cc2.604f.feb2",
#                     "state": "down",
#                     "mode": "routed",
#                     "duplex": "auto",
#                     "speed": "auto-speed",
#                     "type": "Ethernet",
#                     "bandwidth": 1000000,
#                     "mtu": "1500"
#                 },
#                 "Ethernet2/1": {
#                     "macaddress": "2cc2.604f.feb2",
#                     "state": "up",
#                     "mode": "routed",
#                     "duplex": "full",
#                     "speed": "1000 Mb/s",
#                     "type": "Ethernet",
#                     "bandwidth": 1000000,
#                     "mtu": "1500"
#                 }
#             },
#             "ansible_net_all_ipv4_addresses": [
#                 "10.0.0.71"
#             ],
#             "ansible_net_hostname": "nxos-spine1",
#             "hostname": "nxos-spine1",
#             "ansible_net_serialnum": "TM6017D760B",
#             "interfaces_list": [
#                 "mgmt0",
#                 "Ethernet2/1",
#                 "Ethernet2/2",
#                 "Ethernet2/3",
#                 "Ethernet2/4",
#                 "Ethernet2/5",
#                 "Ethernet2/6",
#                 "Ethernet2/7",
#                 "Ethernet2/8",
#                 "Ethernet2/9",
#                 "Ethernet2/10",
#                 "Ethernet2/11",
#                 "Ethernet2/12",
#                 "Ethernet2/13",
#                 "Ethernet2/14",
#                 "Ethernet2/15"
#             ],
#             "ansible_net_gather_subset": [
#                 "hardware",
#                 "default",
#                 "interfaces",
#                 "legacy"
#             ],
#             "power_supply_info": [
#                 {
#                     "status": "Ok",
#                     "model": "DS-CAC-845W",
#                     "number": 1
#                 },
#                 {
#                     "status": "Absent",
#                     "model": "------------",
#                     "number": 2
#                 }
#             ],
#             "platform": "NX-OSv Chassis",
#             "ansible_net_version": "7.3(1)D1(1) [build 7.3(1)D1(0.10)]",
#             "module": [
#                 {
#                     "status": "active *",
#                     "model": "N7K-SUP1",
#                     "type": "NX-OSv Supervisor Module",
#                     "ports": 0
#                 },
#                 {
#                     "status": "ok",
#                     "model": "N7K-F248XP-25",
#                     "type": "NX-OSv Ethernet Module",
#                     "ports": 48
#                 },
#                 {
#                     "status": "ok",
#                     "model": "N7K-F248XP-25",
#                     "type": "NX-OSv Ethernet Module",
#                     "ports": 48
#                 },
#                 {
#                     "status": "ok",
#                     "model": "N7K-F248XP-25",
#                     "type": "NX-OSv Ethernet Module",
#                     "ports": 48
#                 }
#             ],
#             "ansible_net_all_ipv6_addresses": [],
#             "ansible_net_memtotal_mb": 3908,
#             "ansible_net_filesystems": [
#                 "bootflash:"
#             ],
#             "ansible_net_image": "bootflash:///titanium-d1.7.3.1.D1.0.10.bin",
#             "os": "7.3(1)D1(1) [build 7.3(1)D1(0.10)]",
#             "vlan_list": [
#                 1
#             ]
#         }
#     }
# }

#Step 2-4


#Step 2-5
len(content)
#output: 1

#Step 2-6
print(content.keys())
#output: dict_keys(['output'])

#Step 2-7
output = content['output']
type(output)
#output: <class 'dict'>
print(output.keys())
#output: dict_keys(['ansible_facts'])

#Step 2-8
print(json.dumps(output, indent=4))
#output: {
#     "ansible_facts": {
#         "fan_info": [
#             {
#                 "status": "Ok",
#                 "model": null,
#                 "hw_ver": "0.0",
#                 "name": "ChassisFan1"
#             },
#             {
#                 "status": "None",
#                 "model": null,
#                 "hw_ver": "0.0",
#                 "name": "ChassisFan2"
#             },
#             {
#                 "status": "Ok",
#                 "model": "--",
#                 "hw_ver": "--",
#                 "name": "Fan_in_PS1"
#             },
#             {
#                 "status": "Failure",
#                 "model": "--",
#                 "hw_ver": "--",
#                 "name": "Fan_in_PS2"
#             }
#         ],
#         "ansible_net_model": "NX-OSv Chassis",
#         "ansible_net_interfaces": {
#             "Ethernet2/13": {
#                 "macaddress": "2cc2.604f.feb2",
#                 "state": "down",
#                 "mode": "routed",
#                 "duplex": "auto",
#                 "speed": "auto-speed",
#                 "type": "Ethernet",
#                 "bandwidth": 1000000,
#                 "mtu": "1500"
#             },
#             "Ethernet2/12": {
#                 "macaddress": "2cc2.604f.feb2",
#                 "state": "down",
#                 "mode": "routed",
#                 "duplex": "auto",
#                 "speed": "auto-speed",
#                 "type": "Ethernet",
#                 "bandwidth": 1000000,
#                 "mtu": "1500"
#             },
#             "Ethernet2/11": {
#                 "macaddress": "2cc2.604f.feb2",
#                 "state": "down",
#                 "mode": "routed",
#                 "duplex": "auto",
#                 "speed": "auto-speed",
#                 "type": "Ethernet",
#                 "bandwidth": 1000000,
#                 "mtu": "1500"
#             },
#             "Ethernet2/10": {
#                 "macaddress": "2cc2.604f.feb2",
#                 "state": "down",
#                 "mode": "routed",
#                 "duplex": "auto",
#                 "speed": "auto-speed",
#                 "type": "Ethernet",
#                 "bandwidth": 1000000,
#                 "mtu": "1500"
#             },
#             "Ethernet2/15": {
#                 "macaddress": "2cc2.604f.feb2",
#                 "state": "down",
#                 "mode": "routed",
#                 "duplex": "auto",
#                 "speed": "auto-speed",
#                 "type": "Ethernet",
#                 "bandwidth": 1000000,
#                 "mtu": "1500"
#             },
#             "Ethernet2/14": {
#                 "macaddress": "2cc2.604f.feb2",
#                 "state": "down",
#                 "mode": "routed",
#                 "duplex": "auto",
#                 "speed": "auto-speed",
#                 "type": "Ethernet",
#                 "bandwidth": 1000000,
#                 "mtu": "1500"
#             },
#             "Ethernet2/1": {
#                 "macaddress": "2cc2.604f.feb2",
#                 "state": "up",
#                 "mode": "routed",
#                 "duplex": "full",
#                 "speed": "1000 Mb/s",
#                 "type": "Ethernet",
#                 "bandwidth": 1000000,
#                 "mtu": "1500"
#             }
#         },
#         "ansible_net_all_ipv4_addresses": [
#             "10.0.0.71"
#         ],
#         "ansible_net_hostname": "nxos-spine1",
#         "hostname": "nxos-spine1",
#         "ansible_net_serialnum": "TM6017D760B",
#         "interfaces_list": [
#             "mgmt0",
#             "Ethernet2/1",
#             "Ethernet2/2",
#             "Ethernet2/3",
#             "Ethernet2/4",
#             "Ethernet2/5",
#             "Ethernet2/6",
#             "Ethernet2/7",
#             "Ethernet2/8",
#             "Ethernet2/9",
#             "Ethernet2/10",
#             "Ethernet2/11",
#             "Ethernet2/12",
#             "Ethernet2/13",
#             "Ethernet2/14",
#             "Ethernet2/15"
#         ],
#         "ansible_net_gather_subset": [
#             "hardware",
#             "default",
#             "interfaces",
#             "legacy"
#         ],
#         "power_supply_info": [
#             {
#                 "status": "Ok",
#                 "model": "DS-CAC-845W",
#                 "number": 1
#             },
#             {
#                 "status": "Absent",
#                 "model": "------------",
#                 "number": 2
#             }
#         ],
#         "platform": "NX-OSv Chassis",
#         "ansible_net_version": "7.3(1)D1(1) [build 7.3(1)D1(0.10)]",
#         "module": [
#             {
#                 "status": "active *",
#                 "model": "N7K-SUP1",
#                 "type": "NX-OSv Supervisor Module",
#                 "ports": 0
#             },
#             {
#                 "status": "ok",
#                 "model": "N7K-F248XP-25",
#                 "type": "NX-OSv Ethernet Module",
#                 "ports": 48
#             },
#             {
#                 "status": "ok",
#                 "model": "N7K-F248XP-25",
#                 "type": "NX-OSv Ethernet Module",
#                 "ports": 48
#             },
#             {
#                 "status": "ok",
#                 "model": "N7K-F248XP-25",
#                 "type": "NX-OSv Ethernet Module",
#                 "ports": 48
#             }
#         ],
#         "ansible_net_all_ipv6_addresses": [],
#         "ansible_net_memtotal_mb": 3908,
#         "ansible_net_filesystems": [
#             "bootflash:"
#         ],
#         "ansible_net_image": "bootflash:///titanium-d1.7.3.1.D1.0.10.bin",
#         "os": "7.3(1)D1(1) [build 7.3(1)D1(0.10)]",
#         "vlan_list": [
#             1
#         ]
#     }
# }

#Step 2-9
print(json.dumps(output['ansible_facts']['fan_info'], indent=4))
#output: 
# [
#     {
#         "status": "Ok",
#         "model": null,
#         "hw_ver": "0.0",
#         "name": "ChassisFan1"
#     },
#     {
#         "status": "None",
#         "model": null,
#         "hw_ver": "0.0",
#         "name": "ChassisFan2"
#     },
#     {
#         "status": "Ok",
#         "model": "--",
#         "hw_ver": "--",
#         "name": "Fan_in_PS1"
#     },
#     {
#         "status": "Failure",
#         "model": "--",
#         "hw_ver": "--",
#         "name": "Fan_in_PS2"
#     }
# ]

#Step 2-10
print(type(output['ansible_facts']['fan_info']))
#output: <class 'list'>


#Step 2-11
print(json.dumps(output['ansible_facts']['fan_info'][1], indent=4))
#output:{} 
#     "status": "None",
#     "model": null,
#     "hw_ver": "0.0",
#     "name": "ChassisFan2"
# }


#Step 2-12
fan_name = output['ansible_facts']['fan_info'][1]['name']
print(fan_name)
#output: ChassisFan2

#Step 2-13 - Challenge!


#Step 2-14 - Challenge!


#Task 3 - Handle VLAN Objects
#Step 3-1
vlans = {
    "output": {
        "proposed": {
            "name": "NTC"
        },
        "existing_vlans_list": [
            "1"
        ],
        "end_state_vlans_list": [
            "1",
            "100"
        ],
        "existing": {},
        "updates": [
            "vlan 100",
            "name NTC",
            "exit"
        ],
        "end_state": {
            "vlan_state": "active",
            "mapped_vni": "",
            "admin_state": "up",
            "name": "NTC",
            "vlan_id": "100"
        },
        "proposed_vlans_list": [
            "100"
        ]
    }
}

#Step 3-2
existing_vlans = vlans['output']['existing_vlans_list']
proposed_vlans = vlans['output']['proposed_vlans_list']

#Step 3-3
print(existing_vlans)
#output: ['1']
print(proposed_vlans)
#output: ['100']

#Step 3-4
end_state_vlans = existing_vlans + proposed_vlans
print(end_state_vlans)
#output: ['1', '100']

#Step 3-5
end_state_vlans == vlans['output']['end_state_vlans_list']
#output: True

#Step 3-6
print(vlans['output']['updates'][2])
print(vlans['output']['updates'][-1])
