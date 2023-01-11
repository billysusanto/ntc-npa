#Task 1 - Evaluate Logical Expressions
#Step 1-1
is_layer3 = True

#Step 1-2
type(is_layer3)
##output: class 'bool'>

#Step 1-3
needs_bgp = False
print(needs_bgp)
##output: False

#Step 1-4
hostname = 'nxos-spine1'
vendor = 'cisco'
interfaces = ['Ethernet2/1', 'Ethernet2/2', 'Ethernet2/3']

#Step 1-5
hostname == 'nxos-spine2'
##output: False
vendor == 'cisco'
##output: True


#Step 1-6
len(interfaces) > 3
##output: False
len(interfaces) != 3
##output: False

#Step 1-7
hostname != 'nxos-spine2'
##output: True

#Step 1-8
'Ethernet2/4' in interfaces
##output: False


#Step 1-9
"Eth" in "Ethernet2/4"
##output: True
"eth" in "Ethernet2/4"
##output: False


#Step 1-10
"eth" in "Ethernet2/4".lower()
##output: True

#Step 1-11
'Ethernet2/2' in interfaces and vendor == 'cisco'
##output: True
True and True and True and False
##output: False
True and True and True
##output: True

#Step 1-12
hostname == "nxos-spine2" or hostname == "nxos-spine10"
##output: False

vendor == "cisco" or hostname == "nxos-spine10"
##output: True

#Task 2 - Convert Other Types to Boolean
#Converting other datatype into boolean
#Step 2-1
hostname = "r1"
bool(hostname)
#output: True
#Why? because hostname is not a empty variable

#Step 2-2
vendor = ""
bool(vendor)
##output: False
#Why? because vendor is an empty string

#Step 2-3
vendors = ['cisco']
bool(vendors)
##output: True
#Why? because vendor is an not an empty list

#Step 2-4
vendors = []
bool(vendors)
##output: False
#Why? because vendor is an empty list
