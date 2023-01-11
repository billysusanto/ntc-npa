from napalm import get_network_driver
import json
driver = get_network_driver('eos')
device = driver('eos-spine1', 'ntc', 'ntc123')

device.open()
device.load_merge_candidate(filename='bgp.conf')
print(device.compare_config())
device.commit_config()

commands = ["show running-config | section bgp"]
print(device.cli(commands))