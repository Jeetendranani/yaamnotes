"""
Modern operating system

1. introduction

    1.1 wht is an operating system?
        1.1.1 the operating system as an extended machine
        1.1.2 the operating system as a resource manager

    1.2 history of operating system
        1.2.1 the first generation (1945-55): vacuum tubes
        1.2.2 the second generation (1955-65): transistors and batch systems
        1.2.3 the third generation (1965-1980): ics and multiprogramming
        1.2.4 the forth generation (1980 - present): personal computers
        1.2.5 the fifth generation (1990-present): mobile computers

    1.3 computer hardware review
        1.3.1 processors
        1.3.2 memory
        1.3.3 disks
        1.3.4 i/o devices
        1.3.5 buses
        1.3.6 booting the computer

    1.4 the operating system zoo
        1.4.1 mainframe operating systems
        1.4.2 server operating systems
        1.4.3 multiprocessor operating systems
        1.4.4 personal computer operating systems
        1.4.5 handheld computer operating systems
        1.4.6 embedded operating systems
        1.4.7 sensor node operating systems
        1.4.8 real time operating systems
        1.4.9 smart card operating systems

    1.5 operating system concepts
        1.5.1 processes
        1.5.2 address spaces
        1.5.3 files
        1.5.4 input/output
        1.5.5 protection
        1.5.6 the shell
        1.5.7 ontogeny recapitulates phylogeny todo

    1.6 system calls
        1.6.1 system calls for process management
        1.6.2 system calls for file management
        1.6.3 system calls for directory management
        1.6.4 miscellaneous system calls
        1.6.5 the windows win32 api

    1.7 operating system structure
        1.7.1 monolithic systems
        1.7.2 layered systems
        1.7.3 microkernels
        1.7.4 client-server model
        1.7.5 virtual machines
        1.7.6 exokernels

    1.8 the world according to c
        1.8.1 the c language
        1.8.2 header files
        1.8.3 large programming projects
        1.8.4 the model of run time

    1.9 research on operating systems

    1.10 outline of the rest of this book

    1.11 metric units

    1.12 summary

2. processes and threads

    2.1 process
        2.1.1 the process model
        2.1.2 process creation
        2.1.3 process termination
        2.1.4 process hierarchies
        2.1.5 process states
        2.1.6 implementation of processes
        2.1.7 modeling multiprogramming

    2.2 threads
        2.2.1 thread usage
        2.2.2 the classical thread model
        2.2.3 posix threads
        2.2.4 implementing threads in user space
        2.2.5 implementing threads in the kernel
        2.2.6 hybrid implementations
        2.2.7 scheduler activations
        2.2.8 pop-up threads
        2.2.9 making single threaded core multithreaded

    2.3 interprocess communication
        2.3.1 race conditions
        2.3.2 critical regions
        2.3.3 mutual exclusion with busy waiting
        2.3.4 sleep and wakeup
        2.3.5 semaphores todo
        2.3.6 mutexes todo
        2.3.7 monitors
        2.3.8 message passing
        2.3.9 barriers
        2.3.10 avoiding locks: read copy update

    2.4 scheduling
        2.4.1 introduction to scheduling
        2.4.2 scheduling in batch system
        2.4.3 scheduling in interactive systems
        2.4.4 scheduling in real time systems
        2.4.5 policy versus mechanism
        2.4.6 thread scheduling

    2.5 classical ipc problems
        2.5.1 the dining philosophers problem
        2.5.2 the readers and writers problem

    2.6 research on processes and threads

    2.7 summary

3. Memory management

    3.1 no memory abstraction

    3.2 a memory abstraction: address spaces
        3.2.1 the notion of an address space
        3.2.2 swapping
        3.2.3 managing free memory

    3.3 virtual memory
        3.3.1 paging
        3.3.2 page tables
        3.3.3 speeding up paging
        3.3.4 page tables for large memories

    3.4 page replacement algorithm
        3.4.1 the optimal page replacement algorithm
        3.4.2 the not recently used page replacement algorithm
        3.4.3 the first-in, first-out (fifo) page replacement algorithm
        3.4.4 the second chance page replacement algorithm
        3.4.5 the clock page replacement algorithm
        3.4.6 the least recently used (lru) page replacement algorithm
        3.4.7 simulating lru in software
        3.4.8 the working set page replacement algorithm
        3.4.9 the wsclock page replacement algorithm
        3.4.10 summary of pge replacement algorithms

    3.5 design issues for paging systems
        3.5.1 local versus global allocation policies
        3.5.2 load control
        3.5.3 page size
        3.5.4 separate instruction and data spaces
        3.5.5 shared pages
        3.5.6 shared libraries
        3.5.7 mapped files
        3.5.8 cleaning policy
        3.5.9 virtual memory interface

    3.6 implementation issues
        3.6.1 operating system involvement with paging
        3.6.2 page fault handing
        3.6.3 instruction backup
        3.6.4 locking pages in memory
        3.6.5 backing store
        3.6.6 separation of policy and mechanism

    3.7 segmentation
        3.7.1 implementation of pure segmentation
        3.7.2 segmentation with paging: multics
        3.7.3 segmentation with paging: the intel x 86

    3.8 research on memory management

    3.9 summary

4. file systems

    4.1 files
        4.1.1 file naming
        4.1.2 file structure
        4.1.3 file types
        4.1.4 file access
        4.1.5 file attributes
        4.1.6 file operations
        4.1.7 an example program using file-system calls

    4.2 directories
        4.2.1 single-level directory systems
        4.2.2 hierarchical directory systems
        4.2.3 path names
        4.2.4 directory operations

    4.3 file-system implementation
        4.3.1 file-system layout
        4.3.2 implementing files
        4.3.3 implementing directories
        4.3.4 shared files
        4.3.5 log-structured file systems
        4.3.6 journaling file system todo
        4.3.7 virtual file systems

    4.4 file-system management and optimization
        4.4.1 disk space management
        4.4.2 file system backups
        4.4.3 file system consistency
        4.4.4 file system performance
        4.4.5 defragmenting disks

    4.5 example file systems
        4.5.1 the ms-dos file system
        4.5.2 the unix v7 file system
        4.5.3 cd-rom file systems

    4.6 research on file systems

    4.7 summary

5. input/output

    5.1 principles of i/o hardware
        5.1.1 i/o devices
        5.1.2 device controllers
        5.1.3 memory mapped i/o
        5.1.4 direct memory access
        5.1.5 interrupts revisited

    5.2 principles of i/o software
        5.2.1 goals of the i/o software
        5.2.2 programmed i/o
        5.2.3 interrupt driven i/o
        5.2.4 i/o using dma

    5.3 i/o software layers
        5.3.1 interrupt handlers
        5.3.2 device drivers
        5.3.3 device independent i/o software
        5.3.4 user space i/o software

    5.4 disks
        5.4.1 disk hardware
        5.4.2 disk formatting
        5.4.3 disk arm scheduling algorithms
        5.4.4 error handling
        5.4.5 stable storage

    5.5 clocks
        5.5.1 clock hardware
        5.5.2 clock software
        5.5.3 soft timers

    5.6 user interfaces: keyboard, mouse, monitor
        5.6.1 input software
        5.6.2 output software

    5.7 thin clients

    5.8 power management
        5.8.1 hardware issues
        5.8.2 operating system issues
        5.8.3 application program issues

    5.9 research on input/output

    5.10 summary

6. deadlocks

    6.1 resources
        6.1.1 preemptable and nonpreemptable resources todo
        6.1.2 resource acquisition

    6.2 introduction to deadlocks
        6.2.1 conditions for resource deadlocks
        6.2.2 deadlock modeling

    6.3 the ostrich algorithm todo

    6.4 deadlock detection and recovery
        6.4.1 deadlock detection with one resource of each type
        6.4.2 deadlock detection with multiple resources of each type
        6.4.3 recovery from deadlock

    6.5 deadlock avoidance
        6.5.1 resource trajectories todo
        6.5.2 safe and unsafe states
        6.5.3 the banker's algorithm for a single resource
        6.5.4 the banker's algorithm for multiple resource

    6.6 Deadlock prevention
        6.6.1 attaching the mutual exclusion condition
        6.6.2 attaching the hold and wait condition
        6.6.3 attaching the no-preemption condition
        6.6.4 attaching the circular wait condition

    6.7 other issues
        6.7.1 two-phase locking
        6.7.2 communication deadlocks
        6.7.3 livelock
        6.7.4 starvation

    6.8 research on deadlocks

    6.9 summary

7. virtualization and the cloud

    7.1 history

    7.2 requirements for virtualization

    7.3 type 1 and type 2 hypervisors

    7.4 techniques for efficient virtualization
        7.4.1 virtualizing the unvirtualizable
        7.4.2 the cost of virtualization

    7.5 are hypervisors microkernels done right?

    7.6 memory virtualization

    7.7 i/o virtualization

    7.8 virtual appliances

    7.9 virtual machines on multicore cpus

    7.10 licensing issues

    7.11 clouds
        7.11.1 clouds as a service
        7.11.2 virtual machine migration
        7.11.3 checkpointing

    7.12 case study: vmware
        7.12.1 the early history of vmware
        7.12.2 vmware workstation
        7.12.3 challenges in bringing virtualization to the x86
        7.12.4 vmware workstation: solution overview
        7.12.5 teh evolution of vmware workstation
        7.12.6 esx server: vmware's type 1 hipervisor

    7.13 research on virtualization and the cloud

8. multiple processor systems

    8.1 multiprocessors
        8.1.1 multiprocessor hardware
        8.1.2 multiprocessor operating system types
        8.1.3 multiprocessor synchronization
        8.1.4 multiprocessor scheduling

    8.2 multicomputers
        8.2.1 multicomputer hardwre
        8.2.2 low-level communication software
        8.2.3 user-level communication software
        8.2.4 remote procedure call
        8.2.5 distributed shared memory
        8.2.6 multicomputer scheduling
        8.2.7 load balancing

    8.3 distributed systems
        8.3.1 network hardware
        8.3.2 network services and protocols
        8.3.3 document based middleware
        8.3.4 file system based middleware
        8.3.5 object based middleware
        8.3.6 coordination based middleware

    8.4 research on multiple processor systems

    8.5 summary

9. security

    9.1 The security environment
        9.1.1 threats
        9.1.2 attackers

    9.2 operating systems security
        9.2.1 can we build secure systems
        9.2.2 trusted computing base

    9.3 controlling access to resources
        9.3.1 protection domains
        9.3.2 access control lists
        9.3.3 capabilities

    9.4 formal models of secure systems
        9.4.1 multilevel security
        9.4.2 covert channels

    9.5 basics of cryptography
        9.5.1 secret key cryptography
        9.5.2 public key cryptography
        9.5.3 one way functions
        9.5.4 digital signatures
        9.5.5 trusted platform modules

    9.6 authentication
        9.6.1 authentication using a physical object
        9.6.2 authentication using biometrics

    9.7 exploiting software
        9.7.1 buffer overflow attacks
        9.7.2 format string attacks
        9.7.3 dangling pointers
        9.7.4 null pointer dereference attacks
        9.7.5 integer overflow attacks
        9.7.6 command injection attacks
        9.7.7 time of check to time of use attacks

    9.8 insider attacks
        9.8.1 logic bombs
        9.8.2 back doors
        9.8.3 login spoofing

    9.9 malware
        9.9.1 trojan horses
        9.9.2 viruses
        9.9.3 worms
        9.9.4 spyware
        9.9.5 rootkits

    9.10 defenses
        9.10.1 firewalls
        9.10.2 antivirus and auti-antivirus techniques
        9.10.3 code signing
        9.10.4 jailing
        9.10.5 model based intrusion detection
        9.10.6 encapsulating mobile code
        9.10.7 java security

    9.11 research on security

    9.12 summary

10. case study 1: unix, linux, and android

    10.1 history of unix and linux
        10.1.1 unics
        10.1.2 pdp-11 unix
        10.1.3 protable unix
        10.1.4 berkely unix
        10.1.5 standard unix
        10.1.6 minix
        10.1.7 linux

    10.2 overview of linux
        10.2.1 linux goals
        10.2.2 interfaces to linux
        10.2.3 teh shell
        10.2.4 linux utility programs
        10.2.5 kernel structure

    10.3 processes in linux
        10.3.1 fundamental concepts
        10.3.2 process management system calls in linux
        10.3.3 implementation of processes and threads in linux
        10.3.4 scheduling in linux
        10.3.5 booting linux

    10.4 memory management in linux
        10.4.1 fundamental concepts
        10.4.2 memory management system calls in linux
        10.4.3 implementation of memory management in linux
        10.4.4 paging in linux

    10.5 input/ouput in linux
        10.5.1 fundamental concepts
        10.5.2 networking
        10.5.3 input/output system call in linux
        10.5.4 implementation of input/output in linux
        10.5.5 modules in linux

    10.6 the linux file system
        10.6.1 fundamental concepts
        10.6.2 file-system calls in linux
        10.6.3 implementation of the linux file system
        10.6.4 nfs: the network file system

    10.7 security in linux
        10.7.1 fundamental concepts
        10.7.2 security system calls in linux
        107.3 implementation of security in linux

    10.8 android
        10.8.1 android and google
        10.8.2 history of android
        10.8.3 design goals
        10.8.4 android architecture
        10.8.5 linux extensions
        10.8.6 dalvik
        10.8.7 binder ipc
        10.8.8 android applications
        19.8.9 intent
        10.8.10 application sandboxes
        10.8.11 security
        10.8.12 process model

    10.9 summary

11. case study 2: windows 8 todo

12. operating system design

    12.1 the nature of the design problem
        12.1.1 goals
        12.1.2 why is it hard to design an operating system?

    12.2 interface design
        12.2.1 guiding principles
        12.2.2 paradigms
        12.2.3 the system call interface

    12.3 implementation
        12.3.1 system structure
        12.3.2 mechanism vs policy
        12.3.3 orthogonality
        12.3.4 naming
        12.3.5 binding time
        12.3.6 static vs. dynamic structures
        12.3.7 top-down vs bottom-up implementation
        12.3.8 synchronous vs asynchronous communication
        12.3.9 useful techniques

    12.4 performance
        12.4.1 why are operating system slow?
        12.4.2 what should be optimized
        12.4.3 space time trade offs
        12.4.4 caching
        12.4.5 hints
        12.4.6 exploiting locality
        12.4.7 optimize teh common case

    12.5 project management
        12.5.1 the mythical man month
        12.5.2 team structure
        12.5.3 the role of experience
        12.5.4 no silver bullet

    12.6 trends in operating system design
        12.6.1 virtualization and the cloud
        12.6.2 manycore chips
        12.6.3 large- address space operating systems
        12.6.4 seamless data access
        12.6.5 battery powered computers
        12.6.6 embedded systems

    12.7 summary

13. Reading list and bibliography

    13.1 suggestions for further reading
        13.1.1 introduction
        13.1.2 processes and threads
        13.1.3 memory management
        13.1.4 file system
        13.1.5 input/output
        13.1.6 deadlocks
        13.1.7 virtualization and the cloud
        13.1.8 multiple processor system
        13.1.9 security
        13.1.10 case study 1: unix, linux and android
        13.1.11 case study 2: windows 8
        13.1.12 operating system design

    13.2 alphabetical bibliography
"""