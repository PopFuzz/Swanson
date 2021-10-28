###script to automate ssh login

import os
import netmiko
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
from getpass import getpass



USERNAME = input('Please enter your SSH username : ')
PASSWORD = getpass('Please enter your SSH password : ')


device = {
    'ip' : '192.168.108.1',
    'username' : USERNAME,
    'password' : PASSWORD,
    'device_type' : 'cisco_ios'
}


try:
  c = ConnectHandler(**device)
  output = c.send_command('show run')
  f = open(f'backup_config','x')
  f.write(output)
  f.close
except (NetMikoTimeoutException):
  print ("The following device has timed out: " + device['ip'])
except (AuthenticationException):
  print ("Authentication failure on: " + device['ip'])
except (SSHException):
  print("Could not connect to the device using SSH protocol.  Check your SSH settings on: " + device['ip'])

print("The script has completed")
