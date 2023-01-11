#Task 1 - Explore Dictionary Syntax
#Step 1-1
#Create a variable called facts and assign it the value of {} that will make it an empty dictionary:
facts = {}

#Step 1-2
type(facts)
#output: <class 'dict'>

#Step 1-3
#Assign string to fact with key 'vendor'
facts['vendor'] = 'cisco'

#Step 1-4
print(facts)
#output: {'vendor': 'cisco'}

#Step 1-5
#return the length of the fact variable
len(facts)
#output: 1

#Step 1-6
#Adding 3 keys with its value
facts['os'] = 'nxos'
facts['version'] = '7.1'
facts['platform'] = 'nexus'
print(facts)
#output: {'os': 'nxos', 'version': '7.1', 'vendor': 'cisco', 'platform': 'nexus'}

#Step 1-7
#Replace the value of 'version'
facts['version'] = "7.3"
facts
#output: {'os': 'nxos', 'version': '7.3', 'vendor': 'cisco', 'platform': 'nexus'}

#Step 1-8
#Creating another dictionary
facts_2 = {'os': 'ios', 'version': '16.6', 'vendor': 'cisco', 'platform': 'catalyst'}

#Step 1-9
#Creating another dictionary
facts_3 = dict(hostname='APAC1', vendor='arista', location='Sydney', model='7050')
facts_3
#output: {'hostname': 'APAC1', 'vendor': 'arista', 'location': 'Sydney', 'model': '7050'}

#Step 1-10
#Creating empty dictionary
facts_4 = dict()
facts_4
#output: {}

#Task 2 - Update and Modify Dictionary Contents
#Step 2-1
#print built-in dictionary methods
dir(facts)

#Step 2-2
print(facts.keys())
#output: dict_keys(['vendor', 'os', 'version', 'platform'])

#Step 2-3
print(facts.values())
#output: dict_values(['cisco', 'nxos', '7.3', 'nexus'])

#Step 2-4
print(facts_2.keys())
#output: dict_keys(['os', 'version', 'vendor', 'platform'])
print(facts_2.values())
#output: dict_values(['ios', '16.6', 'cisco', 'catalyst'])

#Step 2-5
facts_3['hostname']
#output: 'APAC1'

#Step 2-6
print(facts['os'])
#output: nxos

#Step 2-7
try:
    print(facts['os_version'])
except Exception as e: print(e)
#output: 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'os_version'

#Step 2-8
facts.get('os_version')

#Step 2-9
facts.get('os_version', 'ERROR')
#output: 'ERROR'

#Step 2-10
os_ver = facts.get('os_version')
print(os_ver)
#output: None

#Step 2-11
facts_3
#output: {'hostname': 'APAC1', 'vendor': 'arista', 'location': 'Sydney', 'model': '7050'}
facts_3.pop('hostname')
#output: 'APAC1'
facts_3
#output: {'vendor': 'arista', 'location': 'Sydney', 'model': '7050'}

#Step 2-12
facts_3['hostname'] = 'nycr01'
facts_3
#output: {'model': '7050', 'hostname': 'nycr01', 'vendor': 'arista', 'location': 'Sydney'}

#Step 2-13
static_facts = {'customer': 'acme', 'device_type': 'switch'}

#Step 2-14
facts.update(static_facts)
facts_2.update(static_facts)
facts_3.update(static_facts)
facts
#output: {'vendor': 'cisco', 'os': 'nxos', 'version': '7.3', 'platform': 'nexus', 'customer': 'acme', 'device_type': 'switch'}
facts_2
#output: {'os': 'ios', 'version': '16.6', 'vendor': 'cisco', 'platform': 'catalyst', 'customer': 'acme', 'device_type': 'switch'}
facts_3
#output: {'vendor': 'arista', 'location': 'Sydney', 'model': '7050', 'hostname': 'nycr01', 'customer': 'acme', 'device_type': 'switch'}
