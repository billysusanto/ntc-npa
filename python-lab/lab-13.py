from netmiko import ConnectHandler

#Begin to process the CSR1 Backup
csr1 = ConnectHandler(
    host="csr1", username="ntc", password="ntc123", device_type="cisco_ios"
)

#Write the running configuration into startup configuration
csr1.send_command("wr mem")

csr1.send_command("term len 0")
#Show running configuration
csr1_config = csr1.send_command("show run")

#Write the show run command result into a file
with open("/home/ntc/labs/python/configs/csr1.cfg", "w") as config_file:
    config_file.write(csr1_config)


#Begin to process the CSR2 Backup
csr2 = ConnectHandler(
    host="csr2", username="ntc", password="ntc123", device_type="cisco_ios"
)


csr2.send_command("wr mem")
csr2.send_command("term len 0")
csr2_config = csr2.send_command("show run")
with open("/home/ntc/labs/python/configs/csr2.cfg", "w") as config_file:
    config_file.write(csr2_config)