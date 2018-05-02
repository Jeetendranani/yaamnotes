"""
1.3 computer hardware review

An operating system is intimately tied to the hardware of the computer it runs on. It extends the computer's instruction
set and manages tis resources. To work ,it must know a great deal about the hardware, at least about how the hardware
appears to the programmer. For this reason, let us briefly review computer hardware as found in modern personal
computers. After that, we can start getting into the details of what operating system do and how they work.

Conceptually, a simple personal computer can be abstracted to a model resembling that of Fig 1-6. The CPU, memory and
i/o devices are all connected by a system bus and communicate with one another over it. Modern personal computers
have a more complicated structure, involving multiple buses, which we will look at later. For the time being, this
model will be sufficient. In the following sections, we will briefly review these components and examine some of the
hardware issues that are of concern to operating system designers. Needless to say, this will be a very compact
summary. Many books have been written on teh subject of computer hardware and computer organization. Two well-known ones
are by Tanenbaum and Austin (2012) and Patterson and Hennessy (2013).

1.3.1 Processor

The "brain" of the computer is the CPU. It fetches instructions from memory and executes them. The basic cycle of every
CPU is to fetch teh first instruction from memory, decode it to determine its type and operands, execute it, and then
fetch, decode, and execute subsequent instructions. The cycle is repeated until the program finishes. In this way,
programs are carried out.

Each CPU has a specific set of instructions that it can execute, Thus an x86 processor cannot execute ARM programs and
an ARM processor cannot execute x86 programs. Because accessing memory to get an instruction or data word takes much
longer than executing an instruction, all CPUs contain some registers inside to hold key variables and temporary
results. Thus the instruction set generally contains instructions to load a word from memory into a register, and store
a word fro ma register into memory. Other instructions combine two operands from registers, memory. or both into a
result, such as adding two words and storing the result in a register or in memory.

In addition to the general registers used to hold variables and temporary results, most computers have several special
registers that are visible to teh programmer, One of these is the program counter, which contains the memory address of
the next instruction to be fetched. After that instruction has been fetched, the program counter is updated to point to
its successor.

Another register is the stack pointer, which points to the top of the current stack in memory. The stack contains one
frame for each holds those input parameters, local variables, and temporary variables that are not kept in registers.

Yet another register is the PSW (Program Status Word). This register contains the conditions code bits, which are set by
comparison instructions, the CPU priority, the mode (user or kernel), and various other control bits. user programs
may normally read the entire PSW but typically may write only some of tis fields. The PSW plays an important role in
system calls and I/O.

The operating system must be fully aware of all the registers. When time multiplexing the CPU, the operating system will
often stop the running program to (re)start another one. Every time it stops a running program, the operating system
must save all teh registers so they can be restored when the program runs later.

To improve the performance, CPU designers have long abandoned teh simple model of fetching, decoding, and executing
one instruction at a time. Many modern CPUs have facilities for executing more than one instruction at the same time.
For example, a CPU migth have separated fetch, decode, and execute units, so that while it is executing instruction n,
it could also be decoding instruction n+1 and fetching instruction n+2. Such an organization is called pipeline and is
illustrated in Fig 1-7(a) for a pipeline with three stages, longer pipelines are common. In most pipeline designs, once
an instruction has been fetched into the pipeline, it must be executed, even if teh preceding instruction was a
conditional branch that was taken. Pipelines case compiler writers and operating system writers great headaches because
they expose the complexities of the underlying machine to them and they have to deal with them.

Even more advanced than a pipeline design is a superscalar CPU, shown in Fig 1-7(b). In this design, multiple execution
unites are present, for example, one for integer arithmetic, one for floating-point arithmetic, and one for Boolean
operations. Two or more instructions are fetched at once, decoded, and dumped into a holding buffer until they can be
executed. As soon as an execution unit becomes available, it looks in the holding buffer to see if there an instruction
it can handler, and if so. it removes the instruction from the buffer and executes it. An implication of this design is
that program instructions are often executed out of order. For the most part, it is up to the hardware to make sure the
result produced is teh same one a sequential implementation would have produced, but an annoying amount of the
complexity is foisted onto the operating system, as we shall see.

Most CPUs, except very simple ones used in embedded system, have two modes, kernel mode and user mode, as mentioned
earlier. usually, a bit in the PSW controls the mode. When running in kernel mode, the CPU can execute every instruction
in its instruction set and use every feature of the hardware. On desktop and server machines, the operating system
normally runs in kernel mode, giving it access to the complete hardware. On most embedded systems, a small piece runs
in kernel mode, with the rest of the operating system running in user mode.

user programs always run in user mode, which permits only subset of the instructions to be executed and subset of the
feature to be accessed. Generally, all instructions involving i/o and memory protection are disallowed in user mode.
Setting the PSW mode bit to enter kernel mode is also forbidden, of course.

To obtain service from the operating system, a user program must make a system call, which traps into the kernel and
invokes the operating system. The TRAP instruction switches from user mode to kernel mode and starts the operating
system. When the work ahs been completed, control is returned to the user program at teh instruction following the
system call. We will explain the detail of teh system call mechanism later in this chapter. For the time being, think of
it as a special kind of procedure call that has the additional property of switching from user mode to kernel mode. As
a note on typography, we will use the lower-case Helvetica font to indicate system calls in running text, like this:
read.

it is worth nothing that computers have traps other than the instruction for executing a system call, most of the other
traps are caused by the hardware to warn of an exceptional situation such as an attempt to divide by 0 or floating-point
underflow. In all cases the operating system gets control and must decide what to do. Sometimes the program must be
terminated with an error. Other times the error can be ignored (an underflowed number can be set to 0). Finally, when
the program has announced in advance that ti wants to handle certain kinds of conditions, control can be passed back to
program to let it deal with the problem.

Multithreaded and multicore chips

Moore's law states that teh number of transistors on a chip doubles very 18 months. This "law" is not some kind of law
of physics, like conservation of momentum, but is an observation by intel cofounder Gordon Moore of how fast process
engineers at the semiconductor companies are able to shrink their transistors. Moore's law has held for over three
decades now and is expected to hold for at least one more. After that, teh number of atoms per transistor will become
too small and quantum mechanics will start to play a big role, preventing further shrinkage of transistor sizes.

The abundance of transistors is leading to a problem: what to do with all of them? We saw one approach above:
superscalar architectures, with multiple functional units. But as the number of transistors increases, even more is
possible. One obvious thing to do is put bigger caches on the CPU chip. That is definitely happening, but eventually
the point of diminishing returns will be reached.

The obvious next step is to replicate not only hte functional units, but also some of the control logic. The intel
Pentium 4 introduced this property. called multithreading or hyperthreading (Intel's name for it), to the x86 processor
and several other CPU chips also have it - including the SPARC, the Power5, the Intel Xeon and the Intel Core family.
To a first  approximation, what is does it allow the CPU to hold the state of two different threads and then switch back
and forth on nanoseconds time scale. (A thread is a kind of lightweight process, which, in turn, is a running program;
We will get into the detail in chapter 2.) For example, if one of the processes need to read a word from memory (which
takes namy clock cycles), a multithreaded  CPU can just switch to another thread, Multithreading does not offer true
parallelism. Only one process at a time is running, but thread-switching time is reduced to the order of a nanosecond.

Multithreading has implications for the operating system because each thread appears to the operating system as a
separate CPU. Consider a system with two actual CPUs, each with two threads. The operating system will see this as four
CPUs. if there is only enough work to keep two CPUs busy at certain point in time, it may inadvertently schedule two
threads on the same CPU. With the other CPU completely idle. This choice is far less efficient than using one thread
on each CPU.

Beyond multithreading, many CPU chips now have four, eight, or more complete processors or cores on them. The multicore
chips of Fig 1-8 effectively carry four mini-chips on them. each with its own independent CPU. (the caches will be
explained below.) Some processors, like Intel Xeon Phi and the Tilera TilePro, already sport more than 60 cores on a
single chip. Making use of such a multicore chip will definitely require a multiprocessor operating system.

Incidentally, in terms of sheer numbers, nothing beats a modern GPU (Graphics Processing Unit). A GPU is processor with,
literally, thousands of tiny cores. They are very good for many small computations down in parallel, like rending
polygons in graphics applications. They are not so good at serial tasks. They are also hard to program. While GPUs can
be useful for operating systems (e.g, encryption or processing of network traffic), it is not likely that much of the
operating system itself will run on the GPUs.

1.3.2 Memory

The second major component in any computer is the memory. Ideally, a memory should be extremely fast (faster than
executing an instruction so that the CPU is not held up by teh memory), abundantly large, and dirt cheap. No current
technology satisfies all of these goals, so a different approach is taken. The memory system is constructed as a
hierarchy of layers. as shown in Fig 1-9. The top layers have higher speed, smaller capacity, and greater cost per
bit than the lower ones, often by factors of a billion or more.

The top layer consists of the registers internal to the CPU. They are made of the same material as the CPU and are thus
just as fast as the CPU. Consequently, there is no delay in accessing them. The storage capacity available in them is
typically 32x32 bits on teh 32bit CPU and 64x64 bits on a 64-bits CPU. Less then 1kb in both cases. Programs must
manage the registers (i.e., decide what to keep in them) themselves, in software.

Next comes teh cache memory, which is mostly controlled by teh hardware. Main memory is divided up into cache lines,
typically 64 bytes, with addresses 0 to 63 in cache line 0, 64 to 127 in cache line 1, and so on. The most heavily used
cache lines are kep in teh high-speed cache located inside or very close to the CPU. When teh program needs to read a
memory word, teh cache hardware checks to see if the line needed is in the cache. If it is, called a cache hit, the
request is satisfied from the cache and no memory request is send over the bus to the main memory. Cache hits normally
take about two clock cycles. Cache misses have to go to memory, with a substantial time penalty. Cache memory is
limited in size due to its high cost. Some machines have two or even three levels of cache, each one slower and bigger
than the one before it.

Caching plays a major role in many areas of computer science, not just caching lines of RAM. Whenever a resource can
be divided into pieces, some of which are used much more heavily than others, caching is often used to improve
performance. Operating systems use it all the time. For example, most operating systems keep (pieces of) heavily used
files in main memory to avoid having to fetch them from the disk repeatedly. Similarly, the results of converting
long path names like
/home/ast/projects/src/kernel/clock.c
into the desk address where the file is located can be cached to avoid repeated lookups. finally, when the address of
web pge (url) is convertd to a network address (IP address), the result can be cached for future use. Many other use
exist.
In any caching system, several questions come up fairly soon, including:
1. When to put a new item into the cache
2. Which cache line to put the new item in
3. Which item to remove from the cache when a slot is needed
4. Where to put a newly evicted item in the larger memory

Not every question is relevant to every caching situation. For caching lines of main memory in the CPU cache, a new item
will generally be entered on every cache miss. The cache line to use is generally computed by using some of the high
order bits of the memory address referenced. For example, with 4096 cache lines of 64 bytes and 32 bit addresses bits 6
through 17 might be used to specify the cache line, with bits 0 to 5 the bytes within the cache line. In this case,
the item to remove is the same one as the new data goes into, but in other systems it might not be. Finally, when a
cache line is rewritten to main memory (if it has been modified since it was cached), the place in memory to rewritten
to main memory (if it has been modified since it was cached), the place in memory to rewrite to is uniquely determined
by the address in question.

Caches are such a good idea that modern CPUs have two of them. The first level or L1 cache is always inside the CPU and
usually feeds decoded instructions into the CPU's execution engine. Most chips have a second L1 cache for very heavily
used data words. The L1 caches are typically 16kb each. In addition there is often a second cache, called L2 cache,
that holds several megabytes of recently used memory words. The difference between the L1 and L2 caches lies in the
timing. Access to the L1 cache is done without any delay, whereas access the L2 cache involves a delay of one or two
clock cycles.

On multicore chips, teh designers have to decide where to place the caches. In Fig 1-8(a), a single L2 cache is shared
by all the cores. The approach is used in Intel shared L2 cache requires a more complicated cache controller but the
AMD way makes keeping the L2 caches consistent more difficult.

Main memory comes next in the hierarchy of Fig1-9. This is the workhorse of the memory system. main memory is usually
called RAM (Random Access Memory). Old-times sometimes call it core memory, because computers in the 1950s and 1960s
used tiny magnetizable ferrite cores for main memory. They have been gone for decades but the name persists. Currently,
memories are hundreds of megabytes to several gigabytes and growing  rapidly. All CPU requests that cannot be satisfied
out of the cache go to main memory.

In addition to the main memory, many computer have a small amount of non-volatile random access memory. unlike RAM,
non volatile memory does not lose its contents when the power is switched off. ROM (Read Only Memory) is programmed at
the factory and connot be changed afterword. it is fast and inexpensive, On some computers, the bootstrap loader used
to start teh computer is contained in ROM. Also some i/o cards come with ROM for handling low-level device control.

EEPROM (Electrically Erasable PROM) and flash memory are also non volatile, but in contrast to ROM can be erased and
rewritten. however, writing the takes orders of magnitude more time than writing RAM. so they are used in the same way
ROM is, only with the additional feature that it is now possible to correct bugs in programs  they hold by rewriting
them in the field.

Flash memory is also commonly used as teh storage medium in portable electronic devices. It serves as film in digital
cameras and as teh disk in portable music players. To name just two uses. Flash memory is intermediate in speed
between RAM and disk. Also, unlike disk memory, if it is erased too many times, it wears out.

Yet another kind of memory is CMOS, which is volatile, many computers use CMOS memory to hold the current time and date.
The CMOS memeory and clock circuit that increments the time in it are powered by a small battery, so the time is
correctly updated even when the computer is unplugged. The CMOS memory can also hold configuration parameters, such as
which disk to boot from. CMOS is used because it draws so little power that the original factory-installed battery
often lasts for years. However, when it begins to fail, the computer appear to have Alzheimer's disease, forgetting
things that it has known for years, like which hard disk to boot from.

1.3.3 Disks

Nest in teh hierachy is magnetic disk (hard disk). Disk storage is two orders of magnitude cheaper than RAM per bit and
often two orders of magnitude larger as well. The only problem is that the time to randomly access data on it is close
to three orders of magnitude slower. The reason is that a disk is a mechanical device, as shown in Fig 1-10.

a disk consists of one of more metal platters that rotate at 5400, 7200, 10800 RPM or more. A mechanical arm pivots over
platters from the corner, similar to the pickup arm on an old 33-RPM phonograph for playing vinyl records. Information
is written onto the disk in a series of concentric circles. At any given arm position, each of teh heads can read an
annular region called track. Together, all the tracks for a given arm position form a cylinder.

Each track is divided into some number of sectors, typically 512 bytes per sector. On modern disks, the outer cylinders
contains more sectors than the inner ones. Moving the arm form one cylinder to the next takes about 1 msec. Moving it to
random cylinder typically takes 5 to msec, depending on the drive. Once the arm is on the correct track, the drive must
wait for the needed sector to rotate under the header, an additional delay of 5 to 10 msec, depending on the drivers'
RPM. Once the sector is under head, reading or writing occurs at rate fo 50MB/sec on lowend disks to 160mb/s on faster
ones.

Sometimees you will hear peole talk about disks that are really not disks at all, like SSDs (solid state disks). SSDs
do not have moving parts, do not contain platters in the shape of disks, and store data in (Flash) memory. The only ways
in which they resemble disks is that they also sore a lot of data which is not lost when the power is off.

many computer support a scheme known as virtual memory, which we will discuss at some length in chapter 3. This scheme
makes it possible to run programs larger than physical memory by placing the on the disk and suing main memory as kind
of cache for the most heavily executed parts. This scheme requires remapping memory address in RAM where the word is
located. This mapping is done by a part of the CPU called MMU (memory Management unit), as show in Fig 1-6.

The presence of caching and MMU can have a major impact on performance. In a multiprogramming system, when switching
from one program to another, sometimes called a context switch, it may be necessary to flush all modified blocks from
the cache and change the mapping registers in the MMU. both of these are expensive operations, and programmers try
hard to avoid them. We will see some of the implications of their tactics later.

1.3.4 I/O devices

The CPU and memory are not the only resources that the operating system must manage. I/O devices also interact heavily
with the operating sytem. As we saw in Fig 1-6 i/o devices generally consist of two parts: a controller and the device
itself. The controller is a chip or a set of chips that physically controls the device. It accepts commands from
the operating system, for example, to read data from the device, and carries them out.

In many cases, the actual control of the devices is complicated and detailed, so it is the job of controller to present
a simpler 9but still very complex) interface to the operating system. For example, a disk controller might accept a
command to read sector 11,206 from disk 2. The controller then has to convert this linear sector number to a cylinder,
sector, and head. This conversion may be complicated by teh fact that outer cylinders have more sectors than inter ones
and that some bad sectors have been remapped onto others ones. Then the controller has to determine which cylinder the
disk arm is on and give it a command to move in or out the requisite number of cylinders. It has to wait until the
proper sector has rotated under the head and then start reading and storing the its as they come off the drive,
removing the preamble and computing the checksum. Finally, it has to assemble the incoming bits into words and store
them in memory. To do all this work, controllers often contain small embedded computers that are programmed to do their
work.

The other piece is teh actual device itself. Devices have fairly simple interfaces, both because they cannot do much and
to make them standard. The latter is needed so that any SATA disk controller can handle any SATA disk, for example. SATA
stands for Serial ATA and ATA in turns stands at AT Attachment. In case you are curious what at stands for, this was
IBM's second generation "Personal Computer Advanced Technology" built around the then-extremely-potent 6mhz 80286
processor that teh company introduced in 1984. What we learn from this is that the computer industry has habit of
continuously enhancing existing acronyms with new prefixes and suffixes. We also leaned that an adjective like
"advanced" should be used with great care. or you will look silly thirty years down the line.

SATA is currently the standard type of disk on many computers. Since the actually device interface is hidden behind the
controller, all that the operating system sees is the interface to teh controller, which may be quite different from
the interface to the device.

Because each type of controller is different, different software is needed to control each one. The software that talks
to a controller, giving it commands and accepting responses, is called device driver. Each controller manufacturer has
to supply a driver for each operating system it supports. Thus a scanner may come with drivers for OSX, windows 7,
widows 8 and linux. For example.

To be sued, teh driver has to be put into the operating system so it can run in kernel mode. Drivers can actually run
outside the kernel, and operating systems like linux and windows nowadays do offer some support for doing so. The vast
majority of the drivers still run below the kernel boundary. Only very few current systems, such as MINIX 3, run all
drivers in user space. Drivers in user space must be allowed to access the deice in a controlled way, which is not
straightforward.

There are three ways the driver can be put into the kernel. The first way is to relink the kernel with the new driver
and then reboot the system. Many older UNIX systems work like this. The second way is to make an entry in an operating
system file telling it that it needs the driver and then reboot the system. At boot time, the operating system goes and
find the drivers it needs and loads them. Windows works this way. The third way is for the operating system to be able
to accept new drivers while running and install them on the fly without the need to reboot. This way used to be rare
but is becoming much more common now. Hot-pluggable devices, such as USB and IEEE 1394 devices (discussed below), always
need dynamically loaded drivers.

Every controller has a small number of registers that are used to communicate with it. For example, a minimal disk
controller might have registers for specifying the disk address, memory address, sector count, and direction (read or
write). To activate the controller, the driver gets a command from the operating system, then translates it into the
appropriate values to write into the device registers. Th collection of all the device registers form the i/o port
space, a subject we will come back to in chapter 5.

On some computers, the device registers are mapped into the operating system's address space (the addresses it can use),
so they can be read and written like ordinary memory words. On such computers, no special i/o instructions are required
and user programs can be kept away from the hardware by not putting these memory addresses within their reach (e.g., by
using base and limit registers). On other computers, the device registers are put in a special i/o port space, with
each register having a port address. On these machines, special IN and OUT instructions are available in kernel mode to
allow drivers to read and write the registers. The former scheme eliminates the need for special i/o instructions but
uses up some of the address space. The latter uses no address space but requires special instructions. Both systems are
widely used.

Input and output can be done in three different ways. In the simplest method, a user program issues a system call, which
the kernel then translates into a procedure call to the appropriate driver. The driver then starts the i/o and sits in
a tight loop continuously polling the device to see if it is done (usually there is some bit that indicates that the
devices is still busy). When the i/o has completed, the driver puts the data (if any) where they are needed and returns.
The operating system then returns control to the caller. This method is called busy waiting and has the disadvantage
of typing up the CPU polling the device unit it is finished.

The second method is for the driver to start the device and ask it to give an interrupt when it is finished. At that
point the driver returns. The operating system then blocks the caller if need be and looks for other work to do. When
the controller detects the end of the transfer, it generates an interrupt to signal completion.

Interrupts are very important in operating systems, so let us examine the idea more closely. In Fig 1-11 we see a three
step process for i/o. In step 1, the driver tells the controller what to do by writing into its device registers. The
controller then starts teh device. When the controller has finished reading or writing the number of bytes it has been
told to transfer, its signals the interrupt controller chip using certain bus lines in step 2. if the interrupt
controller is ready to accept the interrupt (which it may not be if it is busy handling a higher-priority one), it
asserts a pin on the CPU chip telling it. In step 3, In step 4, the interrupt controller puts the number of the device
on the bus so the CPU can read it and know which device has just finished (many devices may be running at the same
time).

Once the CPU has decide to take teh interrupt, the program counter and PSW are typically then pushed onto the current
stack and the CPU switched into kernel mode. The device number may be used as an index into part of memory to find the
address of the interrupt handler for this device. This part of memory is called the interrupt vector. Once the interrupt
handler (part of the driver for the interrupting device) has started, It remove the stacked program counter and PSW and
saves them, then queries the device to learn its status. When the handler is all finished, it return to the previously
sunning user program to the first instruction that was not yet executed. These steps are shown in Fig 1-11(b).

The third method for doing i/o makes use of special hardware: a DMA (Direct Memory Access) chip that can control the
flow of bits between memory and some controller without constant CPU intervention. The CPU sets up the DMA chip, telling
it how many bytes to transfer, the device and memory addresses involved, and the direction, and lets it go. When the
DMA chip is done, it causes an interrupt, which is handled as described above. DMA and i/o hardware in general will be
discussed in more detail in chapter 5.

Interrupts can (and often do) happen at highly inconvenient moments, for example, while another interrupt handler is
running. For this reason, the CPU has a way to disable interrupts and then reenable them later. While interrupts are
disabled, any devices that finish continue to assert their interrupt signals, but the CPU is not interrupted until
interrupts are enabled again. If multiple devices finished while interrupts are disabled, the interrupt controller
decides which one to let through first, usually based on static priorities assigned to each device. The highest priority
device wins and gets to be serviced first. The others must wait.

1.3.5 buses

The organization of Fig 1-6 was used on minicomputers for years and also on the original IBM PC. However, as processors
and memories got faster, the ability of the single bus (and certainly the IMB PC bus) to handle all traffic was strained
to the breaking point. Something had to give. As a result, additional buses were added, both of faster i/o devices and
for CPU to memory traffic. As a consequence of this evolution, a large x86 system currently looks something like Fig 1-2

This system has many buses (e.g., cache, memory, PCIe, PCI, USB, SATA, and DMI), each with a different transfer rate
and function. The operating system must be aware of all of them for configuration and management. The main bus is the
PCIe (Peripheral Component Interconnect Express) bus.

The PCIe bus was invented by Intel as a successor to the older PCI bus, which in turn was a replacement for the original
ISA (Industry Standard Architecture) bus. Capable of transferring tens of gigabits per second, PCIe is much faster than
its predecessors. It is also very different in nature. Up to its creation in 2004, mot buses were parallel and shared. A
shared bus architecture means that multiple devices use the same wires to transfer data. Thus, when multiple devices
have data to send. you need an arbiter to determine who can use the bus. In contract, PCIe makes use of dedicated, point
to point connections. A parallel bus architecture as used in traditional PCI means that you send each word of data over
multiple wires. For instance, in regular PCI buses, a single 32-bit number is sent over 32 parallel wires, In contrast to
this, PCIe uses a serial bus architecture and sends all bits in a message through a single connection, known as a lane,
much like a network packet. This is much simpler, because you do not have to ensure that all 32 bits arrive at the
destination at exactly the same time. Parallelism is still used. Because you can have multiple lanes in parallel. For
instance, we amy use 32 lanes to carry 32 messages in parallel. As the speed of peripheral devices like network cards
and graphics adapters increases rapidly, the PCIe standard is upgraded every 3-5 years. For instance, 16 lanes of PCIe
2.0 offer 64 gigabits per second. upgrading to PCIe 3.0 will give you twice that speed and PCIe 4.0 will double that
again.

Meanwhile, we still have many legacy devices for the older PCI standard. as we see in fig 1-12, these devices are hooked
up to a separate hub processor, in the future, when we consider PCI no longer merely old, but ancient, it is possible
that all PIC devices will attached to yet another hub that in turn connects them to teh main hub, creating a tree of
buses.

In this configuration, the CPU talks to memory over a fast DDR3 bus, to an external graphics device over PCIe and to all
other devices via a hub over a DMI (Direct Media Interface) bus. The hub in turn connects all the other devices, using
the Universal Serial Bus to talk to USB devices, the SATA bus to interact with ard disks and DVD drivers, and PCIe to
transfer Ethernet frames. We have already mentioned the older PCI devices that use a traditional PCI bus.

Moreover, each of the cores has a dedicated cache and a much larger cache that is shared between them. Each of these
caches introduces another bus.

The USB (Universal Serial Bus) was invented to attach all the slow i/o devices, such as the keyboard and mouse, to
the computer. However, calling a modern USB 3.0 device humming along at 5 Gbps "slow" may not come naturally for the
generation tht grew up with 8-mbps ISA as the main bus in the first IBM PCs USB uses a small connector with four to
eleven wires (depending on the version) some of which supply electrical power to the USB devices or connect to ground.
USB is a centralized bus in which a root device polls all the i/o devices every 1 msec to see if they have any traffic.
USB 1.0 could handle an aggregate load of 12mbps, USB 2.0 increased the speed to 480mbps, and USB 3.0 tops at no less
then 5 Gbps. Any USB device can be connected to a computer and it will function immediately, without requiring a reboot,
something per-USB devices required, much to teh consternation of a generation of frustrated users.

The SCSI (Small computer system interface) bus is a high-performance bus intended for fast disks, scanners, and other
devices needing considerable bandwidth. Nowadays, we find them mostly in servers and workstations. They can run at up
to 640 mbps.

To work in an environment such as that of Fig 1-12, the operating system has to know what peripheral devices are
connected to the computer and configure them. This requirement led intel and microsoft to design a PC system called plug
and play, based on a similar concept first implemented in teh Apple Macintosh. Before plug and play, each i/o card had a
fixed interrupt request level and fixed addresses for its i/o registers. For example, the keyboard was interrupt 1 and
used i/o addresses 0x60 to 0x64. the floppy disk controller was interrupt 6 and use i/o addresses 0x35 to 0x37, and the
printer was interrupt 7 and used i/o addresses 0x378 to 0x 37A, and so on.

So far, so good. The trouble come in when the user brought a sound card and modern card and both happened to use, say,
interrupt 4. They would conflict and would not work together. The solution was included DIP switches or jumpers on
every i/o card and instruct the user to please set them to select an interrupt level and i/o device addresses tht did
not conflict with any others in the user's system. Teenagers who devoted their lives to the intricacies of the PC
hardware could sometimes do this without making errors. Unfortunately, nobody else could, leading to chaos.

What plug and play does is have th system automatically collect information about the i/o addresses, and them tell each
card what its numbers are. This work is closely related to booting the computer, so let us look at that. it is not
completely trivial.

1.3.6 booting the computer

Very briefly, the boot process is as follows. Every PC contains a parentboard (formerly called teh motherboard before
political correctness hit the computer industry). on the parentboard is a program called the system BIOS (Basic Input
Output System). The BIOS contains low-level i/o software, including procedures to read the keyboard, write to the
screen, and do disk i/o, among other things. Nowadays, it is held in a flash RAM, which is nonvolatile but which can
be updated by the operating system when bugs are found in BIOS.

When the computer is booted, the BIOS is started. It first checks to see how much RAM is installed and whether the
keyboard and other basic device are installed and responding correctly. It starts out by scanning the PCIe and PCI
buses to detect all the devices attached to them. if the devices present are different form when the system was last
booted, the new devices are configured.

The BIOS then determines the boot device by trying a list devices stored in the CMOS memory. The user can change this
list by entering a BIOS configuration program just after booting. Typically, an attempt is made to boot from CD-ROM
(or sometime USB) driver, if one is present. If that fails, teh system boots from the hard disk. The first sector from
the boot devices is read into memory and executed. The sector contains a program that normally examines the partition
table at the end of the boot sector to determine which partition is active. then a secondary boot loader is read in
from that partition. This loader reads in the operating syte from teh active partition and starts it.

The operating system then queries the BIOS to get the configuration information. For eah device, it checks to see if
has the device driver. if not, it asks the user to insert a CD-ROM containing the driver (supplied by the device's
manufacturer) or to download it from the Internet. Once it has all the device drivers, the operating system loads them
into the kernel. Then it initializes its tables, creates whatever background processes are needed, and start up a
login program or GUI.

"""