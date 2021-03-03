import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC Address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC Address')

    options, arguments = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use python mac_changer.py --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use python mac_changer.py --help for more info.")

    return options


def change_mac(interface, new_mac):
    print(f'[+] Changing MAC address for {interface} to {new_mac}')

    subprocess.call(f'ifconfig {interface} down', shell=True)
    subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
    subprocess.call(f'ifconfig {interface} up', shell=True)

    print(check_change(interface, new_mac))


def check_change(interface, new_mac):
    ifconfig_result = subprocess.check_output(f'ifconfig {interface}', shell=True)

    changed_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if changed_mac:
        changed_mac = changed_mac.group(0)
    else:
        return '[-] Sorry, this interface has not MAC Address'

    if changed_mac == new_mac:
        return f'[+] The MAC Address was successfully changed to {changed_mac}'
    else:
        return f'[-] The MAC could not be changed, actual MAC Address {changed_mac}, requested MAC Address {new_mac}'


if __name__ == '__main__':
    options = get_arguments()
    change_mac(options.interface, options.new_mac)

# 08:00:27:c2:48:a9
