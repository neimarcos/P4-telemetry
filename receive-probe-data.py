#!/usr/bin/env python
import sys
from probe_hdrs import *
import matplotlib.pyplot as plt

ContadorX=0
ContadorY=0
S1_Link1_Queue_OUT= range(10)
S1_Link1_queue_time= range(10)
S1_Link2_Queue_OUT= range(10)
S1_Link2_queue_time= range(10)

def expand(x):
    yield x
    while x.payload:
        x = x.payload
        yield x

def gera_grafico(Link1,Link2,Nome,titulo):

    # Declaring the points for first line plot
    X1 = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0]
    Y1 = Link1

    # Setting the figure size
    fig = plt.figure(figsize=(6,3))

    # plotting the first plot
    plt.plot(X1, Y1, label = "S1 -> S3")

    # Declaring the points for second line plot
    X2 = [-9,-8,-7,-6,-5,-4,-3,-2,-1, 0]
    Y2 = Link2

    # plotting the second plot
    plt.plot(X2, Y2, label = "S3 -> S1")

    # Labeling the X-axis
    plt.xlabel('Probe')

    # Labeling the Y-axis
    plt.ylabel('Queue')

    # Give a title to the graph
    plt.title(titulo)

    # Show a legend on the plot
    plt.legend()

    #Saving the plot as an image
    fig.savefig(Nome, bbox_inches='tight', dpi=150)


def handle_pkt(pkt):
    global ContadorX,S1_Link1_Queue_OUT,ContadorY,S1_Link2_Queue_OUT,S1_Link1_queue_time,S1_Link2_queue_time

    if ProbeData in pkt:
        data_layers = [l for l in expand(pkt) if l.name=='ProbeData']
        #    print ""
        for sw in data_layers:
            utilization = 0 if sw.cur_time == sw.last_time else 8.0*sw.byte_cnt/(sw.cur_time - sw.last_time)
            #
            tempo = 0 if sw.cur_time == sw.last_time else sw.cur_time - sw.last_time
            print "Switch {} - Port {}: {} Mbps - ingress queue {} - ingress queue time {} - egresse queue {} - egresse queue time {} - probe intertime - {}".format(sw.swid, sw.port, utilization,sw.queue_length_in,sw.queue_in_time,sw.queue_length_out,sw.queue_out_time,tempo)
            if (sw.swid==1) and (sw.port==3):
                #print "ContadorX {} - {}".format(ContadorX,sw.queue_length_out)
                S1_Link1_Queue_OUT[ContadorX]= sw.queue_length_out
                S1_Link1_queue_time[ContadorX]= sw.queue_out_time
                ContadorX+=1
                if (ContadorX == 10):
                    ContadorX=0
                    gera_grafico(S1_Link1_Queue_OUT,S1_Link2_Queue_OUT,"SW1-Queue.jpg","Queue Size in Packet")
                    gera_grafico(S1_Link1_queue_time,S1_Link2_queue_time,"SW1-Queue-time.jpg","Time packet em queue")
            if (sw.swid==3) and (sw.port==3):
                #print "ContadorY {} - {}".format(ContadorY,sw.queue_length_out)
                S1_Link2_Queue_OUT[ContadorY]= sw.queue_length_out
                S1_Link1_queue_time[ContadorX]= sw.queue_out_time
                ContadorY+=1
                if (ContadorY == 10):
                    ContadorY=0
                    gera_grafico(S1_Link1_Queue_OUT,S1_Link2_Queue_OUT,"SW1-Queue.jpg","Queue Size in Packet")
                    gera_grafico(S1_Link1_queue_time,S1_Link2_queue_time,"SW1-Queue-time.jpg","Time packet em queue")

def main():
    ContadorX=0
    ContadorY=0
    iface = 'eth0'
    print "sniffing on {}".format(iface)
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
