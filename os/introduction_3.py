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
"""