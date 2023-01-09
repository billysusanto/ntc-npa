#Task 1 - Use Netmiko in Exec Mode
#Step 1-1
#Check the csr1 with ping: 'ping scr1 -c 3'

#Step 1-2
#Move to cd /home/ntc/files
#run python command

#Step 1-3
#Import the netmiko ConnectHandler function and establish an SSH session to the Cloud Services Router device
from netmiko import ConnectHandler
platform = 'cisco_ios'
host = 'csr1'
username = 'ntc'
password = 'ntc123'
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

#Step 1-4
#See available methods that can be called
dir(device)

#Step 1-5
#Verify the active connection
device.is_alive()
#output: True

#Step 1-6
#Run the single command
output = device.send_command('show version')
print(output)
#output: 
# Cisco IOS XE Software, Version 17.01.01
# ....

#Step 1-7
output = device.send_command('show version | include register')
print(output)
#output: Configuration register is 0x2102

#Step 1-8
'0x2102' in output
#output: True
'0x2142' not in output
#output: True

#Step 1-9
output = device.send_command('wr mem')
print(output)
#output:
# Building configuration...
# [OK]

#Step 1-10
#Run the single command
output = device.send_command('ping 10.0.0.15')
print(output)
#output:
# Type escape sequence to abort.
# Sending 5, 100-byte ICMP Echos to 10.0.0.15, timeout is 2 seconds:
# !!!!!
# Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/9 ms


#Task 2 - Issue Configuration Commands with Netmiko
#Step 2-1
commands = ['interface Loopback100', 'ip address 10.200.1.20 255.255.255.0']

#Step 2-2
output = device.send_config_set(commands)

#Step 2-3
print(output)
#output:
# configure terminal
# Enter configuration commands, one per line.  End with CNTL/Z.
# csr1(config)#interface Loopback100
# csr1(config-if)#ip address 10.200.1.20 255.255.255.0
# csr1(config-if)#end
# csr1#


#Step 2-4
#Run the command as config set with Netmiko
snmp_commands = ['snmp-server community ntclab RO', 'snmp-server community ntcrw RW']
response = device.send_config_set(snmp_commands)
verify = device.send_command('show run | inc snmp-server community')
print(verify)
# snmp-server community ntc-public RO
# snmp-server community ntc-private RW
# snmp-server community ntclab RO
# snmp-server community ntcrw RW


#Step 2-5
#Run the os module to send Linux commands to shell to check the file is exist or not
# import os
# os.system('ls /home/ntc/files/config.txt')
# /home/ntc/files/config.txt
# 0

#Step 2-6
#Inside of the config.txt
# os.system('cat /home/ntc/files/config.txt')
# !
# snmp-server community supersecret RW
# snmp-server community notprivate RO
# !
# interface Loopback101
#  ip address 10.9.88.1 255.255.255.0
# !
# 0

#Step 2-7
#Deploy the command from config file using Netmiko
output = device.send_config_from_file('/home/ntc/files/config.txt')

#Step 2-8
print(output)
#output:
# configure terminal
# Enter configuration commands, one per line.  End with CNTL/Z.
# csr1(config)#!
# csr1(config)#snmp-server community supersecret RW
# csr1(config)#snmp-server community notprivate RO
# csr1(config)#!
# csr1(config)#interface Loopback101
# csr1(config-if)# ip address 10.9.88.1 255.255.255.0
# csr1(config-if)#!
# csr1(config-if)#end
# csr1#


#Task 3 - Use Other Built-in Methods
#Step 3-1
# Entering the Config Mode
device.config_mode()

#Step 3-2
#By default send_command waits for the device "prompt string" to return to what it was. 
# If you're choosing to send non-global config commands using send_command, 
# the prompt will change. 
# Therefore, you should be aware of send_command_timing
data = device.config_mode()
data = device.send_command_timing('interface Gigabit3')

#Step 3-3
#You can always view your prompt string
print(device.find_prompt())
#output: csr1(config-if)#

#Step 3-4
#Exit configuration mode:
device.exit_config_mode()
#output: 'end\r\ncsr1#'

#Step 3-5
#Disconnect from the device
device.disconnect()

#Step 3-6
#Validate the SSH connection
device.is_alive()
#output: False

#Step 3-7
#Re-establish connection back to the device
device.establish_connection()

#Step 3-8
#Finally, disconnect one final time.
device.disconnect()
