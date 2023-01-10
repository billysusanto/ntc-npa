#Step 2-2
import argparse
from netmiko import ConnectHandler
from getpass import getpass

def print_logger(message, hostname):
    print(f"{message} | {hostname}")

def connect_to_device(hostname, username, password, device_type):
    print_logger("Connecting to device", hostname)
    device = ConnectHandler(
        host=hostname,
        username=username,
        password=password,
        device_type=device_type,
    )
    return device

def deploy_commands(device, hostname, config_file):
    print_logger("Sending commands from file", hostname)
    device.send_config_from_file(config_file)


def main(device_hostname, username, password, device_type):
    config_file = "./configs/snmp.cfg"

    net_device = connect_to_device(
        device_hostname, username, password, device_type
    )

    deploy_commands(net_device, device_hostname, config_file)

    print_logger("Disconnecting from device", device_hostname)
    net_device.disconnect()

#Step 2-3
#Prepare the argumen parser
parser = argparse.ArgumentParser(description="Deploy configuration to a device")
parser.add_argument(
    "-i",
    "--ip",
    help="Enter the IP address or hostname of the device",
    required=True,
)
parser.add_argument(
    "-d", "--device_type", help="Enter the device type", required=True
)
parser.add_argument(
    "-u", "--username", help="Enter the username", required=True
)
parser.add_argument(
    "-p", "--password", help="Enter the password", required=True
)

# Parse the argument
args = parser.parse_args()

#Set into the variable
device = args.ip
username = args.username
password = args.password
device_type = args.device_type

#Run the Netmiko
main(device, username, password, device_type)

#RUN
# python lab-19-02.py -i csr1 -d cisco_ios -u ntc -p ntc123Connecting to device | csr1