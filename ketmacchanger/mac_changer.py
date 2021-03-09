import subprocess
import optparse
import re

class MACChanger:
    def __init__(self, interface, new_mac):
        # Constructor method
        self.interface = interface
        self.new_mac = new_mac

    
    def set_change_values(self, interface, new_mac):
        # Method to change the values of the class variables to not have to create a new object
        self.interface = interface
        self.new_mac = new_mac


    def change_mac(self):
        # Printing the old MAC and the new MAC
        print(f'[+] Changing MAC address for {self.interface} to {self.new_mac}')

        # Commands to change the MAC Address
        subprocess.call(f'ifconfig {self.interface} down', shell=True)
        subprocess.call(f'ifconfig {self.interface} hw ether {self.new_mac}', shell=True)
        subprocess.call(f'ifconfig {self.interface} up', shell=True)

        # Printing the result of the check_change method
        print(self.check_change())


    def check_change(self):
        # Using the check_output method to get the information of the command executed
        ifconfig_result = subprocess.check_output(f'ifconfig {self.interface}', shell=True)

        # Using the result of check_output method to find the MAC Address of the interface
        changed_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

        # Validating if the MAC Address exist inside the interface that we are looking for
        if changed_mac:
            changed_mac = changed_mac.group(0)
        else:
            return '[-] Sorry, this interface has not MAC Address'

        # Validating if the MAC get from the command ifconfig is the same than the new MAC
        if changed_mac == self.new_mac:
            return f'[+] The MAC Address was successfully changed to {changed_mac}'
        else:
            return f'[-] The MAC could not be changed, actual MAC Address {changed_mac}, requested MAC Address {self.new_mac}'


if __name__ == '__main__':
    mc = MACChanger('eth0', '11:22:33:44:55:66')
    mc.change_mac()

# 08:00:27:c2:48:a9
