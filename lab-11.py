#Task 1 - Hello Network Automation
#Step 1-1
#Create a directory: mkdir -p /home/ntc/labs/python

#Step 1-2
#Move into the newly created directory: cd /home/ntc/labs/python

#Step 1-3
#Create a file with touch command: touch networkauto.py

#Step 1-4
#SSH to the machine and edit the file

#Step 1-5
#Inside the networkauto.py, add the following code: print('Hello Network Automation!')

#Step 1-6
#Run the python

#Task 2 - Print Data from a Script
#Step 2-1


#Step 2-2
import json
facts1 = {'vendor': 'cisco', 'os': 'nxos', 'ipaddr': '10.1.1.1'}
facts2 = {'vendor': 'cisco', 'os': 'ios', 'ipaddr': '10.2.1.1'}
facts3 = {'vendor': 'arista', 'os': 'eos', 'ipaddr': '10.1.1.2'}
devices = [facts1, facts2, facts3]
print(json.dumps(devices, indent=4))

#Step 2-3
#Run the print_facts.py
#output:
# [
#     {
#         "vendor": "cisco",
#         "os": "nxos",
#         "ipaddr": "10.1.1.1"
#     },
#     {
#         "vendor": "cisco",
#         "os": "ios",
#         "ipaddr": "10.2.1.1"
#     },
#     {
#         "vendor": "arista",
#         "os": "eos",
#         "ipaddr": "10.1.1.2"
#     }
# ]