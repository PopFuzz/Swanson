from netmiko import ConnectHandler
from getpass import get pass

user = input("Enter your Username: ")
secret = getpass("Enter your Password: ")

ciscoDevice = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.9',
    'username': user,
    'password': secret
}

connection = ConnectHandler(**ciscoDevice)