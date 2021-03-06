"""
computer network

1. introduction

    1.1 uses of computer networks
        1.1.1 business applications
        1.1.2 home applications
        1.1.3 mobile users
        1.1.4. social issues

    1.2. network hardware
        1.2.1 personal area networks
        1.2.2 local area networks
        1.2.3 metropolitan area networks todo
        1.2.4 wide area networks
        1.2.5 internetworks

    1.3 network software
        1.3.1 protocol hierarchies
        1.3.2 design issues for the layers todo
        1.3.3 connection oriented versus connectionless service todo
        1.3.4 service primitives
        1.3.5 the relationship of services to protocols

    1.4. reference models
        1.4.1 the osi reference model
        1.4.2 the tcp/ip reference model
        1.4.3 the model used in this book
        1.4.4 a comparison of the osi and tcp/ip reference models
        1.4.5 a critique of the osi model and protocols
        1.4.6 a critique of the tcp/ip reference model

    1.5 example networks
        1.5.1 the internet
        1.5.2 third generation mobile phone networks
        1.5.3 wireless lans
        1.5.4 frid and sensor networks

    1.6 network standardization
        1.6.1 who's who in the telecommunications world
        1.6.2 who's who in the international standards world
        1.6.3 who's who in the internet standards world

    1.7 metric unites

    1.8 outline of the rest of the book

    1.9 summary

2. the physical layer

    2.1 the theoretical basis for data communication
        2.1.1 fourier analysis
        2.1.2 bandwidth limited signals
        2.1.3 the maximum data rate of a channel

    2.2 guided transmission media
        2.2.1 magnetic media
        2.2.2 twisted pairs
        2.2.3 coaxial cable
        2.2.4 power lines
        2.2.5 fiber optics

    2.3 wireless transmission
        2.3.1 the electromagnetic spectrum todo
        2.3.2 radio transmission
        2.3.3 microwave transmission
        2.3.4 infrared transmission todo
        2.3.5 light transmission

    2.4 communication satellites
        2.4.1 geostationary satellites
        2.4.2 medium-earth orbit satellites todo
        2.4.3 low-earth orbit satellites
        2.4.4 satellites versus fiber

    2.5 digital modulation and multiplexing todo
        2.5.1 baseband transmission
        2.5.2 passband transmission
        2.5.3 frequency division multiplexing
        2.5.4 time division multiplexing
        2.5.5 code division multiplexing

    2.6 the public switched telephone network
        2.6.1 structure of the telephone system
        2.6.2 the politics of telephones
        2.6.3 the local loop: modems, adsl, and fiber
        2.6.4 trunks and multiplexing
        2.6.5 switching

    2.7 the mobile telephone system
        2.7.1 first generation (coco 1g) mobile phones: analog voice
        2.7.2 second generation (2g) mobile phone: digital voice
        2.7.3 third generation (3g) mobile phones digital voice and data

    2.8 cable television
        2.8.1 community antenna television todo
        2.8.2 internet over cable
        2.8.3 spectrum allocation todo
        2.8.4 cable modems
        2.8.5 adsl versus cable

    2.9 summary

3. the data link layer

    3.1 data lin layer design issues
        3.1.1 services provided to the network layer
        3.1.2 framing
        3.1.3 error control
        3.1.4 flow control

    3.2 error detection and correction
        3.2.1 error correcting codes
        3.2.2 error detecting codes

    3.3 elementary data link protocols
        3.3.1 a utopian simplex protocol
        3.3.2 a simplex stop-and-wait protocol for an error free channel
        3.3.3 a simplex stop and wait protocol for a noisy channel

    3.4 sliding window protocols
        3.4.1 a one-bit sliding window protocol
        3.4.2 a protocol using go back n
        3.4.3 a protocol using selective request

    3.5 example data link protocols
        3.5.1 packet over sonet todo
        3.5.2 adsl (asymmetric digital subscriber loop)

    3.6 summary

4. the medium access control sublayer

    4.1 the channel allocation problem
        4.1.1 static channel allocation
        4.1.2 assumptions for dynamic channel allocation

    4.2 multiple access protocols
        4.2.1 aloha
        4.2.2 carrier sense multiple access protocols
        4.2.3 collision free protocols
        4.2.4 limited contention protocols
        4.2.5 wireless lan protocols

    4.3 ethernet
        4.3.1 classic ethernet physical layer
        4.3.2 classic ethernet mac sublayer protocol
        4.3.3 ethernet performance
        4.3.4 switched ethernet
        4.3.5 fast ethernet
        4.3.6 gigabit ethernet
        4.3.7 10 gigabit ethernet
        4.3.8 retrospective on ethernet todo

    4.4 wireless lans
        4.4.1 the 802.11 architecture and protocol stack
        4.4.2 the 802.11 physical layer
        4.4.3 the 802.11 mac sublayer protocol
        4.4.4 the 802.11 frame structure
        4.4.5 services

    4.5 broadband wireless
        4.5.1 comparison of 802.16 with 802.11 and 3g
        4.5.2 the 802.16 architecture and protocol stack
        4.5.3 the 802.16 physical layer
        4.5.4 the 802.16 mac sublayer protocol
        4.5.5 the 802.15 frame structure

    4.6 bluetooth todo
        4.6.1 bluetooth architecture
        4.6.2 bluetooth application
        4.6.3 the bluetooth protocol stack
        4.6.4 the bluetooth radio layer
        4.6.5 the bluetooth link layer
        4.6.6 the bluetooth frame structure

    4.7 frid todo
        4.7.1 epc gen 2 architecture
        4.7.2 epc gen 2 physical layer
        4.7.3 epc gen 2 tag identification layer
        4.7.4 tag identification message formats

    4.8 data link layer switching
        4.8.1 uses of bridges
        4.8.2 learning bridges
        4.8.3 spanning tree bridges
        4.8.4 repeaters, hubs, bridges, switches, routers, and getaways
        4.8.5 virtual lans

    4.9 summary

5. the network layer

    5.1 network layer design issues
        5.1.1 store and forward packet switching
        5.1.2 services provide to the transport layer
        5.1.3 implementation of connectionless service
        5.1.4 implementation of connection oriented service
        5.1.5 comparison of virtual circuit and datagram network

    5.2 routing algorithms
        5.2.1 the optimality principle
        5.2.2 shortest path algorithm
        5.2.3 flooding
        5.2.4 distance vector routing
        5.2.5 link state routing
        5.2.6 hierarchical routing
        5.2.7 broadcast routing
        5.2.8 multicast routing
        5.2.9 anycast routing
        5.2.10 routing for mobile hosts
        5.2.11 routing in ad hoc networks

    5.3 congestion control algorithms
        5.3.1 approaches to congestion control
        5.3.2 traffic aware routing
        5.3.3 admission control
        5.3.4 traffic throttling
        5.3.5 load shedding todo

    5.4 quality of service
        5.4.1 application requirements
        5.4.2 traffic shaping
        5.4.3 packet scheduling
        5.4.4 admission control
        5.4.5 integrated services
        5.4.6 differentiated services

    5.5 internetworking
        5.5.1 how networks differ
        5.5.2 how networks can be connected
        5.5.3 tunneling
        5.5.4 internetwork routing
        5.5.5 packet fragmentation

    5.6 the network layer in the internet
        5.6.1 the ip version 4 protocol
        5.6.2 ip addresses
        5.6.3 ip version 6
        5.6.4 internet control protocols
        5.6.5 label switching and mpls
        5.6.6. ospf - an interior gateway routing protocol
        5.6.7 bgp - the exterior gateway routing protocol
        5.6.8 internet multicasting
        5.6.9 mobile ip

    5.7 summary

6. the transport layer

    6.1 the transport service
        6.1.1 services provided to the upper layers
        6.1.2 transport service primitives
        6.1.3 berkeley sockets
        6.1.4 an example of socket programming: an internet file server

    6.2 elements of transport protocols
        6.2.1 addressing
        6.2.2 connection establishment
        6.2.3 connection release
        6.2.4 error control and flow control
        6.2.5 multiplexing
        6.2.6 crash recovery

    6.3 congestion control todo
        6.3.1 desirable bandwidth allocation
        6.3.2 regulating the sending rate
        6.3.3 wireless issues

    6.4 the internet transport protocols: udp
        6.4.1 introduction to udp
        6.4.2 remote procedure call
        6.4.3 real-time transport protocols

    6.5 the internet transport protocols: tcp
        6.5.1 introduction to tcp
        6.5.2 the tcp service model
        6.5.3 teh tcp protocol
        6.5.4 teh tcp segment header
        6.5.5 tcp connection establishment
        6.5.6 tcp connection release
        6.5.7 tcp connection management modeling
        6.5.8 tcp sliding window
        6.5.9 tcp timer management
        6.5.10 tcp congestion control todo
        6.5.11 the future of tcp

    6.6 performance issues
        6.6.1 performance problems in computer networks
        6.6.2 network performance measurement
        6.6.3 host design for fast network
        6.6.4 fast segment processing
        6.6.5 header compression
        6.6.6 protocols for long fat networks

    6.7 delay tolerant networking
        6.7.1 dtn architecture
        6.7.2 the bundle protocol

    6.8 summary

7. the application layer

    7.1 dns - the domain name system
        7.1.1 the dns name space
        7.1.2 domain resource records
        7.1.3 name servers

    7.2 electronic mail
        7.2.1 architecture and services
        7.2.2 the user agent
        7.2.3 message formats
        7.2.4 message transfer
        7.2.5 final delivery

    7.3 the world wide web
        7.3.1 architectural overview
        7.3.2 static web pages
        7.3.3 dynamic web pages and web applications
        7.3.4 http - the hypertext transfer protocol
        7.3.5 the mobile web
        7.3.6 web search

    7.4 streaming audio and vidio
        7.4.1. digital audio
        7.4.2 digital video
        7.4.3 streaming stored media
        7.4.4 streaming live media
        7.4.5 real time conferencing

    7.5 content delivery
        7.5.1 content and internet traffic
        7.5.2 server farms and web proxies
        7.5.3 content delivery networks
        7.5.4 peer-to-peer networks

    7.6 summary

8. network security

    8.1 cryptography
        8.1.1 introduction to cryptography
        8.1.2 substitution ciphers todo
        8.1.3 transposition ciphers
        8.1.4 one time pads
        8.1.5 two fundamental cryptographic principles

    8.2 symmetric key algorithms todo
        8.2.1 des - the data encryption standard
        8.2.2 aes - the advanced encryption standard
        8.2.3 cipher modes
        8.2.4 other ciphers
        8.2.5 cryptanalysis

    8.3 public key algorithms todo
        8.3.1 rsa
        8.3.2 other public key algorithms

    8.4 digital signatures
        8.4.1 symmetric key signatures
        8.4.2 public key signatures
        8.4.3 message digests
        8.4.4 the birthday attach

    8.5 management of public keys
        8.5.1 certificates
        8.5.2 x 509, 809
        8.5.3 public key infrastructures

    8.6 communication security
        8.6.1 ipsec
        8.6.2 firewalls
        8.6.3 virtual private networks
        8.6.4 wireless security

    8.7 authentication protocol
        8.7.1 authentication based on a shared secret key
        8.7.2 establishing a shared key: the deffie-hellman key exchange
        8.7.3 authentication using a key distribution center
        8.7.4 authentication using kerberos todo
        8.7.5 authentication suing public key cryptography

    8.8 email security
        8.8.1 pgp - pretty good privacy todo
        8.8.2 s/mine todo

    8.9 web security
        8.9.1 threat
        8.9.2 secure naming
        8.9.3 ssl - the secure sockets layer
        8.9.4 mobile code security

    8.10 social issues
        8.10.1 privacy
        8.10.2 freedom of speech
        8.10.3 copyright

    8.11 summary

9. reading list and bibliography todo

    9.1 suggestions for further reading
        9.1.1 introduction and general works
        9.1.2 the physical layer
        9.1.3 the data link layer
        9.1.4 the medium access control sublayer
        9.1.5 the network layer
        9.1.6 the transport layer
        9.1.7 the application layer
        9.1.8 network security

    9.2 alphabetical bibliography

"""