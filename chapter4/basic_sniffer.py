
import sys
orig_stdout=sys.stdout
from scapy.all import *
from scapy.layers.http import HTTPRequest # import HTTP packet
from colorama import init, Fore
sys.stdout=orig_stdout

# initialize colorama
init()
# define colors
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

def sniff_packets(iface=None):
    """
    Sniff packets on port 80 with iface if None then
    use the default interface
    """
    if iface:
        # port 80 for http
        # process_packet is the callback function
        sniff(filter="port 80", prn=process_packet, iface=iface, store=False)
    else:
        # sniff with default interface
        sniff(iface='\\Device\\NPF_Loopback',filter="port 80", prn=process_packet, store=False)

def process_packet(packet):
    """
    this is the callback function for sniffing
    """
    if packet.haslayer(HTTPRequest):
        # if the packet is a HTTP reequest
        # get the URI requested
        url = packet([HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode())
        # get the requested IP address
        ip = packet[IP].src
        # get the method requested
        method = packet[HTTPRequest].Method.decode()
        print(f"\n{GREEN}[+] {ip} Requested {url} with {method}{RESET}")
        if show_raw and packet.haslayer(Raw) and method == "POST":
            # if show_raw flag is enabled, has raw data, and the
            # requested method is POST
            print(f"\n{RED}[*] Some useful Raw data: {packet[Raw].load}{RESET}")


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description="HTTP Packet Sniffer, \
    this is useful when you are man in the middle")
    parser.add_argument("-i", "--iface", help="Interface to use, or default")
    parser.add_argument("--show-raw", dest="show_raw", action="store_true", help="you want to store or show raw")
    # parse the arguments
    args = parser.parse_args()
    iface = args.iface
    show_raw = args.show_raw
    sniff_packets(iface)
