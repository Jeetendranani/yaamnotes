"""
1.6 System calls

We have sen that operating systems have two main functions: providing abstractions to user programs and managing the
computer's resources, For the ost part, the interaction between user programs and the operating system deals with the
former; for example, creating, writing , reading, and deleting files. The resources management part is largely
transparent to the users and done automatically. Thus, the interface between user programs and the operating system is
primarily about dealing with the abstractions. To really understanding what operating systems do, we must examine this
interface closely. The system calls available in the interface vary from one operating system to another (although the
underlying concepts tend to be similar)

We are thus forced to make a choice between (1) vague generalities ("operating systems have system calls for reading
files") and (2) some specific system ("unix has a read system call with three parameters: one to specify the file, one
to tell where teh data are to be put, and one to tell how many bytes to read").

We have chosen the latter approach. It's more work that way, but it gives more insight into what operating systems
really do. Although this discussion specifically refers to POSIX (international standard 9945-1), hence also to unix,
system v, bsd, linux, minix 3, and so on, most other modern operating systems have system calls that perform the same
functions, even if the details differ. Since the actual mechanics of issuing a system call are highly machine dependent
and often must be expressed in assembly code, a procedure library is provided to make it possible to make system calls
from c programs and often from other languages as well.

It is useful to keep the following in mind. Any single-CPU computer can execute only one instruction at a time. If a
process is running a user program in user mode and need a system service, such as reading data form a file, it has to
execute a trap instruction to transfer control to the operating system. The operating system then figure out what the
calling process wants by inspecting the parameters. Then it carries out the system call and returns controls to the
instruction following the system call. In a sense, making a system call is like making a special kind of procedure
call, only system calls enter teh kernel and procedure calls do not.

To make the system call mechanism clearer, let us take a quick look at the read system call. As mentioned above, it has
three parameters: the first one specifying the file, the second one pointing to the buffer, adn the third one giving the
number of bytes to read. Like nearly all system calls, it is invoked from C programs by calling a library procedure
with the same name as the system call: read. A call from a C program might look like this:

count = read(df, buffer, nbytes);

The system call (and the library procedure) return the number of bytes actually read in count. This value is normally
the same as nbytes, but may be smaller, if for example, end of file is encountered while reading.

If the system call cannot be carried out owing to an invalid parameter or a disk error, count is set to -1, and the
error number is put in a global variable errno. Programs should always check the result of a system call to see if
na error occurred.

System call are performed in a series of steps. To make this concept clearer, let us examine the read call discuss
above. In preparation for calling the read library procedure, which actually make the read system call, the calling
program first pushes the parameters onto the stack, as shown in steps 1-3 in Fig. 1-17.

C and C++ compilers push the parameters onto the stack in reverse order for historical reasons (having to do with
making the first parameter to printf, the format string, appear on top of the start). The first and third parameters are
called by value, but the second parameter is passed by reference, meaning that the address of the buffer (indicated by
&) is passed, not the contents of the buffer. Then comes the actual call to the library procedure (step 4). This
instruction is the normal procedure call instruction used to call all procedures.

The library procedure, possibly written in assembly language, typically puts the system call number in a place where
the operating system expects it, such as a register (step5). Then it executes a TRAP instruction to switch from user
mode to kernel mode and start execution at a fixed address within the kernel (step 6). The Trap instruction is actually
fairly similar to the procedure call instruction in sense that the instruction following it is taken from a distant
location and the return address is saved on the stack for use later.

Nevertheless, the TRAP instruction also differs from teh procedure call instruction in two fundamental ways. First, as
a side effect, it switches into kernel mode. The procedure call instruction does not change the mode. Second, rather
than giving a relative or absolute address where the procedure is located, the TRAP instruction cannot jump to an
arbitrary address. Depending on the architecture, either it jumps to a single fixed location or there is an 8-bit field
in the instruction giving the index into a table in memory containing jump addresses, or equivalent.

The kernel code that starts following the trap examines the system call number and then dispatches to the correct
system call handler, usually via a table of pointers to system call handler runs (step 8). Once it has completed it work
control may be returned to the user-space library procedure at teh instruction following the trap instruction (step 9).
This procedure then return the user program in the usual way procedure calls return (step 10).

To finish the job, the user program has to clean up the stack, as it does after any procedure call (step 11). Assuming
the stack grows downward, as it often does, the compiled code increments the stack pointer exactly enough to remove
the parameters pushed before the call to read. The program is now free to do whatever it wants to do next.

In step 9 above, we said "may be returned to the user-space library procedure" for good reason. The system call may
blocked the caller, preventing it from continuing. For example, if it is trying to read from the keyboard and nothing
has been typed yet, the caller has to be blocked. In this case, the operating system will look around to see if some
other process can be run next. Later, when the desired input is available, this process will get the attention of the
system and run steps 9-11.

In the following sections, we will examine some of the most heavily used POSIX system calls, or more specifically, the
library procedures that make those system calls. POSIX has about 100 procedure calls. Some of the most important ones
are listed in Fig 1-18, grouped for convenience in four categories. In the next we will briefly examine each call to
see what it does.

To a large extent, the services offered by these calls determine most of what the operating system has to do, since the
recourse management on personal computer is minimal (at least compared to big machines with multiple users). The
services including things like creating and terminating processes, creating, deleting, reading, and writing files,
managing directories, and performing input and output.

As an aside, it is worth pointing out that the mapping of POSIX procedure calls onto system calls not one-to-one. The
POSIX standard specifies a number of procedures that a conformant system must supply, but it does not specify whether
they are system calls, library calls, or something else. If a procedure can be carried out without invoking a system
call (i.e., without trapping to the kernel), it will usually be done in user space for reasons of performance.
However, most of the POSIX procedures do invoke system calls, usually with one procedure mapping directly onto one
system call. In a few cases, especially where several required procedures are only minor variations of one another, one
system call handles more than one library call.

1.6.1 system calls for process management

The first group of calls in Fig 1-18 deals with process management. Fork is a good place to stat the discussion. Fork is
the only way to create a new process in POSIX. It creates an exact duplicate of the original process, including all the
file descriptors, registers - everything. After the fork, the original process and the copy (the parent and child) go
their separate ways. All the variables have identical values at the same time fo the fork, but since the parent's data
are copied to create the child, subsequent changes in one of them do not affect the other one. (The program text, which
is unchangeable, is shared between parent and child). The fork call returns a value, which is zero in the child and
equal to hte child's PID (Process Identifier) in the parent. using the returned PID, th two processes can see which one
is the parent process and which one is the child process.

process management

pid = fork()    create a child process identical to the parent
pid = waitpid(pid, &statloc, options)   wait for a child to terminate
s = execve(name, argv, environp)    replace a process' core image
exit(status)    terminate process execution and return status

file management

fd = open(file, how, ...)   open a file for reading, writing, or both
s = close(fd)   close an open file
n = read(fd, buffer, nbytes)    read data from a file into a buffer
n = write(fd, buffer, nbytes)   write data from buffer into a file
position = lseek(fd, offset, whence)    move the file pointer
s = stat(name &buf) get a file's status information

directory and file system management

s = mkdir(name, mode)   create a new directory
s = rmdir(name)     remove an empty directory
s = link(name1, name2) create a new entry, name2, pointing to name1
s = unlink(name)    remove a directory entry
s = umount(special, name, flag) mount a file system
s= unmount(special) unmount a file system.

miscellaneous

s = chdir(dirname)  change the working directory
s = chmod(name, mode)   change a file's protection bits
s = kill(pid, signal)   send a signal to a process
seconds = time(&seconds) get the elapsed time since jan. 1, 1970

in most cases, after a fork, the child will need to execute different code from the parent. consider the case of the
shell. It reads a command from the terminal, forks off a child process, waits for the child to execute the command, and
then reads the next command when the child terminates. To wait for the child to finish, the parent executes a waitpid
system call, which just waits until the child terminates (any child if more than one exists). Waitpid can wait for a
specific child, or for any old child by setting the first parameter to -1. When waitpid completes, the address pointed
to by the second parameter, statloc, will be set to the child process' exit status (normal or abnormal termination and
exit value). Various options are also provided, specified by the third parameter. For example, returning immediately if
no child has already existed.

Now consider how fork is sued by the shell. When a command is typed, the shell forks off a new process. This child
process must execute the user command. It does this by using the execve system call, which cause its entire core imange
to be replaced by the file named in its first parameter. (actually, hte system call itself is exec, but several library
procedures call it with different parameters and slightly different names. We will treat these as system calls here).
A highly simplified shell illustration the use of fork. waitpid, and execve is show in Fig 1-19.

while (TRUE) {
    type_prompt();
    read_command(command, parameters);

    if (fork()!=0){
        /* parent code */
        waitpid(-1, &status, 0);
    } else {
        /*child code. */
        execve(commmand, parameters, 0);
    }
}

In the most general case, execve has three parameters: the name of the file to be executed, a pointer to the argument
array, and a pointer to teh environment array. These will be described shortly. Various library routines, including
execl, execv, execle, execve, are provided to allow the parameters to omitted or specified in various ways. Throughout
this book we will use the same exec to represent the system call invoked by all of these.

Let us consider the case of the command such as

cp file1 file2

used to copy file1 to file2. After the shell has forked, the child process locates and executes the file cp and passes
to it the names of the source and target files.

The main program of cp (and main program of most other C programs) contains the declaration

main(argc, argv, envp)

where argc is a count of the number of items on the command line, including the program name. For example above, argc
is 3.

The second parameter, argv is a pointer to an array. Element i of that array is a pointer to the ith string on the
command line. In our example, argv[0] would point to the string 'cp', argv[1] would point to the string 'file1', and
argv[2] point to the sting 'file2'.

The third parameter of main, envp, is a pointer to the environment, an array of strings containing assignments of the
form name = value used to pass information such as the terminal type and home directory name to programs. There are
library procedures that programs can call to get the environment variables, which are often used to customize how a
user wants to perform certain tasks (e.g., the default printer to use). In Fig 1-19, no environment is passed to the
child, so the third parameter of execve is a zero.

if exec seems complicated, do not despair; it is (semantically) the most complex of all the posix system calls. all the
other ones are much simpler. As an example one, consider exit, which process should use when they are finished executing
It has one parameter, the exit status (0 to 255), which is the returned to the parent via statloc in the waitpid system
call.

Processes in unix have their memory divided up into three segments: the text segment (i.e., the program code), the data
segment (i.e., the variables), and the stack segment. The data segment grows upward and the stack grows downward, as
shown in Fig 1-20. Between them is a gap of unused address space. The stack grows into the gap automatically, as needed,
but expansion of the data segment is done explicitly by suing a system call, brk, which specifies the new address where
the data segment is to end. This call, however, is not defined by the posix standard, since programmers are encouraged
to use the malloc library procedure for dynamically allocating storage, and the underlying implementation of malloc
was not thought to be a suitable subject for standardization since few programmers use it directly and it is doubtful
that anyone even notices that brk is not in POSIX.

1.6.2 System calls for file management

many system calls relate to the file system. In this section we will look at calls that operate on individual files; in
the next one we will examine those that involve directories or the file system as a whole.

To read or write a file, it must first be opened. This call specifies the file name to be opened, either as an absolute
pathname or relative to the working directory, as well as a code of O_RDONLY, O_WRONLY, or O_RDWR, meaning open for
reading, writing, or both. To create a new file, the O_CREAT parameter is used. The file descriptor returned can then
be used for reading writing. Afterward, the file can be closed by close, which makes the file descriptor available for
reuse on a subsequent open.

The most heavily used call are undoubtedly read and write. We saw read earlier. Write has the same parameters.

Although most programs read and write files sequentially, for some applications programs need to be able to access any
part of a file at random. Associated with each file is a pointer that indicates the current position in the file. When
reading (writing) sequentially, it normally point to the next byte to be read (written). The lseek call can begin
anywhere in the file.

Lseek has three parameters: the first is the file descriptor for the file, the second is a file position, and the third
tells whether the file position is relative to the beginning of the file, the current position, or the end of the file.
The value returned by lseek is absolute position in eh file (by bytes) after chaning the pointer.

For each file, unix keeps track of the file mode (regular file, special file, directory, and so on), size, time of last
modification, and other information. Programs can ask to see this information via the stat system call. The first
parameter specifies the file to to inspected; the second one is a pointer to a structure where the information is to be
put. The fstat calls does the same thing for an open file.

1.6.3 system calls for directory management

In this section we will look at some system calls that relate more to directories or the file system as a whole, rather
than just to  one specific file as in the previous section. The first two calls, mkdir and rmdir, create and remove
empty directories, respectively. The next call is link Its purpose is to allow the same file to appear under two or more
names, often in different directories. A typical use is to allow several members of the same programming team to share
a common file, with each of them having the file appear in his own directory, possibly under different names. Sharing a
file is not the same as giving every team member a private copy; having a shared file means that changes that any
member of the team makes are instantly visible to the other members - there is only one file. When copies are made of
file, subsequent changes made to one copy do not affect others.

To see how link works, consider the situation of Fig 1-21(a). Here are two users, ast and jim, each having his own
directory with some files. If ast now executes a program containing the system call

link('use/jim/memo', 'usr/ast/note');

the file memo in jim's directory is now entered into ast's directory under the name note. Thereafter, /usr/jim/memo and
/usr/ast/note refer to teh same file. As an aside, whether user directories are kept in /usr, /user, /home, or somewhere
else is simply a decision made by the local system administrator.

Understanding how link works will probably make it clearer what it does. Every file in Unix has a unique number, its
i-number, that identifies it. This i-number is an index into a table of i-nodes, one per file, telling who owns the
file, where its disk blocks are, and so on. A directory is simply a file containing a set of (i-number, ascii name)
pairs. In the first versions of Unix, each directory entry was 16 bytes - 2bytes for teh i-number and 14 bytes for the
name. now a more complicated structure is needed to support long file names, but conceptually a directory is still a
set of (i-number, ascii name) pairs. In Fig 1-21, mail has i-number 16, and so on. What link does is simply create a
brand new directory entry with a (possibly new) name, using the i-number of an existing file. In Fig 1-21(b), two
entries has the same i-number (70) and thus refer to the same file. If either one is later removed, using the unlink
system call, the other one remains. If both are removed, unix sees that no entries to the file exist (a filed in the
i-node keeps track of the number of directory entries pointing to the file), so the file is removed from the disk.

As we have mentioned earlier, the mount system call allows two file systems to be merged into one. A common situation
is to have the root file system, containing the binary (executable) versions of the common commands and other heavily
used files, on a hard disk (sub)partition and user files on another (sub)partition. Further, the user can then insert
a USB disk with files to be read.

By executing the mount system call, the USB file system can be attached to the root file system, as shown in Fig 1-22.
A typical statement is in C to mount is

mount("/dev/sdb0", "/mnt", 0);

where the firs parameter is the name of a block special file for USB drive 0, the second parameter is the place in the
tree where it is to be mounted, and the third parameter tells whether the file system is to be mounted read-write or
read-only.

After the mount call, a file on drive 0 can be accessed by just using its path from the root directory or the working
directory, without regard to which dive it is on. In fact, second, third, and fourth drives can also be mounted
anywhere in the tree. The mount call makes it possible to integrate removable media into a single integrated file
hierarchy, without having to worry about which device a file is on. Although this example involves CD-ROMs, portions of
hard disks (often called partitions or minor devices) can also be mounted this way, as well as external hard disks as
USB sticks. When a file system is no longer needed, it can be unmounted with the unmount system call.

1.6.4 miscellaneous system calls

A variety of other system calls exist as well. We will look at just four of them here. The chdir call changes the
current working directory, After the call

chdir("/usr/ast/test");

an open on the file xyz will open /use/ast/test/xyz. The concept of a working directory eliminates the need for typing
(long) absolute path names all the time.

In unix every file has a mode used for protection. The mode includes the read write execute bits for the owner, group
and others. The chmod system call makes it possible to change the mode of the file. for example, to make a file
readonly by everyone except the owner one could execute

chmod("file", 0644);

The kill system call is the way users and user processes send signals. If a process is prepared to catch a particular
signal, then when it arrives, a signal handler is run. If the process is not prepared to handle a signal, then its
arrival kills the process (hence the name of call).

Posix defines a number of procedures for dealing with time. For example, time just return the current time in seconds,
with 0 corresponding to jan 1, 1970 at midnight (just as teh day was starting, not ending). On computers using 32-bit
words, the maximum values time can return is 2^32 -1 seconds (assuming an unsigned integer is used). this value
corresponds to a little over 136 years. Thus in the year 2106, 32-bit unix system will go berserk, not unlike the
famous y2k problem that would have wreaked havoc with the world's computers in 2000, were it not for the massive effort
the IT industry put into fixing the problem. If you currently have a 32-bit unix system, you are advised to trade it in
for a 64-bit one sometime before 2106.

1.6.5 the windows 32 api

so far we have focused primarily on unix, now it is time to look briefly at windows. windows and unix differ in a
fundamental way in their respective programming models. A unix program consists of code that does something or other,
making system call to have certain services performed. In contrast, a windows program is normally event driven. The
main program waits for some event to happen, then calls a procedure to handle it. Typical events are keys being struck,
the mouse being moved, a mouse button being pushed, or a USB drive inserted. handlers are then called to process the
event, update the screen and update the internal program state. All in all, this leads to a somewhat different style of
programming than with unix. but since the focus of this book is on operating system function and structure, these
different programming models will not concern us much more.

Of course, windows also has system calls, with unix, there is almost a one to one relationship between the system call
(e.g., read) and the library procedures (e.g., read) used to invoke the system calls. In other words, for each system
call, there is roughly one library procedure that is called to invoke it,, as indicated in Fig 1-17. Furthermore,
POSIX has only about 100 procedure calls.

With windows, the situation is radically different, To start with, the library calls and teh actual system calls are
highly decoupled. Microsoft has defined a set of procedures called the win32 api (application Programming Interface)
that programmers are expected to use to get operating system services. This interface is (partially) supported on all
versions of windows since windows 95. By decoupling the api interface from teh actual system calls, microsoft retains
the ability to change teh actual system calls in time (even from release to release) without invalidating existing
programs. What actually constitutes win32 is also slightly ambiguous because recent versions of windows have many new
calls that were not previous available. In this section, win32 means the interface supported by all version of windows.
win32 provides compatibility among versions of windows.

The number of win32 api calls is extremely large, numbering in the thousands. Furthermore, while many of them do invoke
system calls, a substantial number are carried out entirely in user space. As a consequence, with windows it is
impossible to see what is system call (i.e., performed by the kernel) and what is simply a user-space library call. In
fact, wht is a system call in one version of windows may be done in user space in a different version, and vice versa.
When we discuss the windows system calls in this book, we will sue the win32 procedures (where appropriate) since
Microsoft guarantees that these will be stable over time. but it is worth remembering that not all fo them are true
system calls (i.e., traps to the kernel).

The win32 api has a huge number of calls for managing windows, geometric figures, text, fonts, scrollbars, dialog boxes
memus, and other features of the GUI. To the extent that the graphics subsystem runs in the kernel (true on some
versions of windows but not on all), these are system calls; otherwise they are just library calls. Should we discuss
these calls in this book or not? since they are not really related to the function of an operating system, we have
decided not to, even though they may be carried out by the kernel. Readers interested in the win32 api should consult
one of the many books on the subject (e.g., hart, 1997; rector and Newcomer, 1997; and Simon, 1997)

Even introducing all the win32 api calls here is out of the question, so we will restrict ourselves to those calls that
roughly correspond to the functionality of the unix call listed in Fig 1-18. These are listed in Fig 1-23.

Let us now briefly go through the list of Fig 1-23. CreateProcess creates a new process. It does the combined work of
fork and execve in unix. It has many parameters specifying the properties of the newly created processes. Windows does
not have a process hierarchy as unix does so there no concept of a parent process and a child process. After a process
is created, the creator and createe are equals. WaitForSingleObject is used to wait for an event. Many possible events
can be waited for. If the parameter specifies a process, then teh caller waits for hte specified process to exit, which
 is done using ExitProcess.

The next six call operate on files and are functionally similar to their unix counterparts although they differ in the
parameters and details. Still, files can be opened, closed, read, and write pretty much as in unix. The SetFilePointer
and GetFileAttributesEx calls set the file position and get some of the file attributes.

Windows has directories and they are created with CreateDirectory and RemoveDirectory API calls, respectively. There is
also a notion of a current directory, set by SetCurrentDirectory. The current time of day is acquired using
GetLocalTime.

The win32 interface does not have links to files, mounted file systems, security, or signals, so the calls
corresponding to the unix ones do not exist. Of course, win32 has a huge number of other calls that unix does not have,
especially for managing the GUI. Windows vista has an elaborate security system and also supports file links. Windows 7
and 8 and yet more features and system calls.

One last note about win32 is perhaps worth making. win32 is not a terribly uniform or consistent interface. The main
culprit here was the need to be backward compatible with hte previous 16-bit interface used in Windows 3.x.

1.7 operating system structure

now that we have seen wht operating systems look like on the outside (i.e., the programmer's interface) it is time to
take a look inside. In the following sections, we will examine six different structures that have been tried, in order
to get some idea of teh spectrum of possibilities. These are by no means exhaustive, but they give an idea of some
designs that have been tried in practice. The six designs we will discuss here are monolithic systems, layered systems,
microkernels, client-server systems, virtual machines and exokernels.

1.7.1 Monolithic systems

By far the most common organization, in the monolithic approach hte entire operating system runs as a single program in
kernel mode. The operating system is written as a collection of procedures, linked together into a single large
executable binary program. When this technique is used, each procedure in the system is free to call any other one, if
the latter provides some useful computation that teh former needs. Being able to call any procedure you want is very
efficient, but having thousands of procedures that can call each other without restriction may also led to a system
that is unwieldy and difficult to understand. Also, a crash in any of these procedures will take down hte entire
operating system.

To construct the actual object program of the operating system when this approach is used, one first compiles all the
individual procedures (or the files containing the procedures) and then binds them all together into a single
executable file using the system linker. In terms of information hiding, there is essentially none - every procedure is
visible to every other procedures (as opposed to a structure containing modules or packages, in which much of the
information is hidden away inside modules, and only the officially designated entry points can be called from outside
the module).

Even in monolithic systems, however, it is possible to have some structure. The services (system calls) provided by the
operating system are requested by putting the parameters in a well-defined place (e.g., on the stack) and then executing
a trap instruction. This instruction switches the machine from user mode to kernel mode and transfers control to the
operating system, show as step 6 in Fig 1-17. the operating system then etches the parameters and determines which
system call is to be carried out. After that, it indexes into a table that contains is slot k a pointer to the
procedure that carries out system call k (step 7 in Fig 1-17).

This organization suggests a basic structure for the operating system:
1. A main program that invokes the requested service procedure
2. A set of service procedures that carry out the system calls
3. A set of utility procedures tha help the service procedures.

In this model, for each system call there is one service procedure that takes care of it and executes it. The utility
procedures do things that are needed to by several service procedures, such as fetching data from user programs. This
division of the procedures into three layers is shown in Fig 1-24.

In addition to the core operating system that is loaded when the computer is booted, many operating system support
loadable extensions, such as i/o device drivers and file systems. These components are loaded on demand. In unix they
are called shared libraries. In windows they are called dlls (dynamic link libraries. They have file extension .dll and
the c:\windows\system32 directory on windows systems has well over 1000 of them.

1.7.2 layered systems

A generalization of the approach of Fig 1-24 is to organize the operating system as a hierarchy of layers. each one
constructed upon the one below it. The first system constructed in this way is the system built at the technische
Hohgeschool eindhoven in the netherlands by e. w. dijkstra (1968) and his strudent.
The THE system was a simple batch system for a dutch omputer, the Eletrologica x8, which had 32k of 27-bits words (bits
were expensive back them).

The system had six layers, as shown in Fig 1-25. Layer 0 dealt with allocation of th processor, switching between
processes when when interrupts occurred or timers expired. Above layer 0, the system consisted of sequential processes,
each of which would be programmed without having to worry about the fact that multiple processes were running on a
single processor. In other words, layer 0 provided the basic multiprogramming of CPU.

5       the operator
4       user programs
3       input/output management
2       operator-process communication
1       memory and drum management
0       processor allocation and multiprogramming

layer 1 did the memory management. It allocated space for processes in main memory and on a 512k word drum used for
holding parts of processes (pages) for which there was no room in main memory. Above layer 1, processes did not have to
worry about whether they were in memory or on the drum; the layer 1 software took care of making sure pages were brought
into memory at the moment they were needed and removed when they were not needed.

Layer 2 handled communication between each process and the operator console (that is , the user). On top of this layer
each process effectively had its own operator console. Layer 3 took care of managing the i/o devices and buffering the
information steams to and from them. Above layer 3 each process could deal with abstract i/o devices with nice
properties, instead of real devices with many peculiarities. layer 4 was where the user program were found. They did
not have to worry about process, memory, console, or i/o management. The system operator process was located in layer 5.

A further generalization of the layering concept was present in the MULTICS system. Instead of layers, MULTICS was
described as having a series of concentric rings, with the inner ones being more privileged than the outer ones (which
is effectively the same thing). When a procedure in an outer ring wanted to call a procedure in an inner rings, it had
to make the equivalent of a system call, that is , a TRAP instruction whose parameters were carefully checked for
validity before the call was allowed to processed. Although the entire operating system was part of the address space
of each user process in MULTICS, the hardware made it possible to designate individual procedures (memory segments,
actually) as protected against reading, writing, or executing.

Whereas the THE layering scheme was really only a design aid, because all the parts of teh system were ultimately linked
together into a single program, in MULTICS, the ring mechanism was very much present at run time and enforced by the
hardware. The advantage of the ring mechanism is that it can easily be extended to structure use subsystems. For
example, a professor could write a program to test and grade student programs and run this program in ring n, with the
student program running in n+1 so that they could not change their grads.

1.7.3 microkernels

with the layered approach, teh designers have a choice where to draw the kernel user boundary. Traditionally, all the
layers went in the kernel, but that is not necessary. In fact, a strong case can be made for putting as little as
possible in kernel mode because bugs in the kernel can bring down the system instantly. In contrast, user processes can
be set up to have less power so that a bug there may mot be fatal.

Various researchers have repeatedly studied the number of bugs per 1000 lines of code (e.g., Basilli and Perricone,
1984; and Ostrand and Weyuker, 2002). bug density depends on module size, module age, and more, but a ballpark figure
for serous industrial systems is between two and ten bugs per thousand lines of code. This means that a monolithic
operating system of five million lines of code is likely to contain between 10,000 and 50,000 kernel bugs. Not all of
these are fatal, of course, since some bugs may be things like issuing an incorrect error message in a situation that
rarely occurs. Nevertheless, operating systems are sufficiently buggy that computer manufacturers put reset buttons on
them (often on the from panel), something the manufacturers of TV sets, stereos, and cars do not do, despite the large
amount of software in these devices.

The basic idea behind the microkernel design is to archive high reliability by splitting the operating system up into
small, well defined modules, only one of which - the microkernel - runs in kernel mode and the rest run as relatively
power less ordinary user processes. In particular, by running each device driver and file system as a separate user
process, a bug in one of these can crash that component, but cannot crash the entire system. Thus a bug in the audio
driver will cause the sound to be garbled or stop, but will not scratch the computer. In contrast, in a monolithic
system with all the drivers in the kernel, a buggy audio dirver can easily reference an invalid memory address and bring
the system to a grinding halt instantly.

many microkernels have been implemented and deployed for decades (Haertiget al.. 1997; heiser et al., 2006; Herder et
al., 2006; Heldebradn, 1992; kirssh et, al, 2005; liedtke, 1993, 1995, 1996; pike et, al, 1992, and Zuberi et, al,1999).
with the exception of osX, which is based on the math microkernel (Accetta et, al., 1986), common desktop operating
systems do not use microkernels. however, they are dominant in real-time, industrial, avionics, and military
applications that are mission critical and have every high reliability requiements. A few of the better-known
microkernels include Integrity, K42, L4, PikeOS QNX Symbian, and MINIX 3. We now give a brief overview of MINIX 3, which
has taken the idea of modularity to the limit, breaking most of the operating system up into a number of independent
user mode processes. MINIX 3 is a posix conformant, open source system freely available at www.minix3.org.

The MINIX 3 microkernel is only about 12,000 lines of C and some 1400 lines assembler for very low-level functions such
as catching interrupts and switching processes. The C code managers and schedules processes, handles interprocess
communication (by passing messages between process), and offers a set of about 40 kernel calls to allow the rest of
operating system to do its work. These calls perform functions like hooking handlers to interrupts, moving data between
address spaces, and installing memory maps for new processes. The process structures of MINIX 3 is shown in Fig 1-26,
with the kernel call handlers labeled sys. The device driver for the clock is also in the kernel because the scheduler
interacts closely with it. The other device drivers run as separate user processes.

Outside the kernel, the system is structured as three layers of processes all running in uer mode. The lowest layer
contains teh devices drivers. Since they run in user mode, they do not have physical access to the i/o port space and
connot issue i/o commands directly. Instead, to program an i/o device, the driver builds a structure telling which
values to write to which i/o ports and makes a kernel call telling the kernel to do the write. This approach means that
the kernel can check to see that the driver is writing (or reading) from i/o it is authorized to use. Consequently (and
unlike a monolithic design), a buggy audio driver cannot accidentally write on the disk.

Above the drivers is another user-mode layer containing the servers, which do most of the work of the operating system.
One or more file servers manage the file system(s), the process manager creates, destroys, and manages processes, and
so on. user programs obtain operating system services by sending shot messages to the servers asking for the posix
system calls. For example, a process needing to do a read sends a message to one of the file servers telling it what to
read.

One interesting server is teh reincarnation server, whose job is to check if the other servers and drivers are
functioning correctly. in the event that a faulty one is detected, it is automatically replaced without any user
intervention. In this way, the system is self healing and can achieve high reliability.

The system has many restrictions limiting the power of each process. As mentioned, drivers can touch only authorized i/o
ports, but access to kernel calls is also controlled on a per-process basis, as is the ability to send message to the
other processes. Processes can also grant limited permission for other processes to have the kernel access their address
spaces. As an example, a file system can grant permission for the disk driver to let the kernel put a newly read-in
disk block at a specific address within the file system's address space. The sum total of all these restrictions is that
each driver and server has exactly the power to do its work and nothing more, thus greatly limiting the damage a buggy
component can do.

An idea somewhat related to having a minimal kernel is to put the mechanism for doing something in the kernel but not
the policy. To make this point better, consider the scheduling of processes. A relatively simple scheduling algorithm
is to assign a numerical priority to every process and then have the kernel run the highest-priority process that is
runnable. The mechanism - in the kernel - is to look for the highest - priority process and run it. The policy -
assigning priorities to process - can be done by user-mode processes. In this way, policy and mechanism be decoupled and
the kernel can be made smaller.
"""