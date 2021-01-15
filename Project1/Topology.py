from mininet.topo import Topo


class GhZeTopo(Topo):

    def __init__(self):
        Topo.__init__(self)
        # create 16 host
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        h11 = self.addHost('h11')
        h12 = self.addHost('h12')
        h13 = self.addHost('h13')
        h14 = self.addHost('h14')
        h15 = self.addHost('h15')
        h16 = self.addHost('h16')

        # Create a 11 switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')

        # Add links between the switches and hosts
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s5, s7)
        self.addLink(s3, s6)
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)
        self.addLink(s6, h8)
        self.addLink(s6, s10)
        self.addLink(s6, h9)
        self.addLink(s8, h5)
        self.addLink(s8, h6)
        self.addLink(s8, h7)
        self.addLink(s8, s9)
        self.addLink(s9, h12)
        self.addLink(s9, h13)
        self.addLink(s9, s10)
        self.addLink(s10, s11)
        self.addLink(s11, h15)
        self.addLink(s11, h16)
        self.addLink(s10, h14)
        self.addLink(s7, h9)
        self.addLink(s7, h10)
        self.addLink(s7, h11)
        self.addLink(s6, h9)

topos = {
    'MyTopo': GhZeTopo
}
