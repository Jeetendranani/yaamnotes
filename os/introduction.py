"""
1. Introduction

A modern computer consists of one or more processors, some main memory, disk, printers, a keyboard, a mouse, a display,
network interfaces, and various other input/output devices. All n all, a complex system.oo if every application
programmer had to understand how all these things work in detail, no code would ever get written. Furthermore, managing
all these components and using them optimally is an exceedingly challenging job. For this reason, computers are
equipped with a layer of software called the operating system, whose job is to provide user programs with a better,
simpler, cleaner, model of the computer and to handle managing all the resources just mentioned. Operating systems are
the subject of this book.

Most readers will have had some experience with an operating system such as Windows, Linux, FreeBSD, or OSX, but
appearances can e deceiving. The program that users interact with, usually called the shell when it is text based and
the GUI (Graphical User Interface) - which is pronounced "gooey" - when it uses icons, is actually not part of the
operating system, although it uses the operating system to get its work done.

A simple overview of the main components under discussion here is given in Fig 1-1. Here we see the hardware at the
bottom. The hardware consists of chips, boards, disks, a keyboard, a monitor, and similar physical objects. On top of
the hardware is the software. most computers have two modes of operation: kernel mode and user mode. The operating
system, the most fundamental piece of software, runs in kernel mode (also called supervisor mode). In this mode it has
complete access to all the hardware and can execute any instruction the machine is capable to executing. The rest of the
software runs in user mode, in which only a subset of teh machine instructions is available. In particular, those
instructions that affect control of the machine or do i/o "input/output" are forbidden to user-mode programs. We will
come back to the difference between kernel mode and user mode repeatedly throughout this book. It plays a crucial role
in how operating systems work.

This user interface program, shell or GUI, is hte lowest level of user-mode software, and allows the user to start other
programs, such as a web browser, email reader, or music player. These programs, too, make heavy use of the operating
system.

The placement of the operating system is shown in Fig 1-1. It runs on the bare hardware and provides the base for all
the other software.

An important distinction between the operating system and normal (user mode) software is that if a user does not like
a particular email reader, here is free to get a different one or write his own if he so chooses; he is not free to
write his own clock interrupt handler, which is part of the operating system and it protected by hardware against
attempts by users to modify it.

This distinction, however, is sometimes blurred in embedded systems (which may not have kernel mode) or interpreted
systems (such as Java-based systems that use interpretation, not hardware, to separate the components).

Also, in many systems there are programs that run in user mode but help the operating system or perform privileged
functions. For example, there is often a program that allows users to change their passwords. It is not part of the
operating system and does not run in kernel mode, but it clearly carries out a sensitive function and has to be
protected in a special way. In some systems, this idea is carried to an extreme, and pieces of what is traditionally
considered to be the operating system (such as the file system) run in user space. In such systems, it is difficult to
draw a clear boundary. Everything running in kernel mode is clearly part of the operating system, but some programs
running outside it are arguably also part of it, or at least closely associated with it.

Operating systems differ from user (i.e., application) programs in ways other than where they reside. In particular,
In they are huge, complex, and long-lived. The source code of the heart of an operating system like linux or Windows
is on the order of five million lines of code or more. To conceive of what this means, think of printing out five
million lines in book from, with 50 lines per page and 1000 pages per volume (larger than this book). It would take
100 volumes to list an operating system of this size - essentially an entire bookcase, Can you imagine getting a job
maintaining an operating system and on the first day having your boss bring you to a bookcase with the code and say:
"Go learn that." And this is only for the part runs in the kernel. When essential shared libraries are included,
Windows is well over 70 million lines of code or 10 or 20 bookcases. And this excludes basic application software
(things like windows explore, windows media player, and so on).

It should be clear now why operating systems live a long time - they are very hard to write, and having written one, the
owner is loath to throw it out and start again. Instead, such system evolve over long periods of time. Windows 95/98/Me
was basically one operating system and windows nt/2000/xp/vista/windows 7 is a different one. They look similar to the
users because microsoft made very sure that the user interface of windows 2000/xp/vista/windows 7 was quite similar to
that of the system it was replacing, mostly windows 98. nevertheless, there were very good reasons why microsoft got rid
of windows 98. We will come to these when we study windows in detail in chap. 11.

Besides windows, the other main example we will use throughout this book is unix and its variants and clones. It, too,
has evolved over the years, with versions like system v, solaris, and freeBSD being derived from the original system,
whereas Linux is a fresh code base, although very closely modeled on Unix and highly compatible with it. We will use
examples from UNIX throughout this book and look at Linux in the detail in chapter 10.

In this chapter we will briefly touch on a number of key aspects of operating systems, including what they are, their
history, what kinds are around, some of the basic concepts, and their structure. We will come back to many of these
important topics in later chapters in more detail.

1.1 What is an operating system?

It is hard to pin down what an operating system is other than saying it is the software that runs in kernel mode - and
even that is not always true, part of the problem is that operating system perform two essentially unrelated functions:
providing application programmers (and application programs, naturally) a clean abstract set of resources. Depending on
who is doing the talking, you might hear mostly about one function or other. Lets now look at both.

1.1.1 The operating system as an extended machine

The architecture (instruction set, memory organization, i/o, and bus structure) of most computers at the machine
language level is primitive and awkward to program, especially for input/output. To make this point more concrete,
consider modern sata (serial ata) hard disks used on most computers. A book (anderson, 2007) describing an early version
of the interface to the disk - what a programmer would have to know to use the disk - ran over 450 pages. Since then
teh interface has been revised multiple times and its more complicated than it was in 2007. Clearly no sane programmer
would want to deal with this disk at teh hardware level, instead, a piece of software, called a disk driver, deals with
the hardware and the provides an interface to read and write disk blocks, without getting into the details. Operating
systems contains many drivers for controlling i/o devices.

but even this level is much too low for most applications. For this reason, all operating systems provide yet another
layer of abstraction for using disks: files. using this abstraction, programs can create, write, and read files,
without having to deal with the messy details of how the hardware actually works.

This abstraction is the key to managing all this complexity. good abstractions turn a nealy impossible task into two
manageable ones. The first is defining and implementing the abstractions. The second is using these abstractions to
solve the problem at hand. One abstraction that almost every computer user understands is the file, as mentioned above.
It is a useful piece of information, such as digital photo, saved email message, song, or web page. It is much easier
to deal with photos, emails. songs, and web pages than with the detail of sata (or other) disks. The job of the
operating system is to create good abstractions and then implement and mange the abstract objects thus created.

This point is so important that it is worth repeating in different words. with all due respect to the industrial
engineers who so carefully designed the macintosh, hardware is ugly, real processors, memories, disks, and other devices
are very complicated and present difficult, awkward, idiosyncratic, and inconsistent interfaces to the people who
have to write software to sue them. sometimes this is due to the need for backward compatibility with older hardware.
Other times it is attempt to save money. Often, however, teh hardware designers do not realize (or care) how much
trouble they are causing for the software. One of the major tasks of the operating system is to hide the hardware and
present programs (and their programmers) with nice, clean, elegant, consistent, abstractions to work with instead.
Operating systems turn teh ugly into the beautiful. as shown in Fig. 1-2.

It should be noted that the operating system's real customers are the application programs (via the application
programmers, of course). They ar the ones who deal directly with the operating system and its abstractions. In contrast,
end users deal with the abstractions provided by the user interface, either a command line shell or a graphical
interface. While the abstractions at the user interface may be similar to the ones provided by the operating system,
this is not always the case. To make this point clearer, consider the normal windows desktop and the line-oriented
command-line prompt. both are programs running on the windows operating system and use the abstractions windows
provides, but they offer very different user interfaces. Similarly, a linux user running Gnome or KDE sees a very
different interface than a Linux user working directly on top of the underlying X windows System, but the underlying
operating system abstractions are the same in both cases.

In this book, we will study the abstractions provided to application programs in great detail, but say rather little
about user interfaces. That is a large and important subject, but one only peripherally related to operating systems.

1.1.2. the operating system as a resource manager

the concept of an operating system as primarily providing abstractions to application programs is a top down view. An
alternative bottom up, view holds that teh operating system is there to manage all teh pieces of a complex system.
Modern computers consist of processors, memories timers, mice, network interfaces, printers, and wide variety of other
devices. In the bottom up view, the job of the operating system is to provide for an orderly and controlled allocation
of the processors, memories, and i/o devices among the various programs wanting them.

Modern operating systems allow multiple programs to be in memory and run at the same time. Imagine what would happen if
three programs running on the some computer all tried to print there output simultaneously on the sam printer. The first
few lines of printout might be from program 1, teh next few from program 2, then some from program 3, and so forth. The
result would be utter chaos. The operating system can bring order to the potential chaos by buffering all the output
destined for the printer on the disk. When one program is finished, the operating system can then copy its output from
the disk file where it has been stored from the printer, while at the same time the other program can continue
generating more output, oblivious to the fact that the output is not really going to the printer (yet).

When a computer (or network) has more than one user, the need for managing and protecting the memory, i/o devices, and
other resources is even more since the user might otherwise interface with one another. In addition, users often need to
share not only hardware, but information (files, databases, etc.) as well. In short, this view of the operating system
holds that its primary task is to keep track of which programs are using which resource, to grant resource requests, to
account for usage, and to mediate conflicting requests from different programs and users.

Resource management includes multiplexing (sharing) resources in two different ways: in time and space. When a resource
is time multiplexed, different programs or users take turns using it. First one of them gets to use the resource, then
another, and so on. For example, with only one CPU and multiple programs that want to run on it. The operating system
first allocates the CPU to one program, then after it has run long enough, another program gets to use the CPU, then
another, and then eventually the first one again. Determining how the resource is time multiplexed = who goes next and
for how long - is the task of the operating system. Another example of time multiplexing is share the printer. When
multiple print jobs are queued up for printing on a single printer, a decision has to be made about which one is to
be printed next.

The other kind of multiplexing is space multiplexing. Instead of the customers taking turns, each one gets part of the
resource. For example, main memory is normally divided up among several running programs, so each one can be resident at
the same time (for example, in order to take turns using the CPU). Assuming there is enough memory to hold multiple
programs, it is most efficient to hold several programs in memory at once rather than give on eof them all of it,
especially if it only needs a small fraction fo the total. Of course, this raises issues of fairness, protection, and so
on, and it is up to the operating system to solve them. Another resource that is space multiplexed is the disk. In many
systems a single disk can hold files from many users at the same time. Allocating disk space and keeping track of who
is using which disk blocks is a typical operating system task.

1.2 history of operating systems

Operating systems have been evolving through the years. in the following sections we will briefly look at the few of the
highlights. Since operating systems have historically been closely tied to the architecture of the computers on which
they run, we will look at successive generations of computers to see what their operating system were like. This mapping
of operating system generations to computer generations is crude, but it does provide some structure where there would
otherwise be none.

The progression given below is largely chronological, but it has been a bumpy ride. Each development did not wait until
the previous one nicely finished before getting started. There was a lot of overlap, not to mention many false starts
and dead ends. Take this as a guide, not as the last word.

The first true digital computer was designed by the English mathematician Charles Babbage (1792 - 1871). Although
Babbage spend most of his life and fortune trying to build his "analytical engine," he never got it working properly
because it was purely mechanical, and the technology of his day could not produce the required wheels, gears, and cogs
to the high precision that he needed. Needless to say, the analytical engine did not have an operating system.

As an interesting historical aside, Babbage realized that he would need software for his analytical engine, so he hired
a young woman named Ada Lovelace, who was the daughter of the famed British peot Lord Byron, as the world's first
programmer, the programming language Ada is named after her.

1.2.1 The first generation (1945-55): Vacuum Tubes

After Babbage's unsuccessful efforts, little progress was made in constructing digital computers until the word war II
period, which stimulated an explosion of activity. Professor John Atanasoff and his graduate student Clifford Berry
built what is now regarded as the first functioning digital computer at Iowa State University. It used 300 vacuum tubes.
At roughly the same time, Konrad Zuse in Berlin built the Z3 computer out of electromechanical relays. in 1944, the
Colossus was built and programmed by a group if scientists (including Alan Turing) at Bletchley Park, England, the mark
I was built by Howard Aiken at Harvard, and teh ENIAC was built by William Mauchley and this graduate student J.
Presper Eckert at teh University of Pennsylvania. Some were binary, some used vacuum tubes, some were programmable, but
all were very primitive and took seconds to perform even the simplest calculation.


In these early days, a single group of people (usually engineers) designed, built, programmed, operated, and
maintained each machine. All programming was done in absolute machine language, or even worse yet, by wiring up
electrical circuits by connecting thousands of cables to plug boards to control the machine's basic functions.
Programming languages were unknown (even assembly language was unknown). Operating systems were unheard of. The usual
mode of operation was for the programmer to sing up for a block of time using the signup sheet on the wall, then come
down to the machine room, insert his or her plug board into the computer, and spend the next few hours hoping that none
of 20000 or so vacuum tubes would burn out during the run. Virtually all the problems were simple straightforward
mathematical and numerical calculations, such as grinding out tables sines, cosines, and logarithms, or computing
artillery trajectories.

By the early 1950s, the routine had improved somewhat with the introduction of punched cards. it was now possible to
write programs on cards and read them in instead of using plug boards; otherwise, the procedure was the same.

1.2.2 The second generation 1955-65): Transistors and Batch Systems

The introduction of the transistor in the mid-1950s changed teh picture radically. Computers became reliable enough
that they could be manufactured and sold to paying customers with the expectation that they would continue to function
long enough to get some useful work down. For the first time, there was a clear separation between designers, builders,
operators, programmers, and maintenance personal.

These machines, now called mainframes, were locked away in large, specially are-conditioned computer rooms, with staffs
of professional operators to run them. Only large corporations or major government agencies or universities could
afford the multi million dollar price tag. To run a job (i.e., a program or set of programs), a programmer would first
write the program on paper (in Fortran or assembler), then punch it on the cords. He would then bring the card deck
down to the input room and hand it to one of hte operators and go drink coffee until the output was ready.

When the computer finished whatever job it was currently running, an operator would go over the printer and tear off the
output and carry it over to the output room, so that the programmer could collect it later. Then he would take one of
the card decks that had been brought from the input rand read it in. If the fortran compiler was needed, the operator
would have to get it from a file cabinet and read it in. Much computer time was wasted while operators were walking
around the machine room.

Given the high cost of the equipment, it is not surprising that people quickly looked for ways to reduce the wasted
time. The solution generally adopted was the batch system. The idea behind it was to collect a tray full of jobs in the
input room and then read them onto a magnetic tape using a small (relatively) inexpensive computer, such as IBM 1401,
which was quite good at readign cards, copying tapes, and printing output, but not at all good at numerical calculations
Other, much more expensive machines, such as the IBM 7094, were used for the real computing. This situation is shown
in Fig. 1-3.

After about an hour of collecting a batch of jobs, the cards were read onto a magnetic tape. which was carried into the
machine room. Where it was mounted on a tape drive. The operator then loaded a special program (the ancestor of today's
operating system), which read the first job from tape and run it. The output was written onto a second tap, instead of
being printed. After each job finished, the operating system automatically read the next job from the tape and began
running it. When the whole batch was done, the operator removed the input and output tapes, replaced the input tape
with the next batch, and brought the output tape to a 1401 for printing offline (ie.g, not connected to the main
computer.)

The structure of a typical input job is shown in Fig. 1-4. It started out with a $JOB card, specifying the maximum run
time in minutes, the account number to be charged, and the programmer's name. Then came a $FORTRAN card, telling the
operating system to load the FORTRAN compiler from the system tape. It was directly followed by the program to be
compiled, and then a $LOAD card, directing the operating system to load the object program just compiled. (Compiled
programs were often written on scratch tapes and had to be loaded explicitly.) Next came the $RUN card, telling the
operating system to run the program with the data following it. Finally, the $END card marked the end of the job. These
primitive control cards were teh forerunners of modern shells and command-line interpreters.

Large second-generation computers were used mostly for scientific and engineering calculations, such as solving the
partial differential equations that often occur in physics and engineering. They were largely programmed in Fortran
and assembly language. Typical operating systems were FMS (the Fortran Monitor System) and IBSYS, IBM's operating
system for the 7094.

1.2.3 The third generation (1965-80): ICs and multiprogramming

By teh early 1960s, most computer manufacturer had two distinct, incompatible, product lines. On the one hand, there
were the word-oriented, large-scale scientific computers, such as the 7094, which were used for industrial-strength
numerical calculations in science and engineering. On the other hand, there were the character-oriented, commercial
computers, such as the 1401, which were widely used for tape sorting and printing by banks and insurance companies.

Developing and maintaining two completely different product lines was expensive proposition for the manufacturers. In
addition, many new computer customers initially needed a small machine but later outgrew it and wanted a bigger machine
that would run all their old programs, but faster.

IBM attempted to solve both of these problems at a single stroke by introducing the system/360. The 360 was a series of
software-compatible machines ranging from 1401-sized models to much larger ones, more powerful then the mighty 7094.
The machines differed only in price and performance (maximum memory, processor speed, number of i/o devices permitted,
and so forth). Since they all had the same architecture and instruction set, programs written for one machine could
run on all the others - at least in theory. (But as yogi Berra reputedly said: "In theory, theory and practice are the
same; in practice, they are not." Since the 360 was designed to handle both scientific (i.e., numerical) anc commercial
computing, a single family of machines could satisfy the needs of all customers. In subsequent years, IBM came out
with backward compatible successors to the 360 line, using more modern technology, known as the 370, 4300, 3080, and
3090. The zSeries is the most recent descendant of this line, although it has diverged considerably from the original.
The IBM 360 was the first major computer line to sue (small-scale) ics (integrated circuits), thus providing a major
price/performance advantage over the second generation machines, which were built up from individual transistors. it was
an immediate success, and the idea of a family of compatible computers was soon adopted by all the other major
manufacturers. The descendants of these machines are still in use at computer centers today. Nowadays they are often
used for managing huge databases (e.g., for airline reservation systems) or as servers for World Wide Web sites that
must process thousands of requests per second.

The greatest strength of the "single-family" idea was simultaneously its greatest weakness. The original intention was
that all software, including the operating system, OS/360, had to work on all models. It had to run on small systems,
which often just replaced 1401s for copying cards to tape, and on very large systems, which often replaced 7094s for
doing weather forecasting and other heavy computing. It had to be good on systems with few peripherals and on systems
with many peripherals. It had to work in commercial environments and in scientific environments. Above all, it had to
be efficient for all of these different uses.

There was no way that IBM (or anybody else for that matter) could write a piece of software to meet all those
conflicting requirements. The result was an enormous and extraordinarily complex operating system, probably two to three
orders of magnitude large than FMS. It consisted of millions of lines of assembly language written by thousands of
programmers, and contained thousands upon thousands of bugs, which necessitated a continuous stream of new releases in
an attempt to correct them. Each new release fixed some bugs and introduced new ones, so the number of bugs probably
remained constant over time.

One of the designers of OS/360, Fred Brooks, subsequently wrote a witty and incisive book (Brooks, 1995) describing
his experiences with OS/360. While it would be impossible to summarize the book here, suffice it to say that the cover
shows a herd of prehistoric beasts stuck in a tar pit. The cover of Silberschatz  et al. (2012) makes a similar point
about operating systems being dinosaurs.

Despite its enormous sie and problems, OS/360 and the similar third-generation operating systems produced by other
computer manufacturers actually satisfied most of their customers reasonably well. They also popularized several key
techniques absent in second-generation operationg systems. Probably the most important of these was multiprogramming.
On the 7094, when the current job paused to wait for a tape or other i/o operation to complete, the CPU simply stay
idle until the i/o finished. With heavily cpu bound scientific calculation, i/o is infrequent, so this wasted time is
not significant. With commercial data processing, the i/o wait time can often 80% or 90% of the total time, so something
had to be done to avoid having the (expensive) CPU be ideal so much.

The solution that evolved was to partition memory into several pieces, with a different job in each partition, as
shown in Fig 1-5. While one job was waiting for i/o to complete, another job could be suing the CPU. If enough jobs
could be hold in memory at once, the CPU could be kept busy nearly 100% of the time. Having multiple jobs safely in
memory at once requires special hardware to protect each job against snooping and mischief by other ones, but the 360
and other third-generation systems were equipped with this hardware.

Another major feature present in third-generation operating systems was the ability to read jobs from cards onto the
disk as soon as they were brought to the computer room. Then, whenever a running job finished, the operating system
could load a new job from the disk into the now-empty partition and run it. This technique is called spooling (from
Simultaneous Peripheral Operation On Line) and was also used for output. With spooling, the 1401s wre no longer needed,
and much carrying of tapes disappeared.

Although third-generation operating systems were well suited for big scientific calculations and massive commercial
data-processing runs, they were still basically batch system. many programmers pined fro the first-generation days when
they had the machine all to themselves for a few hours, so they could debug their programs quickly. With
third-generation systems, the time between submitting a job and getting back the output was often several hours, so
a single misplaced comma could cause a compilation to fail, and the programmer to waste half a day. Programmers did not
like that very mch.

This desire for quick response time paved teh way for timesharing, a variant of multiprogramming, in which each user has
an online terminal. In a timesharing system, if 20 users are logged in and 17 of them are thinking or talking or
drinking coffee, the CPU can be allocated in turn to the tree jobs that want services. Since people debugging programs
usually issue short commands (e.g., compile a five page procedure) rather than long ones (e.g. sort a million-record
file), the computer can provide fast, interactive service to number of users and perhaps also work on big batch jobs
in the background when the CPU is otherwise idle. The first general-purpose timesharing system. CTSS (Compatible Time
Sharing System), was developed at MIT on a specially modified 7094. However, timesharing did not really become popular
until the necessary protection hardware became widespread during the third generation.

After teh success fo the CTSS system, MIT Bell labs, and general Electric ( at that time a major computer manufacturer)
decided to embark on the development of a "computer utility," that is, a machine that would support some hundreds of
simultaneous timesharing users. Their model was the electricity system - when you need electric power, you just stick a
plug in the wall, and within reason, as much power as you need will be there. The designers of this system, known as
MULTICS (MULTIplexed Information and Computing Service), envisioned one huge machine providing computing power for
everyone in teh Boston area. The idea that machines 10,000 times faster than their GE-645 mainframe would be sold (for
well under $1000) by the millions only 40 years later was pure science fiction. Sort of like the idea of supersonic
trans-Atlantic undersea trains now.

MULTICS was a mixed success. It was designed to support hundreds of users on a machine only slightly more powerful than
an Intel 386-based PC, although it had much more i/0 capacity. This is not quite as crazy as it sounds, since in those
days people knew how to write small, efficient programs, a skill that has subsequently been completely lost. There
were many reason that MULTICS did not take over the world, not the least of which is that it was written in the PL/I
programming language, and the PL/I compiler was years late and barely worked at all when it finally arrived. In
addition, MULTICS was enormously ambitious for its time, much like Charles Babbage's analytical engine in the nineteenth
century.

To make a long story short, MULTICS introduced many seminal ideas into the computer literature, but turning it into a
serious product and major commercial success was a lot harder than anyone had expected. Bell labs dropped out the
project, and General Electric quit the computer business altogether. However, MIT persisted and eventually got MULTICS
working. It was ultimately sold as a commercial product by teh company (Honeywell) that bought GE's computer business
and was installed by about 80 major companies and universities worldwide. While their numbers were small, MULTICS users
were fiercely loyal. General Motors, Ford, and US National Security Agency, for example, shut down their MULTICS system
only in late 1990s, 30 years after MULTICS was released, after years of trying to get Honeywell to update the hardware.

By teh end of the 20th century, the concept of computer utility had fizzled out, but it may well come back in the form
of cloud computing, in which relatively small computers (including smartphones, tablets, and the like) are connected to
services in vast and distant data centers where all the computing is done, with the local computer just handling the
user interface. The motivation here is that most people do not want to administrate an increasingly complex and finicky
computer system and would prefer to have that work done by a team of professionals, for example, people working for the
company running the data center. E-commerce is already evolving in this direction with various companies running emails
on multiprocessor servers to which simple client machines connect, very much in the spirit of the MULTICS design.

Despite its lack of commercial success, MULTICS had a huge influence on subsequent operating systems (especially Unix
and its derivatives, FreeBSD, Linux, iOS, and android). It is described in several papers and a book. It also has an
active website, located at www.multicians.org, with much information about the system. Its designers, and its users.

Another major development during the third generation was the phenomenal growth of minicomputers, starting with the DEC
PDP-1 in 1961. The PDP-1 had only 4K of 18-bit words, but at $120,000 per machine (less then 5% of the price of a 7094),
it sold like hotcakes. For certain kinds of nonnumerical work, it was almost as fast as the 7094 and gave birth to a
whole new industry. It was quickly followed by a series of other PDPs (unlike IBM's family, all incompatible)
culminating in the PDP-11.

One of the computer scientists at Bell labs who had worked on the MULTICS project, Ken Thompson, subsequently found a
small PDP-7 minicomputer that no one was using and set out to write a stripped-down, one-user version of MULTiCS. This
work later developed into the UNIX operating system, which became popular in teh academic world, with government
agencies, and with many companies.

The history of UNIX has been told elsewhere (e.g. Salus, 1994). Part of that story wil be given in Chapter 10. For now,
suffice it to say that because the source code was widely available, various organizations developed their own
(incompatible) versions, which led to chaos. Two major version developed, System V, from AT&T, and BSD (Berkeley
Software Distribution) from the university of california at berkeley. These had minor variants as well. To make it
possible to write programs that could run on any UNIX system. IEEE developed a standard for UNIX, called POSIX, that
most versions of UNIX now support. POSIX defines a minimal system-call interface that conformant UNIX system must
support. In fact, some other operating systems now also support the POSIX interface.

As an aside, it is worth mentioning that in 1987, the author released a small clone of UNIX, called MINIX, for
educational purposes. Functionally, MINIX is very similar to UNIX, including POSIX support. Since that time, the
original version has evolved into MINIX 3, which is highly modular and focused on very high reliability. It has the
ability to detect and and replace faulty or even crashed modules (such as i/o device drivers) on the fly without a
reboot and without disturbing running programs. it focus is on providing very high dependability and availability.
A book describing its internal operation and listing the source code in an appendix is also available (Tanenbaum and
Woodhull, 2006). The MINIX 3 system is available for free (including al lthe source code) over the internet at
www.minix3.org.

The desire for a free production (as opposed to educational) version of MINIX led a finnish student, Linus Torvalds, to
write Linux. This system was directly inspired by and developed on MINIX and originally supported various MINIX feature
(e.g., the MINIX file system). It has since been extended in many ways by many people but still retains some underlying
structure common to MINIX and to UNIX. Readers interested in a detailed history of Linux and the open source movements
might want to read Glyn Moody's (2001) book. Most of what will be said about UNIX in this book thus applies to System V,
MINIX, Linux and other versions and clone of UNIX as well.

1.2.4 The fourth generation (1980-present): Personal Computers

With the development of LSI (Large Scale Integration) circuits - chips containing thousands of transistors on a square
centimeter of silicon - the age of personal computer dawned. In terms of architecture, personal computers (initially
called microcomputers) were not all that different from minicomputers of the PDP-11 class, but in terms of price they
certainly were different. Where the minicomputer make it possible for a department in a company or university to
have its own computer, the microprocessor chip made it possible for a single individual to have his or her own personal
computer.

In 1974, when intel came out with the 8080, the first general-purpose 8-bit CPU, it wanted an operating system for the
8080, in part to be able to rest it. Intel asked one of its consultants, Gary Kildall, to write one. kildall and a
friend first built a controller for the newly released Shugart Associates 8-inch floppy disk and hooked the floppy disk
up to the 8080, thus producing the first microcomputer with a disk. Kildall then wrote a disk-based operating system
called CP/M (Control Program for Microcomputers) for it. Since intel did not think that disk-based microcomputers had
much of a future, when Kildall asked for teh rights to CP/M, Intel granted his request. Kildall then formed a company,
Digital Research, to further develop and sell CP/M.

In 1977, Digital Research rewrote CP/M to make it suitable for running on the many microcomputers using the 8080, Zilog
Z80, and other CPU chips. Many application programs were written to run on CP/M, allowing it to completely dominate the
world of micro-computing for about 5 years.

In the early 1980s, IBM designed the IBM PC and looked around for software to run on it. People from IBM contacted Bill
Gates to license his BASIC interpreter. They also asked him if he knew of an operating system to run on the PC. Gates
suggested that IBM contact Digital Research, then the world's dominant operating systems company. Making what was surely
the worst business decision in recorded history, Kildall refused to meet with IBM, sending a subordinate instead.
To make mattes even worse, his lawyer even refused to sign IBM's nondisclosure agreement covering the not-yet-announced
PC. Consequently, IBM went back to Gates asking if he could provided the with an operating system.

When IBM came back, Gates realized that a local computer manufacturer, Seattle Computer Products, had a suitable
operating system, DOS (Disk Operating system). He approached them and asked to buy it (allegedly for %75,000), which
they readily accepted. Gates then offered IBM a DOS/BASIC package, which IBM accepted. IBM wanted certain modifications,
so Gates hired teh person who wrote DOS, Tim paterson, as an employee of Gates fledgling company, Microsoft, to make
them. The revise system was renamed MS-DOS (Microsoft Disk Operating System) and quickly came to dominate the IBM PC
market. A key factor here was Gate's (in retrospect, extremely wise) decision to sell MS-DOS to computer companies for
bundling with their hardware, compared to Kildall's attempt to sell CP/M to end users one at a time (at least initially)
After all this transpired, Kildall died suddenly and unexpectedly from causes that have not been fully disclosed.

By the time teh successor to the IMB PC, the IBM PC/AT, came out in 1983 with the intel 80286 CPU, MS-DOS was firmly
entrenched and CP/M ws on its last legs. MS-DOS was later widely used on the 80386 and 80486. Although the initial
version of MS-DOS was fairly primitive, subsequent versions included more advanced features, including many taken from
UNIX. (Microsoft was well aware of UNIX, even selling a microcomputer version of it called XENIX during the company's
early years.)

CP/M, MS-DOS, and other operating systems for early microcomputers were all based on users typing in commands from the
keyboard. That eventually changed due to research done by Doug Engelbart at Stanford Research Institute in the 1960s.
Engelbart invented teh Graphical User Interface, complete with windows, icons, menus, and mouse. These ideas were
adopted by researchers at Xerox PARC and incorporated into machines they built.

One day, Steve Jobs, who con-invented the Apple computer in this garage, visited PARC, saw a GUI, and instantly
realized its potential value, something Xerox management famously did not. This strategic blunder of gargantuan
proportions led to a blook entitled Fumbling the Future (Smith and Alexander, 1988). jobs then embarked on building an
Apple with GUI. This project led to the Lisa, which was too expensive and failed commercially. Jobs' second attempt,
the Apple Macintosh, was a huge success, not only because it was much cheaper than Lisa, but also because it was user
friendly, meaning that it was intended for users who not only knew nothing about computers but furthermore had
absolutely no intention whatsoever of learning. In the creative world of graphic design, professional digital
photography, and professional digital video production, Macintoshes are very widely used and their users are very
enthusiastic about them. In 1999, Apple adopted a kernel derived from Carnegie Mellon University's Mach micro kernel
which was originally developed to replace the kernel of BSD UNIX. Thus, Mac OSX is a unix-based operating system, albeit
with a very distinctive interface.

When Microsoft decided to build a successor to MS-DOS, it was strongly influenced by teh success of teh Macintosh. It
produced a GUI-based system called Windows, which originally run on top of MS-DOS (e.g., it was more like a shell then a
true operating system). For about 10 years, from 1985 to 1995, windows was jut a graphical environment on top of MS-DOS
However, starting in 1995 a freestanding version, Windows 95, was released that incorporated many operating system
features into it, using the underlying MS-DOS system only for booting and running old MS-DOS programs. In 1998, a
slightly modified version of this system, called windows 98 was released. nevertheless, both windows 95 and windows 98
still contained a large amount of 16-bit intel assembly language.

Another microsoft operating system, windows nt (where the nt stands for new technology), which was compatible with
windows 95 at a certain level, but a complete rewrite from scratch internally. it was a full 32-bit system. The lead
designer for windows nt was David Cutler, who was also one of the designers fo the VAX VMS operating system, so some
ideas from VMS are present in NT. In fact, so many ideas form VMS were present in it that the owner of VMS, DEC, sued
Microsoft. The case was settled out of court for an amount of money requiring many digits to express. Microsoft expected
that teh first version of NT would kill off MS-DOS and all other version of windows since it was a vastly superior
system, but it fizzled. only with Windows NT 4.0 did it finally catch on the big way, especially on corporate networks.
Version 5 of windows nt was renamed windows 2000 in early 1999. It was intended to be the successor to both windows 98
and windows nt 4.0.

That did not quite work out either, so Microsoft came out with yet another version of windows 98 called windows me (
Millennium Edition). In 2001, a slightly upgraded version of windows 2000, called windows xp was released. That version
had a much longer run (6 years), basically replacing all previous version of windows.

Still the spawning of versions continued unabated. After widows 2000, Microsoft broke up the windows family into a
client and a server line. The client line was based on xp and tis successors, while the server line included windows
server 2003 and windows 2008. A third line, for the embedded world, appeared a little later. All of these versions
of Windows forked off their variations, in the form of service packs. It was enough to drive some administrators (and
writers of operating systems textbooks) balmy.

Then in January 2007, Microsoft finally released the successor to windows xp, called vista. It came with a new graphical
interface, improved security, and many new or upgraded user programs. Microsoft hoped it would replace windows xp
completely, but it never did. instead, it received much criticism and a bad press, mostly due to the high system
requirements, restrictive licensing terms, and support for digit rights management techniques that made it harder for
users to copy protected material.

With the arrival of windows 7, a new and much less resource hungry version of teh operating system, many people decide
to skip vista altogether, windows 7 did not introduce too many new features, but it was relatively small and quite
stable. in less than tree weeks, windows 7 had obtained more market share than vista in seven months. In 2012,
Microsoft launched its successor, Windows 8, an operating system with a completely new look and feel. geared for touch
screens, The company hopes that the new design will become the dominant operating system on a much wider variety of
devices: desktops, laptops, notebooks, tables, phones, and home theater PCs. So far, however, te market penetration is
slow compared to Windows 7.

The other major contender in personal computer world is UNIX (and its various derivatives). UNIX is strongest on network
and enterprise servers but is also often present on desktop computers, notebooks, tablets, and smartphones. On x86-based
computers, Linux is becoming a popular alternative to windows for student and increasingly many corporate users.

As an aside, throughout this book we will use the term x98 to refer to all modern processors based on teh family of
instruction-set architectures that started with the 8086 in the 1970s. There are many such processors, manufactured by
companies like AMD and Intel, and under the hood they often differ considerably: Processors may be 32 bits or 64 bits
with few or many cores and pipelines that may be deep or shallow, and so on. Nevertheless, to teh programmer, they all
look quite similar and tehy can all still run 8086 code that was written 35 years ago. Where the difference is
important. we will refer to explicit models instead - and use x86-32 and x86-64 to indicate 32-bit and 64-bit variants.

FreeBSD is also a popular UNIX derivative, originating from the BSD project at Berkeley. All modern macintosh computers
run a modified version of freeBSD. unix is also standard on workstations powered by high-performance RISC chips. Its
derivatives are widely used on mobile devices, such a those running iOS 7 and android.

Many UNIX users, especially experienced programmers, prefer a command based interface to a GUI. so nearly all UNIX
systems support a windowing system called X windows system (also know as X11) produced at MIT this system handles the
basic windows management, allowing users to create, delete, move and resize windows using a mouse. Often a complete GUI,
such as Gnome or KDE, is available to run on top of X11, giving UNIX a look and feel something like the macintosh or
microsoft windows, for those UNIX users who want to such a thing.

An interesting development that began taking place during the mid-1980s is teh growth of networks of personal computers
running network operating systems and distributed operating systems (Tanenbaum and Van Steen, 2007). In a network
operating system, teh users are aware of th existence of multiple computers and log in to remote machines and copy files
from one machine to another. Each machine runs its own local operating system and ahs its own local (or users).

Network operating systems are not fundamentally different from single-processor operating system. They obviously need a
network interface controller and some low-level software to driver it, as well as programs to achieve remote login and
remote file access, but these additions do not change the essential structure of the operating system.

A distributed operating system, in contrast, is one that appears to its users as traditional uniprocessor system, even
though it is actually composed of multiple processors. The users should not be aware of where their programs are being
run or where their files are located; that should all be handled automatically and efficiently by the operating system.

True distributed operating systems require more than just adding a little code to a uniqprocessor operating system,
because distributed and centralized system differ in certain critical ways. Distributed systems, for example, often
allow applications to run on several processors at teh same time, thus requiring more complex processor scheduling
algorithms in order to optimize the amount of parallelism.

Communication delays within the network often mean that these (and other) algorithms must run with incomplete, outdated,
or even incorrect information. This situation differs radically from that in a single processor system in which the
operating system has complete information about the system sate.

1.2.5. The fifth generation (1990-present): mobile computers

Ever since detective Dick tracy started talking to his "two-way radio wrist watch" in teh 1940s comic strip, people
have craved a communication device they could carry around wherever they went. The first real mobile phone appeared in
1946 and weighed some 40 kilos. you could take it wherever you went as long as you had a car in which to carry it.

The first true handheld phone appeared in teh 1970s and, at roughly one kilogram, was positively featherweight, It was
affectionately know as "the  brick." Pretty soon everybody wanted one. Today, mobile phone penetration is close to 90%
of teh global population. We can make calls not jsut with our portable phones and wrist watches, but soon with
eyeglasses and other wearable items. Moreover, the phone part is no longer that interesting. We receive email, surf the
Web, text our friends, play games, navigate around heavy traffic - and do not even think twice about it.

While the idea of combining telephony and computing in a phone-like device has been around since the 1970s also, the
first real smartphone did not appear until the mid-1990s when Nokia released the N9000, which literally combined two,
mostly separate device: a phone and a PDA (Personal Digital Assistant). In 1997, Ericsson coined teh term smartphone for
its GS88 "Penelope."

Now that smartphones have become ubiquitous, the competition between the various operating system is fierce and the
outcome is even less clear than the PC world. At the time of writing, Google's Android is the dominant operating system
with Apple's iOS a clear second, but this was not always teh case and all many be different again in just a few years.
If anything is clear in the world of smartphones, it is that it is not easy to stay king of the mountain for long.

After all, most smartphones in the first decade after their inception were running Symbian OS. It was the operating
system of choice for popular brands like Samsung, Sony Ericsson, Motorola, and especially Nokia. However, other
operating systems like RIM's balckberry OS (introduced for smartphones in 2002) and Apple's iOS (released for teh first
iPhone in 2007) started eating into symbian's market share. many expected that rim would dominate the business market,
while ios would be the king of the consumer devices. Symbian's market share plummeted. In 2011, nokia ditched Symbian
and announced it would focus on windows Phone as its primary platform. For some time, Apple and RIM were the toast of
the town (although not nearly as dominant as symbian had been), but it did not take very long for Android. A linux-based
operating system released by Google in 2008, to overtake all its rivals.

For phone manufacturers, Android had the advantage that it was open source and available under a permissive license. As
a result, they could tinker with it and adapt it to their own hardware with ease. Also, it has a huge community of
developers writing apps, mostly in the familiar Java programming language. Even so, the past years have shown that the
dominance may not last, and Android's competitors are eager to claw back some of ti market share. We will look at
android in detail in sec 10.8.
"""