#!/usr/bin/env python
import sys
import time
from probe_hdrs import *

TIME_PROBE = 1

def main():

    probe_pktRLZ = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=8)
    probe_pktLJS = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=4) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=8)
    probe_pktCRR = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=5) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=8)
    probe_pktERE = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=6) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=8)
    probe_pktPAS = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=7) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=8)

    while True:
        try:
            sendp(probe_pktRLZ, iface='eth0')
            sendp(probe_pktLJS, iface='eth0')
            sendp(probe_pktCRR, iface='eth0')
            sendp(probe_pktERE, iface='eth0')
            sendp(probe_pktPAS, iface='eth0')
            time.sleep(TIME_PROBE)
        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    main()
