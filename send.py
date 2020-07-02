#!/usr/bin/env python
import sys
import time
from probe_hdrs import *

TIME = 1

def main():

    probe_pkt = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=5) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=6) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=7) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=3) / \
                ProbeFwd(egress_spec=1)

    while True:
        try:
            sendp(probe_pkt, iface='eth0')
            time.sleep(PROBE_TIME)
        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    main()
