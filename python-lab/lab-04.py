#Step 1-1
#Create variable and assign the value of 10
vlan_id = 10

#Step 1-2
#Check the datatype
type(vlan_id)
#output: <class 'int'>

#Step 1-3
dir(vlan_id)
#output will print all built-in methods for Integers

#Step 1-4
#Create a variable and assign the value of 100 with quotes
vid = "100"

#Step 1-5
#We cannot tell what datatype when we print the value of the variable
print(vlan_id)
#output: 10
print(vid)
#output: 100

#Step 1-6
#Print again without print statement
vlan_id
#output: 10
vid
#output: '100'

#Step 1-7
#Creata and assign variable
ipaddr = "10.2.9.1"
mask = 24

#Step 1-8
#Trying to concanate
ipaddr + "/" + mask
#And we will get error: TypeError: can only concatenate str (not "int") to str

#Step 1-9
#To do that, we need to convert the integer into string first
ipaddr + "/" + str(mask)

#Step 1-10
type(vlan_id)
#output: <class 'int'>

vlan_id_string = str(vlan_id)

type(vlan_id_string)
#output: <class 'str'>