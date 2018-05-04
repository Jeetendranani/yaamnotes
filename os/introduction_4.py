"""
1.7.4 client - server model

A slight variation of teh microkernel idea is to distinguish two classes of processes, the servers, each of which
provides some service, and the clients, which use these services. This model is know  as the client-server model. Often
the lowest layer is a microkernel, but that is not required. The essence is the presence of client processes and server
processes.

communication between clients and servers is often by message passing. To obtain a service, a client process constructs
a message saying what it wants and send it to the appropriate service. The service then does the work and sends back the
answer. if the client and server happen to run on the same machine, certain optimization are possible, but conceptually
we are still talking about massage passing here.

An obvious generalization of this idea is to have the clients and server run on different computers, connected by a
local or wide area network, as depicted in Fig 1-27. Since clients communicate with server by sending messages, the
clients need to not know whether the message are handled locally on their own machines, or whether they are sent across
a network to servers on a remote machine. As far as teh client is connected, the same thing happens in both cases;
requests re sent and replies come back. Thus the client server model is an abstraction that can be used for a single
machine or for a network of machines.

Increasingly many systems involve users at their home pcs as client and large machines elsewhere running as servers. In
fact, much of the web operates this way. A PC sends a request for a web page to the server and the web page comes back.
This is a typical use of the client-server model in a network.

1.7.5 Virtual machines

The initial release of os/360 were strictly batch systems. Nevertheless, many 360 users wanted to be able to work
interactively at a terminal, so various groups, both inside and outside IBM, decide to write timesharing systems for it.
The official IMB timesharing system, TSS/360, was delivered late, and when it finally arrived it was so big and slow
that few sites converted to it. it was eventually abandoned after its development had consumed some $50 million. But a
group at IBM's Scientific center in cambridge, massachusetts, produced a radically different system that IBM eventually
accepted as a product. A linear descendant of it, called z/VM, is now widely used on IBM's current mainframes, the
zSeries, which are heavily used in large corporate data centers, for example, as e-commerce servers that handle hundreds
or thousands of transactions per second and use databases whose sizes run  to millions of gigabytes.

VM/370

This system, originally called CP/CMS and later renamed VM/370 (Seawright and MacKinnon, 1979), was based on astute
observation: A timesharing system provides (1) multiprogramming and (2) an extended machine with a more convenient
interface than the bare hardware. The essence of VM/370 is to completely separate these two functions.

The heart of the system, known as teh virtual machine monitor, runs on the bare hardware and does the multiprogramming,
providing not one, but several virtual machines to net next layer up, as shown in Fig 1-28. However, unlike all other
operating systems, these virtual machines are not extended machines, with files and other nice features. Instead,
they are exact copies of the bare hardware, including kernel/user mode, i/o, interrupts, and everything else the real
machine has.

Because each virtual machine is identical to the true hardware, each one can run any operating system that will run
directly on the bare hardware. Different virtual machines can, and frequently do, run different operating systems. On
the original IBM VM/370 system, some ran os/360 or one of the other large batch or transaction processing systems,
while other run a single user, interactive system called CMS (conversational monitor system) for interactive
timesharing users. The latter was popular with programmers.

When a CMS program executed a system call, the call was trapped to the operating system in tis own virtual machine, not
to vm/370, just as it would be were it running on a real machine instead of a virtual one. CMS then issued the normal
hardware i/o instructions for reading its virtual disk or whatever was needed to carry out the call. These i/o
instructions were trapped by vm/370, which them performed them as part of tis simulation of the real hardware. By
completely separating the functions of multiprogramming and providing an extended machine, each of he pieces could be
much simpler, more flexible, and much easier to maintain.

In its modern incarnation, z/VM is usually used to run multiple complete operating systems rather then stripped-down
single-user systems like CMS. For example, the zSeries is capable of running one or more Linux virtual machine along
with traditional IBM operating system.

Virtual machines rediscovered

while IBM has had a virtual machine product available for four decades, and a few other companies, including Oracle and
Hewlett-Packard, have recently added virtual machine support to their high end enterprise servers. the idea of
virtualization has largely been ignored in the pc world until recently, But in the past few years, a combination of new
new needs, new software, and new technologies have combined to make it a hot topic.

First teh needs, many companies have traditionally run their mail servers, web server, ftp servers, and other servers on
separate computers, sometimes with different operating systems. They see virtualization as a way to run them all on the
same machine without having a crash of one server bring down the rest.

Virtualization is also popular in the web hosting between shared hosting (which just given them a login account (which
gives them own machine, which is very flexible but not cost effective for small to medium websites). When a web hosting
company offers virtual machines for rent, a single physical machine can run many virtual machines, each of them appears
to be a complete machine. customers who rent a virtual machine can run whatever operating system and software they want
to, but at a fraction of the cost of a dedicated server (because the same physical machine supports many virtual
machines at the same time).

Another use of virtualization is for end users who want to be able to run two or more operating systems at the same
time, say windows and linux, because some of their favorite application package run on one and some run on the other.
this situation is illustrated in fig 1-29(a), where teh term "virtual machine monitor" has been renamed type 1
hypervisor, which is commonly used nowadays because "virtual machine monitor" requires more keystrokes than people
are prepared to put up with now. note that many authors use the terms interchangeably though.

While no one disputes teh attractiveness of virtual machines today, the problem then was implementation. In order to
run virtual machine software on a computer, its CPU must be virtualizable (Popek and Goldberg, 1974). In a nutshell,
here is the problem. When an operating system running on a virtual machine (in user mode) executes a privileged
instruction. such as modifying the PSW or doing I/O, it is essential that the hardware trap to hte virtual-machine
monitor so the instruction can be emulated in software. On some CPUs - notably the Pentium, its predecessors, and its
clones - attempts to execute privileged instruction in user mode are just ignored. This property made it impossible to
have virtual machines on this hardware, which explains teh lack of interest in the x86 world. Of course, there were
interpreters for the Pentium, such as Bochs, that ran on the Pentium, but with a performance loss of one of two orders
of magnitude, they were not useful for serious work.

This situation changed as a result of several academic research projects in the 1990s and early years of this
millennium, notably Disco at Stanford and Xen at Cambridge university. These research papers led to several commercial
products (e.g., VMware Workstation and Xen) and a revival of interest in virtual machines. Besides VMware and Xen,
popular hypervisors today include KVM (for the linux kernel), VirtalBox (by Orical) and Hyper-V (by Microsoft).

Some of these early research projects improved the performance over interpreters like bochs by translating blocks of
code on the fly. Storing them in an internal cache, and then reusing them if they were executed again. This improved the
performance considerably, and led to what we call machine simulators, as shown in Fig 1-29(b). However although this
technique, known as binary translation, helped improve matters, the resulting systems, while good enough to publish
papers about in academic conferences, were still not fast enough to use in commercial environments where performance
matters a lot.

The next step in improving performance was to add a kernel module to do some of the heavy lifting, as shown in Fig 1-29
(c). In practice now, all commercially available hypervisors, such as vmware workstation, use this hybrid strategy
(and have many other improvements as well). they are called type 2 hypervisors by everyone, so we will (somewhat
grudgingly) go along and use this name in the rest of this book, even though we would prefer to call them type 1.7
hypervisors to reflect the fact that they are not entirely user-mode programs. In chapter 7, we will describe in detail
how vmware workstation works and what the various pieces do.

In practice, the real distinction between type1 and a type2 hypervisor is that the type2 makes uses of a host operating
system and its file system to create processes, store files, and so on. A type 1 hypervisor has no underlying support
and must perform all these functions itself.

After a type2 hypervisor is started, it reads the installation CD-ROM (or CD-ROM image file) for the chosen guest
operating system and installs the guest os on a virtual disk, which is just a big file in the host operating systems'
file system. Type 1 hypervisors cannot do this because there is no host operating system to store files on. They must
manage their own storage on a raw disk partition.

When the gust operating system is booted, it does the same thing it does on the actual hardware, typically starting up
some background processes and then a GUI. To the user, the guest operating system behaves the same way it does when
running on the bare metal even though that is not the case here.

A different approach to handling control instructions is to modify the operating system to remove them. This approach
is not true virtualization, but paravirtualization. we will discuss virtualization in more detail in chapter 7.

The java  virtual machine

Another area where virtual machine are used, but in a somewhat different way, is for running java programs, when sum
microsystems invented the java programming language, it also invented a virtual machine (i.e., a computer architecture)
called the JVM (Java Virtual Machine). The Java compiler produce code for JVM, which then typically is executed by a
software JVM interpreter. The advantage of this approach is that the JVM code can be shipped over the Internet to any
computer that has a JVM interpreter and run there. If the compiler had produced SPARC or x86 binary programs, for
example, they could not have been shipped and run anywhere as easily. (of course, sun could have produced a compiler
that produced SPARC binaries and then ditributed a sparc interpreter, but jvm is a much simpler architecture to
interpret.) Another advantage of using JVM is that if the interpreter is implemented properly, which is not completely
trivial incoming JVM programs can be checked for safety and them executed in a protected environment so they cannot
steal data or do any damage.

1.7.6 Exokernels

Rather than cloning the actual machine, as is done with virtual machines. another strategy is partitioning it, in other
works, giving each user a subset of the resources, thus one virtual machine might get disk blocks 0 to 1023, the next
one might get blocks 1024 to 2047, and so on.

At teh bottom layer, running in kernel mode, is a program called the exokernel (Engler et al., 1995). Its job is to
allocate resources to virtual machines and then check attempts to use them to make sure no machine is trying to user
somebody else's resources. Each user-level virtual machine can run its own operating system, as on vm/370 and the
pentium virtual 8086s, except that each one is restricted to using only the resources it has asked for and been
allocated.

The advantage of the exokernel scheme is that it saves a layer of mapping. in the other designs, each virtual machine
thinks it has its own disk, with blocks running from 0 to some maximum, so the virtual machine monitor must maintain
table to remap disk addresses (and all other resources). With the exokernel, this remapping has been assigned which
resource. This methods is still has the advantage of separating the multiprogramming (in the exokernel) from the user
operating system code (in user space), but with less overhead, since all the exokernel has to do is keep the virtual
machines out of each other's hair.

1.8 the world according to c

Operating systems are normally large C (or sometimes C++) programs consisting of many pieces written by many
programmers. The environment used for developing operating systems is very different from what individuals (such as
students) are used to when writing small java programs. This section is an attempt to give a very brief introduction to
the world of writing an operating system for small time java or python programmers.

1.8.1 The c language

This is not a guide to c, but a shot summary of some of the key differences between c and language like python and
especially java. java is based on c, so there are many similarities between the two. Python is somewhat different, but
still fairly similar. For convenience, we focus on Java. Java, python and c are all imperative languages with data
types, variables, and control statements, for example. The primitive data types in C are integers (including short and
long ones), characters, and floating-point numbers. composite data sypes in c are similar to those in java, including
if, switch for, and while statements. Functions and parameters are roughly the same in both languages.

One feature C has that Java and Python do not is explicit pointers. A pointer is a variable that pointer to a variable
or data structure. Consider the statements

    char c1, c2 *p;
    c1 = 'c';
    p = &c1;
    c2 = *p;

which declare c1 and c2 to be character variables and p to be a variable that points to a character. The first
assignment stores teh ascii code for the character 'c' in the variables c1. The second one assigns the address of c1 to
the pointer p. The third one assigns teh contents of the variable pointed to by p to the variable c2, so after these
statements are executed, c2 also contains the ascii code for 'c'. In theory, pointers are typed, so you are not
supposed to assign the address of a floating-point number to a character pointer, but in practice compilers accept such
assignments, albeit sometimes with a warning. Pointers are a very powerful construct, but also a great source of errors
when used carelessly.

Some things that C does not have include built-in strings, threads, packages, classes, objects, type safety, and
garbage collection. The last one is a show stopper for operating systems. All storage in C is either static or
explicitly allocated and released by the programmer, usually with teh library functions malloc and free. It is the
latter property - total programmer control over memory - along with explicit pointers that makes c attractive for
writing operating systems. operating systems are basically real-time system to some extent, even general-purpose ones.
When an interrupt occurs, the operating system may have only a few microseconds to perform some action or lose
critical information. Having the garbage collector kick in at an arbitrary memory is intolerable.

1.8.2 header files

An operating system project generally consists of sme number os directories, each containing many .c files containing
the code for some part of the system, along with some .h header files tht contains declarations and definitions sued by
one or more code files. Header files can also include simple macros, such as

#define BUFFEER_SIZE 4096

which allows the programmer to name constants, so that when BUFFER_SIZE is used in the code, it is replaced during
complication by the number 4096. Good C programming practice is to name every constant except 0, 1, and -1, and
sometimes even them. Macros can have parameters, such as

#define max(a, b) (a>b?a:b)

which allows the programmer to write

i = max(j, k+1)

and get i = (j>K+1?j:k+1)

to store the larger of j and k+1 in i. Headers can also contain conditional compilation, for example

#ifdef x86
inter_int_ack();
#endif

which compiles into a call to the function intel_int_ack if the macro x86 is defined and nothing otherwise. Conditional
compilations is heavily used to isolate architecture-dependent code so that certain code is inserted only when the
system is compiled on a sparc, and so on. A .c file can bodily include zero or more header files using the #include
directive. There are also many header fiels that are common to nearly every .c and are stored in a central directory.

1.8.3 Large programming projects

To build the operating system, each .c is compiled into an abject file by the c compiler. object files, which have the
suffix .o, contain binary instructions for teh target machine. They will later be directly executed by the CPU. There
is nothing like java byte code or python byte code in the c world.

The first pass of the c compiler is called the c preprocessor, as it reads each .c file, every time it hits a #include
directive, it goes and gets the header file named in it and process it, expanding macros, handing conditional
compilation (and certain other things) and passing the results to the next pass of the compiler as if they were
physically included.

Since operating systems are very large (five million lines of code is not unusual), having to recompile the entire thing
every time one file is changed would be unbearable. On the other hand, changing a key header file that is included in
thousands of other files does require recompiling those files. Keeping track of which object files depend on which
header files is completely unmanageable without help.

Fortunately, computers are very good at precisely this sort of thing. On unix systems, there is a program called
make ( with numerous variants such as gmake, pmake, etc) that reads the Makefile, todo
which is tells it which files are dependent on (the code and headers) have been modified subsequent to the last time
the object file was created. If so, that object files has to be recompiled. When make has determined which .c files
have to recompiled, it then invokes the C compiler to recompile them, thus reducing the number of compilations to the
bare minimum. In large projects, creating Makefile is error prone, so there are tools that do it automatically.

Once all the .o files are ready, they are passed to a program called the linker to combine all of them into a single
executable binary file. Any library functions called are also included at this point, interfunction references are
resolved, and machine addresses are relocated as need be. When the linker is finished, the result is an executable
program, traditionally called a.out on unix systems. The various components of this process are illustrated in Fig 1-30
for a program with three c files and two header files. Although we have been discussing operating system development
here, all of this applies to developing any large program.

1.8.4 the model of run tiem

Once the operating system binary has been linked, the computer can be rebooted and the new operating system started.
Once running, it may dynamically load pieces that were not statically included in the binary such as device drivers
and file systems. At run time the operating system may consist of multiple segments, for the text (the program code),
the data, and the stack. The text segment is normally immutable, not changing during execution. The data segment starts
out at a certain size and initialized with certain values, but it can change and grow as need be. The stack is initially
empty but trows and shrinks as functions are called and returned from. Often the next segments is placed near the bottom
of the memory, the data segment just above it, with the ability to grow upward, and the stack segment at a high virtual
address, with the ability to grow downward, but different systems work differently.

In all cases, the operating system code is directly executed by the hardware, with no interpreter and no just in time
compilation, as is normal with java.

1.9 research on operating systems

Computer science is a rapidly advancing field and it is hard to predict where is is going. Researchers at universities
and industrial research labs are constantly thinking up new ideas, some of which go nowhere but some of which become
the cornerstone of future products and have massive impact on the industry and users. Telling which is which turns out
to be easier to do in hindsight than in real time. Separating the wheat for the chaff is especially difficult because
it often takes 20 to 30 years from idea to impact.

For example, when president Eisenhower set up teh dept. of defense's advanced research project agency in 1958, he was
trying to keep hte army from killing hte navy and the air force over the pentagons's research budget. He aws not trying
to invent the internet. But one of things ARPA did was fund some university research on the then obscure concept of
packet switching, which led to the first experimental packet switched network, the ARPANET. It went live in 1969, before
long, other arpa-funded research networks were connected to the arpanet, and the internet was born. The internet was
then happily used by academic researchers for sending email to each other for 20 years. In the early 1990s. Tim
Berners -Lee invented the world wide web at teh cern research lab in geneva and marc andreesen wrote a graphical browser
for it at th university of illinois. All of a sudden the internet was full of twittering teenagers. President Eisenhower
is probably rolling over in this grave.

Research in operating system has also led to dramatic changes in practical systems. As we discussed earlier, the first
commercial computer systems were all batch systems, until MIT invented general purpose timesharing in the early 1960s.
Computers were all text-based until Doug Engelbart invented teh mouse and the graphical user interface at standford
research institute in the late 1960s. Who knows what will come next?

In this section and in comparable sections throughout the book, we will take a brief look at some of the research in
operating systems that has taken place during the past 5 to 10 years, just to give a flavor of what might be on the
horizon. This introduction is certainly not comprehensive. It is based largely on papers that have been published in
the top research conferences because these ideas have at least survived a rigorous peer review process in order to get
published. Note that in computer science - in contrast to other scientific fields - most research is published in
conferences, not in journals. Most of the papers cited in teh research sections were published by either ACM, the IEEE
computer society, or usenix and are available over the internet to (student) members of these organizations. For more
information about this organizations and their digital libraries, see

ACM                         http://www.acmorg todo
IEEE computer society       http://www.computer.org todo
USENIX                      http://www.usenix.org todo

Virtually all operating systems researchers realize that current operating systems are massive, inflexible, unreliable,
insecure, and loaded with bugs, certain ones more than others (named withheld here to protect the guilty).
Consequently, there is a lot of research on how to build better operating systems. Work has recently been published
about bugs and debugging, crash recovery, energy management, file and storage systems, high-performance i/o,
hyperthreading and multithreading, managing GPUs, memory management, multicore operating systems, operating system
correctness, operating system reliability, privacy and security, usage and performance monitoring, and virtualization
amount many other topics.

1.10 outline of the rest of this book

We have now completed our introduction and bird's eye view of the operating system. It is time to get down to the
details. As mentioned already, from the programmer's point of view, the primary purpose of an operating system is to
provide some key abstractions, hte most import of which are processes and threads, address spaces and files. Accordingly
the next three chapters are devoted to these topics.

Chapter 2 is about processes and threads. it discusses their properties and how they communicate with one another. It
also gives a number of detailed examples of how interprocess communication works and how to avoid some of the pitfalls.

In chapter 3 we will study address spaces and their adjunct, memory management, in detail. The important topic of
virtual memory will be examined, along with closely related concepts such as paging and segmentation.

Then in chapter 4, we come to the all important topic of the file systems. To a considerable extent, what the user sees
is largely the file system. We will look at both the file system interface and the file system implementation.

input/output is covered in chapter 5. The concepts of device independence and device dependence will be looked at.
Several important devices, including disks, keyboards, and displays, will be used as examples.

chapter 6 is about deadlocks, we briefly showed what deadlocks are in this chapter, but there is much more to sya. Ways
to prevent or avoid them are discussed.

At this point we will have completed our study of the basic principles of single-CPU operating systems. However, there
is more to say, especially about advanced topics. In chapter 7, we examine virtualization. We discuss both the
principles, and some of the existing virtualization solutions in detail. Since virtualization is heavily used in cloud
computing, we will also gaze at existing clouds. Another advanced topic is multiprocessor systems, including multicore,
parallel computers, and distributed systems. These subjects are converted in Chapter 8.

A hugely important subject is operating system security, which is covered in chapter 9. Among the topics discussed in
this chapter are threats (e.g., viruses and worms), protection mechanisms, and security models.

Next we have some case studies of real operating systems. These are unix, linix, and android, and windows 8. The next
concludes with some wisdom and thoughts about operating system design in chapter 12.

1.11 metric units

To avoid any confusion, it is worth stating explicitly that in this book, as in computer science in general, metric
unites are used instead of traditional english units (the furlong stone fortnight system). The principle metric prefixes
are listed in Fig 1-31. The prefix are typically abbreviated by their first letters, with the units greater than 1
capitalized. Thus a 1-TB database occupies 10^12 bytes of storage and a 1--psec (or 100ps) colock ticks every 10^-10
seconds. Since milli and micro both begin with the letter "m" a choice had to be made. Normally, "m" is for milli and
'u' is for th micro.

It is also worth pointing out that, in common industry practice, the units for measuring memory size have slightly
different meanings. There kilo means 2^10 (1024) rather than 10^3 (1000) because memories are always a power of two.
Thus a 1kb memory contains 1024 bytes and a 1-gb memory contains 2 ^30 (1,073,741,824) bytes, However, a 1kbps
communication line transmit 1000 bits per second and 10mbps lan runs at 10,000,000 bits/sec because these speeds are
not powers of two. Unfortunately, many people tend to mix up these two systems, especially for disk sizes. To avoid
ambiguity, in this book, we will use th symbols kb, mb and gb for 2^10, 2^20, and 2^30 bytes respectively and the
symbols Kbps, Mbps, and Gbps for 10^3, 10^6, 10^9 bits/sec, respectively.

1.12 summary

operating systems can be viewed form two viewpoints: resource managers and extended machines. In the resource manager
view, the operating system's job is to manage the different parts of the system efficiently. In the extended machine
view, the job of the system is to provide th users with abstractions that are more convenient to use than the actual
machine. These include processes, address spaces, and files.

operating systems have a long history, starting from the days when they replaced teh operator, to modern
multiprogramming systems. highlights include early batch system, multiprogramming systems, and personal computer
systems.

Since operating systems interact closely with the hardware, some knowledge of computer hardware is useful to
understanding them. Computers are built up of processors, memories, and i/o devices. These aprts are connected by
buses.

The basic concepts on which all operating systems are built are processes, memory management, i/o management, the file
system, and security. Each of these will be treated in a subsequent chapter.

The heart of any operating system is the set of system calls that it can handle. These tell what the operating system
really does. For unix, we have looked at the four groups of system calls. The first group of system calls relates to
processes creation and termination. The second group is for reading and writing files. The third groups is for directory
management. The fourth group contains miscellaneous calls.

Operating systems can be structured in several ways. The most common ones are as a monolithic system, a hierarchy of
layers, microkernel, client-server, virtual machine, or exokernel.
"""