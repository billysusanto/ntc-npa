hostname = 'CORESWITCH-A'
type(hostname)
hostname.lower()

#Step 1-4
lower_hostname = hostname.lower()
print(lower_hostname)
lower_hostname

#Step 1-5
interface_config = "interface Eth1\n duplex full\n speed 100"

#Step 1-6
interface_config
print(interface_config)

#Step 1-7
ip_addr = '10.20.5.5'

#Step 1-8
ip_addr.replace('5', '100')

#Step 1-9
ip_addr.replace('5', '100', 1)

#Step 1-10
ip_addr2 = ip_addr.replace('5', '100')
print(ip_addr2)

# Step 1-11
dir(ip_addr2)
dir(str)

#Step 1-12
help(str.upper)
help(str.replace)
help(str.split)

#Step 1-13
octets = ip_addr2.split('.')
print(octets)
print(octets[0])
print(octets[1])
print(octets[2])
print(octets[3])

#Step 1-14
type(octets)

#Step 2-1
interface = 'Ethernet1/10'

#Step 2-2
interface.lstrip('Ethernet')

#Step 2-3
int_id = interface.lstrip('Ethernet')
int_id

#Step 2-4
slot = int_id.split('/')[0]
intf = int_id.split('/')[1]

#Step 2-5
parsed_interface = int_id.split('/')
parsed_interface
slot = parsed_interface[0]
intf = parsed_interface[1]

#Step 2-6
slot.isdigit()
intf.isdigit()

#Step 3-1
speed = '1000'
duplex = 'full'
description = 'Uplink Interface Configured by Python'

#Step 3-2
speed_cmd = 'speed {}'.format(speed)
duplex_cmd = 'duplex {}'.format(duplex)
descr_cmd = 'description {}'.format(description)

#Step 3-3
print(speed_cmd)
print(duplex_cmd)
print(descr_cmd)

#Step 3-4
default_gw = "10.{}.10.1"

#Step 3-5
site_id = "20"

#Step 3-6
default_gw.format(site_id)
'10.20.10.1'

#Step 3-7
site_id = "30"

default_gw.format(site_id)
'10.30.10.1'

#Step 3-8
service_id = "100"
node_id = "1"
mask = "24"

#Step 3-9
default_gw = f"10.{site_id}.{service_id}.{node_id}/{mask}"

default_gw
'10.30.100.1/24'

#Step 3-10
"{} {} {}".format("Hostname", "Location", "Vendor")
"{:12} {:12} {:12}".format("Hostname", "Location", "Vendor")
"{:12} {:12} {:12}".format("nyc-rt01", "New York", "Cisco")
f"{'nyc-rt02':12} {'New York':12} {'Juniper':12}"