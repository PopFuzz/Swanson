###script to automate ssh login

import os
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
from datetime import date

USERNAME = input('Please enter your SSH username : ')
PASSWORD = getpass('Pleas enter your SSH password : ')
DATE = date.today().strftime("%Y_%m_%d")

device = {
    'ip' : '192.168.108.10',
    'username' : USERNAME,
    'password' : PASSWORD,
    'device_type' : 'cisco_ios'
}

c = ConnectHandler(**device)

output = c.send_command('show run')

f = open(f'backup_config{DATE}','x')

f.write(output)
f.close