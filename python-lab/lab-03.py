#Step 1-1
#Set value on the variable
hostname = 'CORESWITCH-A'

#Step 1-2
#Print the data type of the variable
type(hostname)

#Step 1-3
#Convert the value of the string into lowercase
hostname.lower()

#Step 1-4
#Passing the value after lowering the value into new variable
lower_hostname = hostname.lower()
#Print the new variable
print(lower_hostname)
#output: coreswitch-a
lower_hostname
#output: 'coreswitch-a'

#Step 1-5
interface_config = "interface Eth1\n duplex full\n speed 100"
#adding newline with render escape characters \n

#Step 1-6
interface_config
#output: 'interface Eth1\n duplex full\n speed 100'
print(interface_config)
#output: 
#interface Eth1
# duplex full
# speed 100

#Step 1-7
ip_addr = '10.20.5.5'

#Step 1-8
ip_addr.replace('5', '100')
#the ouput after replace should be 10.20.100.100

#Step 1-9
ip_addr.replace('5', '100', 1)
#the output after replace should be 10.20.100.5

#Step 1-10
ip_addr2 = ip_addr.replace('5', '100')
print(ip_addr2)

# Step 1-11
#Use dir for print the build-in method of the datatype
dir(ip_addr2)
dir(str)

#Step 1-12
#Allow you to learn how to use a given method
help(str.upper)
help(str.replace)
help(str.split)

#Step 1-13
octets = ip_addr2.split('.')
print(octets)
#output: ['10', '20', '100', '100']
print(octets[0])
#output: 10
print(octets[1])
#output: 20
print(octets[2])
print(octets[3])

#Step 1-14
type(octets)
#output: <class 'list'>

#Step 2-1
interface = 'Ethernet1/10'

#Step 2-2
interface.lstrip('Ethernet')

#Step 2-3
int_id = interface.lstrip('Ethernet')
int_id
#output: '1/10'

#Step 2-4
slot = int_id.split('/')[0]
intf = int_id.split('/')[1]

#Step 2-5
parsed_interface = int_id.split('/')
parsed_interface
#output: ['1', '10']
slot = parsed_interface[0]
#slot = 1
intf = parsed_interface[1]
#intf = 10

#Step 2-6
slot.isdigit() #True
intf.isdigit() #True

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
#output: speed 1000
print(duplex_cmd)
#output: duplex full
print(descr_cmd)
#output: description Uplink Interface Configured by Python

#Step 3-4
default_gw = "10.{}.10.1"

#Step 3-5
site_id = "20"

#Step 3-6
default_gw.format(site_id)
#output: '10.20.10.1'

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
#output: '10.30.100.1/24'

#Step 3-10
"{} {} {}".format("Hostname", "Location", "Vendor")
#output: 'Hostname Location Vendor'
"{:12} {:12} {:12}".format("Hostname", "Location", "Vendor")
#output: 'Hostname     Location     Vendor      '
"{:12} {:12} {:12}".format("nyc-rt01", "New York", "Cisco")
#output: 'nyc-rt01     New York     Cisco       '
f"{'nyc-rt02':12} {'New York':12} {'Juniper':12}"
#output: 'nyc-rt02     New York     Juniper     '