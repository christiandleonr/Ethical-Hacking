import scapy.all as scapy

class NetworkScanner:
    def __init__(self, subnet, mac):
        # Constructor method, creating class variables and assigning the parameters to them
        self.subnet = subnet
        self.mac = mac
        self.client_list = []


    def change_scan_values(self, subnet, mac):
        # Method to change the class variables and don't have to create a new object
        self.subnet = subnet
        self.mac = mac


    def scan(self):
        # Create a arp request with de ip and subnet mask to analise
        arp_request = scapy.ARP(pdst=self.subnet)

        # Create a broadcast mac using the Ether method from Scapy
        # The Ether class is to refer to a Ethernet layer creation (Here we define the MAC Address broadcast)
        broadcast = scapy.Ether(dst=self.mac)

        # Create de arp broadcast request with the broadcast mac and the arp request created before
        arp_broadcast = broadcast/arp_request

        # Send and Receive Packets or sr(), return an answered and unanswered packets
        # The srp() function do the same that sr function but for layer 2 packets (Ethernet, 802.3, etc.)
        answered = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]

        # Iterate the packets in the answered array and adding them to a list of dictionaries
        self.client_list = []
        for element in answered:
            self.client_list.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})

        # Returning list of dictionaries
        return self.client_list


    def print_result(self):
        # Printing a header for the IP and MAC Address fields received from the scan methods
        print('IP\t\t\tMAC Address\n===================================================')

        # Printing the values of the IP and MAC Address inside the packets obtained from the scan method
        for client in self.client_list:
            print(client['ip'] + '\t\t' + client['mac'])


if __name__ == '__main__':
    ns = NetworkScanner('10.0.2.1/24', 'ff:ff:ff:ff:ff:ff')
    ns.scan()
    ns.print_result()
