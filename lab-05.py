#Task 1 - Explore Basic List Operations
#Step 1-1
mac_list = ['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33', '44:00:00:00:44:44']

#Step 1-2
print(mac_list)
#output: ['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33', '44:00:00:00:44:44']

#Step 1-3
mac_list[3] = mac_list[3].replace(':', '.')

#Step 1-4
print(mac_list)
#output: ['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33', '44.00.00.00.44.44']

#Step 1-5
mac_list.pop()
#removing: '44.00.00.00.44.44'

mac_list
#output: ['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33']

#Step 1-6
mac_list.pop(1)
#removing index 1: '00.00.00.00.22.22'

mac_list
#output: ['00.00.00.00.11.11', '33.00.00.00.33.33']

#Step 1-7
#Insert the value in index of 1
mac_list.insert(1, '00.00.00.00.22.22')

mac_list
#output: ['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33']

#Step 1-8
#Insert the value in index of 2
mac_list.insert(2, '22.22.00.00.00.22')

mac_list
#output: ['00.00.00.00.11.11', '00.00.00.00.22.22', '22.22.00.00.00.22', '33.00.00.00.33.33']

#Step 1-9
#Insert the value from the last index
mac_list.append('55.55.55.55.55.55')
mac_list.append('66.66.66.66.66.66')

print(mac_list)
#output: ['00.00.00.00.11.11', '00.00.00.00.22.22', '22.22.00.00.00.22', '33.00.00.00.33.33', '55.55.55.55.55.55', '66.66.66.66.66.66']

#Task 2 - Build a List of Commands for Network Devices
#Step 2-1
commands = ['interface Eth1/1', 'description configured by Python', 'shutdown']

#Step 2-2
cmd_string = ' ; '.join(commands)

#Step 2-3
print(cmd_string)
#output: interface Eth1/1 ; description configured by Python ; shutdown

#Step 2-4
cmd_string_n = '\n'.join(commands)

#Step 2-5
print(cmd_string_n)
#output:
# interface Eth1/1
# description configured by Python
# shutdown

#Step 2-6
cmd_string_n = '\n '.join(commands)
print(cmd_string_n)
# interface Eth1/1
#  description configured by Python
#  shutdown

#Step 2-7
#Print built-in methods for lists.
dir(list)

#Task 3 - Sort Lists of Similar Objects
#Step 3-1
#Preparing list of string
n7k_linecards = ['N7K-SUP1', 'N7K-M132XP-12', 'N7K-M148GS-11', 'N7K-M148GT-11', 'N7K-F132XP-15', 'N7K-SUP1', 'N7K-M132XP-12', 'N7K-M132XP-12', 'N7K-M148GT-11','N7K-M148GT-11']

#Step 3-2
n7k_linecards.count("N7K-SUP2")
#output: 0
n7k_linecards.count("N7K-SUP1")
#output: 2
n7k_linecards.count("N7K-M132XP-12")
#output: 3

#Step 3-3
vendors = ["cisco", "cisco", "juniper", "cisco", "arista", "juniper"]
vendors.count('cisco')
#output: 3

#Step 3-4
vendors.sort()
vendors
#output: ['arista', 'cisco', 'cisco', 'cisco', 'juniper', 'juniper']

#Step 3-5
vendors.sort(reverse=True)
vendors
#output: ['juniper', 'juniper', 'cisco', 'cisco', 'cisco', 'arista']

