import scapy.all as scapy
import optparse

def user_input():
    # Take the target IP range from the command line.
    parser = optparse.OptionParser()
    parser.add_option("-i","--ip",dest="ip",help="ip address range/CIDR")
    (user_inputs, args) = parser.parse_args()

    if not user_inputs.ip:
        print("Please specify an IP address range")
    else:
        return user_inputs.ip

def scan(ip):
    # Build an ARP request and send it to the broadcast MAC address.
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    # Show the devices that answered the request.
    answered_list.summary()

# Read the user input and start the scan.
ip_address = user_input()
scan(ip_address)
