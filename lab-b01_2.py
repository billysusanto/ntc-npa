import json
from napalm import get_network_driver

ios_driver = get_network_driver('ios')
nxos_driver = get_network_driver('nxos')
eos_driver = get_network_driver('eos')

ios_device = ios_driver('csr1', 'ntc', 'ntc123')
nxos_device = nxos_driver('nxos-spine1', 'ntc', 'ntc123')
eos_device = eos_driver('eos-spine1', 'ntc', 'ntc123')

ios_device.open()
nxos_device.open()
eos_device.open()

print(json.dumps(ios_device.get_facts(), indent=4))