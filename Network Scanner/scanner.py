import scapy.all as scapy

arp_request_packet = scapy.ARP(pdst="192.168.29.0/24")
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
combined_packet = broadcast_packet / arp_request_packet
print(scapy.srp(combined_packet, timeout=1))