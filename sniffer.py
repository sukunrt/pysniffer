import pcap, dpkt
from construct.protocols.ipstack import ip_stack

def print_packet(pkt_len, data, time_stamp):
    if not data:
        return
    else :
        packet = ip_stack.parse(data)
        print packet
        
p = pcap.pcapObject()
dev = pcap.lookupdev()
p.open_live('wlan0', 1600, 0, 100)

try:
    while 1:
        p.dispatch(1, print_packet)
        

except KeyboardInterrupt:
    print 'shutting down'
