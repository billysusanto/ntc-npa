#Task 1 - Read Network Configuration F>>>iles
#Step 1-1
#Navigate to some directory

#Step 1-2
# cat vlan_ids.conf
#output: will print what inside the file

#Step 1-3,4
#Open the file
vlan_file = open('vlan_ids.conf', 'r')

#Step 1-5
type(vlan_file)
#output: <class '_io.TextIOWrapper'>

#Step 1-6
dir(vlan_file)
#view built-in methods

#Step 1-7
data = vlan_file.read()

#Step 1-8
print(data)
#output:
# vlan 1
# vlan 2
# vlan 10
# vlan 20
# vlan 50

#Step 1-9
#Close the file
vlan_file.close()

#Task 2 - Write to a Configuration File
#Step 2-1
#Open file with write method
out_file = open('interface.cfg', 'w')

#Step 2-2
out_file.write("interface Eth1\n")
#output: 15
out_file.write(" speed 100\n")
#output: 11
out_file.write(" duplex full\n")
#output: 13

#Step 2-3
#Dont forget to close the file
out_file.close()

#Step 2-4
#Checking the file.. with cat command

#Task 3 - Use a Context Manager
#Step 3-1
with open("interfaces_2.cfg", "w") as out_file:
    out_file.write("interface Eth2\n")
    out_file.write(" speed 10\n")
    out_file.write(" duplex half\n")
#output: 15
#output: 10
#output: 13

#Step 3-2
with open("vlan_ids.conf", "r") as vlan_file:
    data = vlan_file.read()
print(data)
#output: 
# vlan 1
# vlan 2
# vlan 10
# vlan 20
# vlan 50
