from time import sleep
from mininet.cli import CLI
from mininet.log import lg, info
from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
from mininet.util import pmonitor

def main():
    lg.setLogLevel( 'info')
    topo = SingleSwitchTopo(4)   
    net = Mininet(topo=topo) 
    
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')

    popens = {}
    p1 = h1.popen('python3 tcp_server.py %s & ' %h1.IP())

    print(h2.cmd('python3 tcp_client.py 1 %s |& tee -a output.log &' %h1.IP()))
    print(h3.cmd('python3 tcp_client.py 2 %s |& tee -a output.log &' %h1.IP()))
    print(h4.cmd('python3 tcp_client.py 3 %s |& tee -a output.log &' %h1.IP()))

    sleep(5)
    p1.terminate()

    h3.cmd('chmod 777 output.log')
    with open('output.log', 'r') as fin:
        print(fin.read())
    
    h3.cmd('sudo rm output.log')

    net.stop()

if __name__ == '__main__':
    main()