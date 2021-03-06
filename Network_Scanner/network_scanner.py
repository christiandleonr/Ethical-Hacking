import scapy.all as scapy
import optparse


def get_arguments():
    # This method get arguments from the console execution
    parser = optparse.OptionParser()

    # Adding options to the OptionParser object
    parser.add_option('-s', '--subnet', dest='subnet', help='IP ADDRESS / NETWORK MASK')
    parser.add_option('-m', '--mac', dest='mac', help='Target MAC Address')

    # Getting the options and arguments from the command line execution
    options, arguments = parser.parse_args()

    # Validating the obtained information
    if not options.subnet:
        parser.error('[-] PLease specify a valid subnet, use python network_scanner.py --help for more info.')
    elif not options.mac:
        parser.error('[-] PLease specify a target mac address, use python network_scanner.py --help for more info.')

    # Returning the options
    return options


def scan(subnet, mac):
    # Create a arp request with de ip and subnet mask to analise
    arp_request = scapy.ARP(pdst=subnet)

    # Create a broadcast mac using the Ether method from Scapy
    # The Ether class is to refer to a Ethernet layer creation (Here we define the MAC Address broadcast)
    broadcast = scapy.Ether(dst=mac)

    # Create de arp broadcast request with the broadcast mac and the arp request created before
    arp_broadcast = broadcast/arp_request

    # Send and Receive Packets or sr(), return an answered and unanswered packets
    # The srp() function do the same that sr function but for layer 2 packets (Ethernet, 802.3, etc.)
    answered = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]

    # Iterate the packets in the answered array and adding them to a list of dictionaries
    client_list = []
    for element in answered:
        client_list.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})

    # Returning list of dictionaries
    return client_list


def print_result(client_list):
    # Printing a header for the IP and MAC Address fields received from the scan methods
    print('IP\t\t\tMAC Address\n===================================================')

    # Printing the values of the IP and MAC Address inside the packets obtained from the scan method
    for client in client_list:
        print(client['ip'] + '\t\t' + client['mac'])


if __name__ == '__main__':
    options = get_arguments()
    print_result(scan(options.subnet, options.mac))
