"""
What is an operating system?

It is hard to pin down what an operating system is other than saying it is the software that runs in kernel mode - and
even that is not always true, part of the problem is that operating system perform two essentially unrelated functions:
providing application programmers (and application programs, naturally) a clean abstract set of resources. Depending on
who is doing the talking, you might hear mostly about one function or other. Lets now look at both.

The operating system as an extended machine

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

This poitn is so important that it is worth repeating in different words. with all due respect to the industrial
engineers who so carefully designed the macintosh, hardware is ugly, real processors, memories, disks, and other devices
are very complicated and present difficult, awkward, idiosyncratic, and inconsistent interfaces to the people who
have to write software to sue them. sometimes this is due to the need for backward compatibility with older hardware.
Other times it is attempt to save money. Often, however, teh hardware designers do not realize (or care) how much
trouble they are causing for the software. One of the major tasks of the operating system is to hide the hardware and
present programs (and their programmers) with nice, clean, elegant, consistent, abstractions to work with instead.
Operating systems turn teh ugly into the beautiful.

the operating system as a resource manager

the concept of an operating system as primarily providing abstractions to application programs is a top down view. An
alternative bottom up, view holds that teh operating system is there to manage all teh pieces of a complex system.
Modern computers consist of processors, memories timers, mice, network interfaces, printers, and wide variety of other
devices. In the bottom up view, the job of the operating system is to provide for an orderly and controlled allocation
of the processors, memories, and i/o devices among the various programs wanting them.

1.2 history of operating systems

The IBM 360 was the first major computer line to sue (small-scale) ics (integrated circuits), thus providing a major
price/performance advantage over the second generation machines, which were built up from individual transistors.
"""