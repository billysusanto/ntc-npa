#Task 1 - Use the json module
#Step 1-1
#Create a dictionary
facts = {'platform': 'nexus', 'version': '7.3', 'vendor': 'cisco', 'device_type': 'switch', 'os': 'nxos'}

#Step 1-2
print(facts)
#output: {'platform': 'nexus', 'version': '7.3', 'vendor': 'cisco', 'device_type': 'switch', 'os': 'nxos'}
#The larger the dictionary, the harder this will be to read.

#Step 1-3
import json

#Step 1-4
#The larger the dictionary, the harder this will be to read.
print(json.dumps(facts, indent=4))
{
    "platform": "nexus",
    "version": "7.3",
    "vendor": "cisco",
    "device_type": "switch",
    "os": "nxos"
}

#Step 1-5
print(json.dumps(facts, indent=10))
{
          "platform": "nexus",
          "version": "7.3",
          "vendor": "cisco",
          "device_type": "switch",
          "os": "nxos"
}

print(json.dumps(facts, indent=20))
{
                    "platform": "nexus",
                    "version": "7.3",
                    "vendor": "cisco",
                    "device_type": "switch",
                    "os": "nxos"
}

#Task 2 - Use the time module
#Step 2-1
import time

#Step 2-2
#Notice how the interpreter hangs for 5 seconds. 
time.sleep(5)

#Step 2-3
local_time = time.asctime()
print(local_time)
#output: Tue Nov  9 17:20:33 2021

#Task 3 - Use the os module
#Step 3-1
import os

#Step 3-2
#Get working directory
os.getcwd()
#output: '/home/ntc'

#Step 3-3
#Change directory to: ...
os.chdir('/home/ntc/files')
os.getcwd()
#output: '/home/ntc/files'

#Step 3-4
os.getenv('HOME')
#output: '/home/ntc'

#Step 3-5
os.listdir('/home/')
# output omitted (list the contents of a given directory)

#Step 3-6
os.system('date')
#output: Tue Nov  9 17:23:20 UTC 2021
#output: 0

os.system('ifconfig')
# output omitted

