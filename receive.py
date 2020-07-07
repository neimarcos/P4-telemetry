#!/usr/bin/env python

from probe_hdrs import *

def expand(x):
    yield x
    while x.payload:
        x = x.payload
        yield x

def handle_pkt(pkt):
    if ProbeData in pkt:
        data_layers = [l for l in expand(pkt) if l.name=='ProbeData']
        pkt.show2()
            hexdump(pkt)
        sys.stdout.flush()
    #    print ""
    #    for sw in data_layers:
    #         utilization = 0 if sw.cur_time == sw.last_time else 8.0*sw.byte_cnt/(sw.cur_time - sw.last_time)
    #         tempo = 0 if sw.cur_time == sw.last_time else sw.cur_time - sw.last_time
    #         print "Switch {} - Port {}: {} Mbps - ingress queue {} - ingress queue time {} - egresse queue {} - egresse queue time {} - probe intertime - {}".format(sw.swid, sw.port, utilization,sw.queue_length_in,sw.queue_in_time,sw.queue_length_out,sw.queue_out_time,tempo)
            #print "{};{};{};{};{};{};{};{}".format(sw.swid, sw.port, utilization,sw.queue_length_in,sw.queue_in_time,sw.queue_length_out,sw.queue_out_time,tempo)

def main():
    iface = 'eth0'
    print "sniffing on {}".format(iface)
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
