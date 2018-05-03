"""
1.4 The operating system zoo

Operating system have been around now for over half a century. During this time, quite a variety of them have been
developed, not all of them widely known. In this section we will briefly touch upon nine of them. We will come back to
some of these different kinds of system later in teh book.

1.4.1 Mainframe operating systems

At the high end are the operating system for mainframes, those room-sized computers still found in major corporate data
centers. These computers differ from personal computers in terms of their i/o capacity. A mainframe with 1000 disks and
millions of gigabytes of data is not unusual; a personal computer with something of a comeback as high end web servers,
servers for large-scale electronic commerce sites, and servers for business to business transactions.

The operating systems for mainframes are heavily oriented toward processing many jobs at once, most of which need
prodigious amounts of i/o. They typically offer three kinds of services: batch, transaction processing, and timesharing.
A batch system is one that processes routine jobs without any interactive user present. Claims processing in an
insurance company or sales reporting for a chain of stores is typically done in batch mode. Transaction-processing at
a bank or airline reservations. Each unit of work is small, but the system must handle hundreds or thousands per
second. Timesharing systems allow multiple remote users to run jobs on the computer at once, such as querying a big
database. These functions are closely related; mainframe operating systems often perform all them them. An example
mainframe operating system is os/390, a descendant of os/360. However, mainframe operating system are gradually being
replaced by UNIX variants such as Linux.

1.4.2 Server operating systems

One level down are teh server operating systems. They run on servers, which are either very large personal computer,
workstations, or even mainframes. They serve multiple users at once over a network and allow the users to share
hardware and software resources, Servers can provide print service, file service, or Web service. Internet providers
run many server machines to support their customers and websites use servers to store the Web pages and handle the
incoming requests. Typical server operating systems are Solaris, FreeBSD, Linux and Windows Server 201x.

1.4.3 multiprocessor operating systems

An increasingly common way to get major-league computing power is to connect multiple CPUs into a single system.
Depending on precisely how they are connected and what is shred, these systems are called parallel computers,
multicomputers, or multiprocessors. They need special operating systems, but often these are variations on the server
operating systems, with special features for communication, connectivity, and consistency.

With the recent advent of multicore chips for personal computers, even conventional desktop and notebook operating
systems are starting to deal with at least small-scale multiprocessors and the number of cores is likely to grow over
time, Luckly, quite a bit is known about multiprocessor operating systems from years of previous research, so using
this knowledge in multicore systems should not be hard. The hard part will be having applications make use of all this
computing power. many popular operating systems, including windows and linux, run on multiprocessors.

1.4.4 personal computer operating systems

The next category is the personal computer operating system. Modern ones all support multiprogramming, often with dozens
of programs started up at boot time. Their job is to provide good support to a single user. They are widely used for
word processing, spreadsheets, games, and internet access. Common examples are linux, freeBSD, windows 7, windows 8 and
Apple's osx. personal computer operating systems are so widely known that probably little introduction is needed. In
fact, many people are not even aware that other kinds exist.

1.4.5 handheld computer operating systems

Continuing on down to smaller and smaller systems, we come to tables, smartphones and other handheld computers. A
handheld computer, originally known as a PDA (personal digit assistant), is a small computer that can be held in your
hand during operation. Smartphones and tablets are the best-known examples. As we have already seen, this market is
currently dominated by Google's Android and Apple's ios, but they have many competitors. Most of these devices boast
multicore CPUs and GPS, cameras and other sensors, copious amounts of memory, and sophisticated operating systems.
Moreover, all of them have more third-party application ("apps") then you can share a (USB) stick at.

1.4.6 Embedded operating systems

Embedded systems run on the computers that control devices that are not generally though of as computers and which do
not accept use-installed software. Typical examples are microwave ovens, TV sets, cares, DVD recorders, traditional
phones, and MP3 players. The main property which distinguishes embedded systems form handheld is the certainty that
no untrusted software will ever run on it. you cannot download new applications to your microwave oven - all the
software is in ROM. this means that there is no need for protection between applications, leading to design
simplification. Systems such as Embedded linux, QNX and VxWorks are popular in this domain.

1.4.7 Sensor-node operating systems

Networks of tiny sensor nodes are being deployed for numerous purposes. These nodes are tiny computers that communicate
with each other and with a base station using wireless communication. Sensor networks are used to protect the
perimeters of buildings, guard national borders, detect fires in forests, measure temperature and precipitation for
weather forecasting, glean information about enemy movements on battlefields, and much more.

The sensors are small battery-powered computers with built-in radios, they have limited power and must work for long
periods of time unattended outdoors, frequently in environmentally harsh conditions. The network mut be robust enough
to tolerate failures of individual nodes, which happen with ever-increasing frequency as the batteries begin to run
down.

Each sensor node is a real computer, with a CPU, RAM, ROM, and one or more environmental sensors. it runs a small, but
real operating system, usually one that is event driven, responding to external events or marking measurements
periodically based on an internal clock. The operating system has to be small and simple because the nodes have little
RAM and battery lifetime is a major issue. Also, as with embedded systems, all the programs are loaded in advance;
users do not suddenly start programs they downloaded from the internet, which makes the design much simpler. TinyOS is a
well-known operating system for a sensor node.

1.4.8 Rea-time operating systems

Another type of operating system is the real-time system. These systems are characterized by having time as a key
parameter. For example, in industrial process-control systems, real-time computers have to collect data about the
production process and use it to control machines in the factory. Often there are hard deadlines that must be met.
For example, if a car is moving down an assembly line, certain actions must take place at certain instants of time. If,
for example, a welding robot welds too early or too late, the car will be ruined. If the action absolutely must occur at
a certain moment (or within a certain range), we have a hard real-time system. Many of these are found in industrial
process control, avionics, military, and similar application areas. These systems must provide absolute guarantees that
a certain action will occur by a certain time.

A soft real-time system, is one where missing an occasional deadline, while not desirable, is acceptable and does not
cause any permanent damage. Digital audio or multimedia systems fall in this category. Smartphones are also soft
real-time systems.

Since meeting deadlines is crucial in (hard) real time system, sometimes the operating system is simply a library
linked in with the application programs, with everything tightly coupled and no protection between parts of the system.
An example of this type of real time syste is eCos.

The categories of handheld, embedded system, and real-time systems overlap considerably. Nearly all of them have at
least some soft real-time aspect.s The embedded and rea-time system run only software put in by the system designers;
user cannot add their own software, which makes protection easier. The handheld and embedded systems are intended for
consumers, whereas real time systems are more for industrial usage. Nevertheless, they have a certain amount in common.

1.4.9 smart card operating systems

The smallest operating system run on smart cards, which are credit card sized devices containing a CPU chip, they have
very severe processing power and memory constraints. Some are powered by contacts in the reader into which they are
inserted, but contactless smart card are inductively powered, which greatly limits what they can do. Some of them can
handle multiple functions. Often these are proprietary system.

Some smart cards are java oriented. This means that the ROM on the smart card holds an interpreter for teh Java Virtual
Machine (JVM). Java applets (small programs) are downloaded to the card and are interpreted by the JVM interpreter.
Some of these cards can handle multiple Java applets at the same time, leading to multiprogramming and the need to
schedule them. Resource management and protection also become an issue when two or more applets are present at teh same
time. These issues must be handled by the (usually extremely primitive) operating system present on the card.

1.5 Operating system concepts

Most operating systems provide certain basic concepts and abstractions such as processes, address spaces, and files
that are central to understand them. In th following sections, we will look at some of these basic concepts ever so
briefly, as an introduction. We will come back to each of them in great detail later in this book. To illustrate these
concepts we wil, from time to time, use examples, generally drawn from UNIX. Similar examples typically exist in other
systems as well, however, and we will study some of them later.

1.5.1 processes

A key concept in all operating systems is the process. A process is basically a program in execution. Associated with
each process is its address space, a list of memory locations from 0 to maximum, which teh process can read and write.
The address space contains the executable program, the program's data, and its stack. Also associated with each process
is a set of resources, commonly including registers (including the program counter and stack pointer), a list of open
files, outstanding alarms, lists of related process, and all the other information needed to run the program. A process
is fundamentally a container that holds all the information needed to run a program.

We will come back to the process concept in much more detail in chapter 2. For the time being, the easiest way to get
a good intuitive feel for a process is to think about a multiprogramming system. The user may have started a video
editing program and instructed it to convert a one-hour video to a certain format (something that can take hours) and
then gone off to surf the web. Meanwhile, a background process that wakes up periodically to check for incoming email
may have started running. Thus we have (at least) three active processes: the video editor, the web browser, and the
email receiver, Periodically, the operating system decides to stop running one process and start running another,
perhaps because the first one has used up more than its share of CPU time in the past seconds or two.

When a process is suspended temporarily like this, it must later be restarted in exactly the same state it had when it
was stopped. This means that all information about the process may hae several files open for reading at once.
Associated with each of these files is a pointer giving the current position (i.e., the number of the byte or record to
be read next). When a process is temporarily suspended, all these pointers must be read so that a read call executed
after the process is restarted will read teh proper data. In many operating systems, all the information about each
process, other than the contents of its own address space, is stored in an operating system table called teh process
table, which is an array of structures, one of each process currently in existence.

Thus, a (suspended) process consists of its address space, usually called the core image (in honor of the magnetic core
memories used in days of yore), and its process table entry, which contains the contents of its registers and many
other items needed to restart the process later.

The key process-management systems calls are those dealing with the creation and termination of processes. consider a
typical example. A process called the command interpreter or shell reads commands from a terminal. The user has just
typed a command requesting that a program be compiled. The shell must now create a new process that will run the
compiler. when that process has finished the compilation, it executes a system call to terminate itself.

If a process can create one or more other processes (referred to as child processes) and these processes in turn can
create child processes, we quickly arrive at teh process tree structure of Fig 1-13. Related processes that are
cooperating to get some job done often need to communicate with one another and synchronize their activities. This
communication is called interprocess communication, and will be addressed in detail in chapter 2.

Other process system calls are available to request more memory (or release unused memory), wait for a child process to
terminate, and overlay its program with a different one.

Occasionally, there is a need to convey information to running process that is not sitting around waiting for this
information. For example, a process that is communicating with another process on a different computer does so by
sending messages to the remote process over a computer network. To guard against the possibility that a message or its
reply is lost, the sender may request that its own operating system notify it after a specified number has been received
yet. After setting this timer, teh program may continue doing other work.

When teh specified number of seconds has elapsed, the operating system sends an alarm signal to the process. The signal
causes the process to temporarily suspend whatever ti was doing, save tis registers on teh stack, and start running a
special signal handling procedure, for example, to retransmit a presumably lost message. When the signal handler is
done, the running process is restarted in the state it was in just before the signal. signals are the software analog
of hardware interrupts and can be generated by a variety of causes in addition to timers expiring. Many traps detected
by hardware, such as executing an illegal instruction or using an invalid address, are also converted into signals to
the guilty process.

Each person authorized to use a system is assigned a UID (User Identification) by the system administrator. Every
process started has the UID of the person who started it. A child process has the same UID as its parent. Users can be
members of groups, each of which has a GID (Group Identification).

One UID, called the superuser (in NNIX), or administrator (in windows), has special power and amy override many of the
protection rules. In large installations, only the system administrator knows the password needed to become superuser,
but many of the ordinary users (especially students) devote considerable effort seeking flaws in the system that allow
them to become superuser without the password.

We will study process and interprocess communication in chapter 2.

1.5.2 Address Spaces

Every computer has some main memory that is uses to hold executing programs. In a very simple operating system, only
one program in the memory at a time. To run a second program, the first one has to be removed and the second one placed
in memory.

More sophisticated operating systems allow multiple programs to be in memory at teh same time. To keep them from
interfering with one another (and with the operating system), some kind of protection mechanism is needed. While this
mechanism has to be in the hardware, it is controlled by the operating system.

The above viewpoint is concerned with managing and protecting the computer's main memory. A different, but equally
important, memory related issue is managing the address space of the processes. Normally, each processes has some set of
addresses it can use, typically running from 0 up to some maximum. In the simplest case, the maximum amount of address
space a process has is less than the main memory. In this way, a process can fill up its address pace and there will be
enough room in main memory to hold it all.

However on many computers addresses are 32 or 64 bits, giving an address spaces of 2^32 or 2^64 bytes, respectively.
What happens if a process has more address space than the computer has main memory and the process wants to user it all?
In the first computers, such a process just out of luck. Nowadays, a technique called virtual memory exists, as
mentioned earlier, in which hte operating system keeps part of the address space in main memory and part on disk and
shuttles pieces back and forth between them as needed. In which the operating system creates teh abstraction of an
address space as the set of addresses a process may reference. The address space is decoupled from the machines physical
memory and space and physical memory from an important part of what an operating system does, so call of chapter 3 is
devoted to this topic.

1.5.3 Files

Another key concept supported by virtually all operating systems is the file system. As noted before, a major function
of the operating system is to hide the peculiarities of the disks and other i/o devices and present the programmer with
a nice, clean abstract model of device-independent files. System calls are obviously needed to create files, remove
files, read files. Before a file  can be read, it must be located on the disk and opened, and after being read it should
be closed. so calls are provided to do these things.

To provide a place to keep files, most PC operating systems have the concept of a directory as a way of grouping files
together. A student, for example, might have one directory for each course he is taking (for the programs needed for
that course), another directory for his electric mail, and still another directory for this World Wide Web home page.
System calls are needed to create and remove directories. Calls are also provided to put an existing file in a directory
and to remove a file from directory. Directory entries may be either files or other directories. This model also gives
rise to a hierarchy - the file system - as shown in Fig 1-14.

The process and file hierarchies both are organized as trees, but the similarity stops there. Process hierarchies
usually are not very deep (more than three level is unusual), whereas file hierarchies are commonly four, five, or even
more levels deep. Process hierarchies are typically short-lived, generally minutes at most, whereas the directory
hierarchy may exist for years. Ownership and protection also differ for processes and files. Typically, only a parent
process may control or even access a child process, but mechanisms nearly always exist to allow files and directories
to be read by a wider group than just the owner.

Every file within the directory hierarchy can be specified by giving its path name from the top directory hierarchy, the
root directory. such absolute path names consist of the list of directories that must be traversed from the root
directory to get the file, with slashes separating the components. In Fig 1-14, the path for file CS101 is /Faculty/
Prof.Brown/Course/CS101. The leading slash indicates that the path is absolute, that is, staring at the root directory.
As an aside, in windows, teh backslash (\) character is used as the separator instead of slash (/) character (for
historical reasons), so the file path given above would be written as \Faculty\Prof.Brown\Courses\CS101. Throughout
this book we will generally use the UNIX convention for paths.

At every instant, each process has a current working directory, in which path names not beginning with a slash are
looked for. For example, in Fig 1-14, if /Faculty/Prof.Brown were teh working directory, use of teh path Courses/CS101
would yield the same file as the absolute path name given above. Processes can change their working directory by
issuing a system call specifying the new working directory.

Before a file can be read or written, it must be opened, at which time the permission are checked. If the access
permitted, the system returns a small integer called file descriptor to use in subsequent operations. If the access is
prohibited, an error code is returned.

Another important concept in UNIX is the mounted file system. Most desktop computers has one or more optical drivers
into which CD-ROMs, DVDs, and Blue ray discs can be inserted. They almost always have USB port, into which USB memory
sticks (really, solid state disk drivers) can be plugged, and some computers have floppy disks or external hard disks.
To provide an elegant way to deal with these removable media UNIX allows the file system on the optical disc to be
attached to the main tree. Consider the situation of Fig 1-15(a). Before the mount call, the root file system, on the
hard disk, and a second file system, on a CD-ROM, are separate and unrelated.

However, the file system on the CD-ROM connot be sued, because there is no awy to specify path names on it. Unix does
not allow path names to be prefixed by a driver name or number; that would be precisely the kind of device dependence
that operating system ought to eliminate. Instead, the mount system call allows the file system on the CD-ROM to be
attached to the root file system wherever teh program wants it to be. In Fig 1-15(b) the file system on teh CD-ROM has
been mounted on directory b, thus allowing access to files /b/x and /b/y. If directory b had contained any files they
would refer to teh root directory of the CD-ROM. (not being able to access these files is not as serious as it as first
seems: file systems are nearly always mounted on empty directories.) If a system contains multiple hard disks, they can
all be mounted into a single tree as well.

Another important concept in Unix is the special file. Special files are provided in order to make i/o devices look like
files. That way, they can be read and written using the same system calls as are used for reading and writing files.
Two kinds special files exist: block special files and character special files. Block special files are used to model
devices that consist of a collection of randomly addressable blocks, such as disks. By opening a block special file and
reading, say block 4, a program can directly access teh fourth block on teh device, without regard to the structure of
the file system contained on it. Similarly, character special files are used to model printers, modems, and other device
that accept or output a character steam. by convention, the special files are kept in hte /dev directory. For example,
/dev/lp might be teh print (once called the line printer).

The last feature we will discuss in this overview relates to both processes and files: pipes. A pile is a sort of
pseudofile tht can be used to connect two processes, as shown in Fig 1-16. If processes A and B with to talk using a
pipe, they must set it up in advance. When process A want to send data to process B, it writes on the pipe as through it
were an output file. In fact, the implementation of a pipe is very much like that of a file. Process B can read the data
by reading from teh pipe as though it were an input of a file. Thus, communication between processes in Unix looks very
much like ordinary file reads and writes. Stronger yet, the only way a process and discover that the output file it is
writing on is not really a file, but a pipe, is by making a special system call. File systems are very important. We
will have much more to say about them in chapter 4. And also in chapter 10 and 11.

1.5.4 Input/output

All computers have physical devices for acquiring input and producing output. After all, what good would a computer be
if the user could not tell it what to do and could not get the result after it did the work requested? nay kinds of
input and output devices exist, including keyboards, monitors, printers, and so on. it is up to the operating system to
manage these devices.

Consequently, every operating system has an i/o subsystem for managing its i/o devices, some of the i/o software is
devices independent,that is, applies to many or all i/o devices equally well. Other parts of it, such as device drivers,
are specific to particular i/o devices. in chapter 5 we will have a look at i/o software.

1.5.5 protection

Computers contain large amounts of information tht users often want to protect and keep confidential. This information
may include email, business plans, tax returns, and much more. It is up to the operating system to manage the system
security so that files, for example, are accessible only to authorized users.

As a simple example, just to get an idea of how security can work, consider unix. files in unix are protected by
assigning each one a 9-bit binary protection code. The protection code consists of three 3-bit fields. one for the
owner, one for other member of owner's group (user are divided into groups by teh system administrator), and one for
everyone else, Each fields has a bit for read access, a bit for write access, and a bit for execute access. These 3 bits
are known as the rwx bits. For example, the protection code rwxr-x--x means that the owner can read, write, or execute
the file, other group members can read or execute (but not write) the file, and  everyone else can execute (but not read
or write) the file. For a directory x indicates search permission. A dash means that the corresponding permission is
absent.

In addition to file protection, there are many other security issue. Protecting the system from unwanted intruders,
both human and nonhuman (e.g,. viruses) is one of them. We will look at various security issues in chapter 9.

1.5.6 The shell

The operating system is the code that carries out the system  calls. Editors, compilers, assemblers, linkers, utility
programs, and command interpreters definitely are not part of the operating system, even though they are important and
useful. At the risk of confusing things somewhat, in this section we will look briefly at the unix command interpreter,
the shell. Although it is not part of the operating system, it makes heavy use of many operating system features and
thus serves as a good example of how the system calls are used. it is also the main interfaces between a user sitting at
his terminal and the operating system, unless the user is suing a graphical user interface. many shells exist, including
sh, csh, ksh, and bash. All of them support the functionality described below, which derives from the original shell
(sh).

When any user logs in, a shell is started up. The shell has the terminal as standard input and standard output. it
starts out by typing the prompt, a character such as a dollar sign, which tell the user that the shell is waiting to
accept a command. if teh user now types

data

for example, teh shell creates a child process and run teh date program as teh child. While the child process is running
the shell waits for it to terminate. When the child finishes, the shell types teh prompt again and tires to read the
next input line.

The user can specify that standard output be redirected to a file, for example,

date > file

similarly, standard input can be redirected, as in

sort <file1 > file2

which invokes the sort program with input taken from file1 and output send to file2..

The ouput of one program can be used as the input for another program by connecting them with a pipe. thus

cat file1 file2 file2 | sort >/dev/lp

invokes the cat program to concatenate three files and send the output to sort to arrange all the lines in alphabetical
order. The output of sort is redirected to the file /dev/lp, typically the printer.

If a user puts an ampersand after a command, the shell does not wait for it to complete. Instead it just gives a prompt
immediately. Consequently,

cat file1 file2 file3 | sort >/dev/lp &

start up the sort as a background job, allowing the user to continue working normally while the sort is going on. The
shell has a number of other interesting features, which we do not have space to discuss here. Most books on Unix discuss
the shell at some length (e.g. Kernighan and Pike, 1984; Quigley, 2004; Robbins, 2005).

Most personal computers these days use a GUI, In fact, the GUI is just a program running on top of the operating system,
like a shell. In Linux systems, this fact is made obvious because the user has a choice of (at least) two GUIs: Gnome
and KDE or none at all (using a terminal window on X11). In windows, it is also possible to replace the standard GUI
desktop (Windows Explorer) with a different program by changing some values in the registry, although few people do
this.

1.5.7 Ontogeny Recapitulates phylogeny

After Charles Darwin's book on the top origin of the species was published, the German zoologist Ernst Haeckel stated
that "ontogeny recapitulates phylogeny." By this he meant that development of an embryo (ontogeny) repeats (e.g.,
recapitulates) teh evolution of the species (phylogeny). In other words, after fertilization, a human egg goes through
stages of being a fish, a pig, and so on before turning into a human baby. Modern biologists regards this as a gross
simplification, but it still has a kernel of truth in it.

Something vaguely analogous has happened in the computer industry. Each new species (mainframe, minicomputer, personal
computer, handheld, embedded computer, smart card. etc) seems to go through the development that its ancestors did,
both in hardware and in software. We often forget that much of what happens in the computer business and a lot of
other fields is technology driven. The reason teh ancient Romans lacked cars is not that they liked walking so much.
It is because they did not know how to build cars. Personal customers exist not because millions of people have a
centuries old pent up desire to own a computer, but because it is now possible to manufacture them cheaply. We often
forget how much technology affects our view of systems and it is worth reflecting on this point from time to time.

In particular, it frequently happens that a change in technology renders some idea obsolete and it quickly vanishes.
however, another chane in technology could revive it again. This is especially true when the change has to do with the
relative performance of different parts of the system. For instance, when CPUs became much faster than memories, caches
became important to speed up the "slow" memory. If new memory technology someday makes memories much faster than CPUs,
caches will vanish. And if a new CPU technology makes them faster than memories again, caches will reappear. In biology
extinction is forever, but in computer science it is sometimes only for a few years.

As a consequence of this impermanence,in this book we will from time to time look at "obsolete" concepts, that is,
ideas that are not optimal with current technology. However, changes in the technology may bring back some of the
so called "obsolete concepts". For this reason, it is important to understand why a concept is obsolete and what
changes in the environment might bring it back again.

To make this point clear, let us consider a simple example. Early computers had hardwired instruction sets. The
instructions were executed directly by hardware and could not be changed. Then came microprogramming (first introduced
on a large scale with the IBM 360), in which an underlying interpreter carried out the "hardware instructions" in
software. Hardwired execution became obsolete. it was not flexible enough. Then RISC computers were invented, and
microprogramming (i,e, interpreted execution) became obsolete because direct execution was faster. now we are seeing the
resurgence of interpretation in the form of java applets that are send over the internet and interpreted upon arrival.
Execution speed is not always crucial because network delays are so great that they tend to dominate. Thus teh pendulum
has already swung several cycles between direct execution and interpretation and may yet swing again in the future.

Large Memories

let us now examine some historical developments in hardware and how they have affected software repeatedly. The first
mainframes had limited memory. A fully loaded IMB 7090 or 7094, which played king of the mountain from late 1959 until
1964, had just over 128 kb of memory. it was mostly programmed in assembly language and its operating system was
written in assembly language to save precious memory.

At time went on, compilers for languages like Fortran and cobol got good enough that assembly language was pronounced
dead. but when the first commercial minicomputer was released, it has only 4096 19-bit words of memory, and assembly
language made a surprise comeback. Eventually, minicomputers acquired more memory and high-level language became
prevalent on them.

When microcomputers hit iin the early 1980s, the first ones had 4-kb memories and assembly language programing rose from
teh dead. Embedded computer often use the same CPU chips as the microcomputers (8080s, Z80s, and later 8086s0 and were
also programmed in assembler initially. Now their descendants, the personal computers, have lots of memory and are
programmed in c, c++, java, and other high-level languages, smart cards are undergoing a similar development, although
beyond a certain size, the smart cards often have a java interpreter and execute java programs interpretively, rather
than having java being compiled to the smart card's machine language.

Protection hardware

Early mainframes, like IBM 7090/7094, had no protection hardware, so they just run one program at a time. A buggy
program could wipe out the operating system and easily crash the machine. with the introduction of the IBM 360, a
primitive form of hardware protection became available. these machines could then hold several program in memory at the
same time and let them take turn running (multiprogramming). monoprogramming was declared obsolete.

At least until the first minicomputer showed up - without protection hardware - so multiprogramming was not possible.
Although the PDP-1 and PDP-8 had no protection hardware, eventually the PDP-11 did, and this feature led to
multiprogramming and eventually to unix.

When teh first microcomputers were built, hey used the intel 8080 CPU chip, which had no hardware protection, so we were
back to monoprogramming - one program ini memory at a time. It ws not until the intel 80286 chip that protection
hardware was added and multiprogramming became possible. Until this day, many embedded systems have no protection
hardware and run just a single program.

now let us look at operating systems. The first mainframes initially had no protection hardware and no support for
multiprogramming, so they run simple operating system that handled one manually loaded program at a time. later they
acquired the hardware and operating system support to handle multiple programs at once, and then full timesharing
capabilities.

When minicomputers first appeared, they also had no protection hardware and run one manually loaded program at a time,
even though multiprogramming was well established in the mainframe world by then. Gradually, they acquired protection
hardware and the ability to run two or more programs at once. The first microcomputer were also capable of running
only one program at a time, but later acquired the ability to multiprogramming. Handheld computers and samrt cards went
the same route.

In all cases, the software development was dictated by technology. The first microcomputers, for example, had something
like 4kb of memory and no protection hardware. high-level languages and multiprogramming were simply too much for such
a tiny system to handle. As the microcomputers evolve into modern personal computers, they acquired the necessary
hardware and then the necessary software to handle more advanced features. It is likely that this development will
continue for years to come. Other fields may also have this wheel of reicarnation, but in the computer industry it
seems to spin faster.

Disks

Early mainframes were largely magnetic tape based. They would read in a program from tape, compile it, run it, and write
the result back to another tape. There were no disks and no concept of a file system. That began to change when IBM
introduced the first hard disk - the RAMAC 9RAndoM ACcess) in 1956. it occupied about 4 square meters of floor space and
could store 6 million 7-bit characters, enough for one medium-resolution digital photo. But with an annual rental fee of
$35,000, assembling enough of them to store the equivalent of a roll of film got pricey quite fast. But eventually
prices came down and primitive files systems were developed.

Typical of these new developments was teh CDC 6600, introduced in 1964 and for years by far teh fastest computer in the
world. Users could create so called "permanent files" by giving then names and hoping that no other user ahd also
decided that, say "data" was suitable name for a file. This was a single-level directory. Eventually, mainframes
developed complex hierarchical file systems. perhaps culminating the MULTICS file sytem.

As minicomputers come into use, they eventually also had hard disks, The standard disk on the PDP - 11 when it was
introduced in 1970 was teh RK05 disk, with a capacity of 2.5 mb, about half of the IMB RAMAC, but it was only about
40 cm in diameter and 5 cm high. But it too, had a single-level directory initially. When microcomputers came out, CP/M
ws initially the dominant operating system, and it, too. supported just one directory on the (floppy) disk.

Virtual memory

Virtual memory (discussed in chapter 3) gives the ability to urn programs larger than the machine's physical memory by
rapidly moving pieces back and forth between RAM and disk. it underwent a similar development, first appearing on
mainframes, then moving to the minis, and the micros. Virtual memory also allowed having a program dynamically link in
a library at run time instead of having it compiled in. MULTICS was the first system to allow this. Eventually, the idea
propagated down the line and is now widely used on most UNIX and windows systems.

In all these developments, we see ideas, invented in one context and later thrown out when the context changes (assembly
language programming, monoprogramming, single-level directories, etc) only to reappear in a different context often a
decade later. For this reason in this book we will sometimes look at ideas and algorithms that may seen dated on today's
gigabyte PCs, but which may soon come back on embedded computers and smart cards.
"""