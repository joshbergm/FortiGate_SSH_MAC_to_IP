# -----------------------------------------------------------
# Retrieve IP from ARP table based on MAC address
# Joshua Bergman @ 2021
# -----------------------------------------------------------

# Connect to device containing ARP table
from netmiko import ConnectHandler
import time

fw = {
    'device_type': 'fortinet',
    'host':   '<IP>',
    'username': '<username>',
    'password': '<password>',
    'port': 22,
}

net_connect = ConnectHandler(**fw)
print('Connection successful!')

# Check file for MAC addresses
mac_address = open('D:/mac_address_list.txt', 'r')
while True:
    line = mac_address.readline()

    if not line:
        break

    output = net_connect.send_command('get sys arp | grep -f ' + line.strip())
    print(output)
    ip_address = open('D:/ip_address_output.txt', 'a')
    ip_address.writelines(output)
    time.sleep(0.2)
mac_address.close()

# Disconnect session
net_connect.disconnect()

# Status
print("Done")
