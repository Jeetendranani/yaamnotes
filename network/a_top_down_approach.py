"""
computer networking - a top-down approach

chapter 1: computer networks and the internet

    1.1 wht is the internet?
        1.1.1 a nuts and bolts description todo
        1.1.2 a services description
        1.1.3 what is a protocol?

    1.2 the network edge
        1.2.1 access networks
        1.2.2 physical media

    1.3 the network core
        1.3.1 packet switching todo
        1.3.2 circuit switching
        1.3.3 a network of networks

    1.4 delay, loss, and throughput in packet switched network
        1.4.1 overview of delay in packet switch network
        1.4.2 queuing delay and packets loss
        1.4.3 end to end delay
        1.4.4 throughput in computer network

    1.5 protocol layers and there service models
        1.5.1 layered architecture
        1.5.2 encapsulation

    1.6 networks under attach

    1.7 history of computer networking and the internet
        1.7.1 the development of packets switching: 1961 - 1972
        1.7.2 proprietary networks and internetworking: 1972 - 1980
        1.7.3 a proliferation of networks: 1980-1990
        1.7.4 the internet explosion: the 1990s
        1.7.5 the new millennium

    1.8 summary

chapter 2: application layer

    2.1 principles of network applications
        2.1.1 network application architectures
        2.1.2 processes communicating
        2.1.3 transport services available to application
        2.1.4 transport services provided by the internet
        2.1.5 application layer protocols
        2.1.6 network applications covered in this book

    2.2 the web and http
        2.2.1 overview of http
        2.2.2 non-persistent and persistent connections
        2.2.3 http message format
        2.2.4 user-server interaction: cookies
        2.2.5 web caching
        2.2.6 the conditional get

    2.3 file transfer: ftp
        2.3.1 ftp commands and replies

    2.4 Electronic mail in the internet
        2.4.1 smtp
        2.4.2 comparison with http
        2.4.3 email message format
        2.4.4 email access protocols

    2.5 DNS - the internet's directory service
        2.5.1 services provided by dns
        2.5.2 overview of how dns works
        2.5.3 dns records and messages

    2.6 peer-to-peer applications
        2.6.1 p2p file distribution
        2.6.2 distributed hash tables (dhts)

    2.7 socket programming: creating network applications
        2.7.1 socket programming with udp
        2.7.2 socket programming with tcp

    2.8 summary

chapter 3: transport layer

    3.1 introduction and transport layer services
        3.1.1 relationship between transport and network layers
        3.1.2 overview of the transport layer in the internet

    3.2 multiplexing and demultiplexing

    3.3 connectionless transport: udp
        3.3.1 udp segment structure
        3.3.2 udp checksum

    3.4 principles of reliable data transfer
        3.4.1 building a reliable dat transfer protocol
        3.4.2 pipelined reliable data transfer protocols
        3.4.3 go - back - n (gbn)
        3.4.4 selective repeat (sr)

    3.5 connection oriented transport: tcp
        3.5.1 the tcp connection
        3.5.2 tcp segment structure
        3.5.3 round trip time estimation and timeout
        3.5.4 reliable data transfer
        3.5.5 flow control
        3.5.6 tcp connection management

    3.6 principles of congestion control
        3.6.1 the causes and the costs of congestion
        3.6.2 approaches to congestion control
        3.6.3 network-assisted congestion control example: atm abr congestion control

    3.7 tcp congestion control
        3.7.1 fairness

    3.8 summary

chapter 4: network layer

    4.1 introduction
        4.1.1 forwarding and routing
        4.1.2 network service models

    4.2 virtual circuit and datagram network
        4.2.1 virtual circuit network todo
        4.2.2 datagram networks todo
        4.2.3 origins of vc and datagram networks

    4.3 what's inside a router?
        4.3.1 input processing
        4.3.2 switching
        4.3.3 output processing
        4.3.4 where does queueing occur?
        4.3.5 the routing control panel

    4.4 the internet protocol (ip): forwarding and addressing in the internet
        4.4.1 datagram format
        4.4.2 ipv4 addressing
        4.4.3 internet control message protocol (icmp)
        4.4.4 ipv6
        4.4.5 a brief foray into ip security todo

    4.5 routing algorithms
        4.5.1 the link-state (ls) routing algorithm todo
        4.5.2 the distance vector (dv) routing algorithm todo
        4.5.3 hierarchical routing

    4.6 routing in the internet
        4.6.1 intra-as routing in th internet: rip
        4.6.2 intra-as routing in the internet: ospf
        4.6.3 inter-as routing: bgp

    4.7 broadcast and multicast routing
        4.7.1 broadcast routing algorithms
        4.7.2 multicast

    4.8 summary

chapter 5: the link layer: links, access networks, and lans

    5.1 introduction to the link layer
        5.1.1 the services provided by the link layer
        5.1.2. where is the link layer implemented?

    5.2 error-detection and correction techniques
        5.2.1 parity checks
        5.2.2 checksumming methods
        5.2.3 cyclic redundancy check (crc)

    5.3 multiple access links and protocols
        5.3.1 channel partitioning protocols
        5.3.2 random access protocols todo
        5.3.3 taking turns protocols
        5.3.4 docsis: the link layer protocol for cable internet access

    5.4 switched local area networks
        5.4.1 link layer addressing and arp
        5.4.2 ethernet
        5.4.3 link layer switches
        5.4.4 virtual local area networks (vlans)

    5.5 link virtualization: a network as a link layer
        5.5.1 multiprotocol label switching (mpls)

    5.6 data center networking

    5.7 restrospective: a day in the life of a web page request
        5.7.1 getting started: dhcp, udp, ip and ethernet
        5.7.2 still getting started: dns and arp
        5.7.3 still getting started: intra-domain routing to the dns server
        5.7.4 web client-server interaction: tcp and http

    5.8 summary

chapter 6: wireless and mobile networks

    6.1 introduction

    6.2 wireless links and network characteristics
        6.2.1 cdms

    6.3 wifi: 802.11 wireless lans
        6.3.1 the 802.11 architecture
        6.3.2 the 802.11 mac protocol
        6.3.3 the ieee 802.11 frame
        6.3.4 mobility in the same ip subnet
        6.3.5 advanced features in 802.11
        6.3.6 personal area network: bluetooth and zigbee

    6.4 cellular internet access
        6.4.1 an overview of cellular network architecture
        6.4.2 3g cellular data networks: extending the internet to cellular subscribers
        6.4.3 on to 4g: lte

    6.5 mobility management: principles
        6.5.1 addressing
        6.5.2 routing to a mobile node

    6.6 mobile ip

    6.7 managing mobility in cellular networks
        6.7.1 routing calls to a mobile user
        6.7.2 handoffs in gsm

    6.8 wireless and mobility: impact on higher-layer protocols

    6.9 summary

chapter 7 multimedia networking

    7.1 multimedia networking applications
        7.1.1 properties of video
        7.1.2 properties of audio
        7.1.3 types of multimedia network applications

    7.2 streaming stored video
        7.2.1 udp streaming
        7.2.2 http streaming
        7.2.3 adaptive streaming and dash
        7.2.4 content distribution networks
        7.2.5 case studies: netflix, youtube, and kankan

    7.3 vice-over-ip
        7.3.1 limitations of the best-effort ip service
        7.3.2 removing jitter at the receiver for audio
        7.3.3 recovering from packet loss
        7.3.4 case study: voip with skype

    7.4 protocols for real time conversational applications
        7.4.1 rtp
        7.4.2 sip

    7.5 network support for multimedia todo
        7.5.1 dimensioning best effort networks
        7.5.2 providing multiple classes of services
        7.5.3 diffserv
        7.5.4 per-connection quality of services (qos) guarantees: resource reservation and call admission

    7.6 summary

chapter 8: security in computer networks

    8.1 what is network security?

    8.2 principles of cryptography
        8.2.1 symmetric key cryptography
        8.2.2 public key encryption

    8.3 message integrity and digital signatures
        8.3.1 cryptographic hash functions
        8.3.2 message authentication code
        8.3.3 digital signatures

    8.4 end point authentication
        8.4.1 authentication protocol ap1.0
        8.4.2 authentication protocol ap2.0
        8.4.3 authentication protocol ap3.0
        8.4.4 authentication protocol ap3.1
        8.4.5 authentication protocol ap4.0

    8.5 securing email
        8.5.1 secure email
        8.5.2 pgp

    8.6 securing tcp connections: ssl
        8.6.1 teh big picture
        8.6.2 a more complete picture

    8.7 network layer security: ipsec and virtual private network
        8.7.1 ipsec and virtual private network (vpns)
        8.7.2 the ah and esp protocols
        8.7.3 security associations
        8.7.4 the ipsec datagram
        8.7.5 ike: key management in ipsec

    8.8 securing wireless lans
        8.8.1 wired equivalent privacy (wep)
        8.8.2 ieee 802.11i

    8.9 Operational security: firewalls and intrusion detection systems
        8.9.1 firewalls
        8.9.2 intrusion detection system

    8.10 summary

chapter 9: network management

    9.1 what is network management?

    9.2 the infrastructure for network management

    9.3 the internet-standard management framework
        9.3.1 structure of management information: smi
        9.3.2 management information base: mib
        9.3.3 snmp protocol operations and transport mappings
        9.3.4 security and administration

    9.4 asn.1

    9.5 conclusion

"""