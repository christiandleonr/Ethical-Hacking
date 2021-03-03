import scapy.all as scapy
import optparse


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option('-s', '--subnet', dest='subnet', help='IP ADDRESS / NETWORK MASK')
    parser.add_option('-m', '--mac', dest='mac', help='Target MAC Address')

    options, arguments = parser.parse_args()

    if not options.subnet:
        parser.error('[-] PLease specify a valid subnet, use python network_scanner.py --help for more info.')
    elif not options.mac:
        parser.error('[-] PLease specify a target mac address, use python network_scanner.py --help for more info.')

    return options


def scan(subnet, mac):
    arp_request = scapy.ARP(pdst=subnet)

    broadcast = scapy.Ether(dst=mac)

    arp_broadcast = broadcast/arp_request

    answered = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered:
        client_list.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})

    return client_list


def print_result(client_list):
    print('IP\t\t\tMAC Address\n===================================================')

    for client in client_list:
        print(client['ip'] + '\t\t' + client['mac'])


options = get_arguments()
print_result(scan(options.subnet, options.mac))
