import scapy.all as scapy
from scapy.layers import http
import optparse


def user_input():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Specify the interface to scan")
    (options, args) = parser.parse_args()
    return options.interface


def packet_listener(interface):
    scapy.sniff(iface=interface, store=False, prn=analyze_packet)


def analyze_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load())


interface = user_input()
packet_listener(interface)
