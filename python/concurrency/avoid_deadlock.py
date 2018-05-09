# -*- coding: utf-8 -*-
# avoid_dead_lock.py


from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
print("my rank is : ", rank)

if rank == 1:
    data_send = 'a'
    destination_process = 5
    source_process = 5
    data_received = comm.recv(source=source_process)
    comm.send(data_send, dest=destination_process)
    print("sending data {} to process {}".format(data_send, destination_process))
    print("data received is {}".format(data_received))

if rank == 5:
    data_send = 'b'
    destination_process = 1
    source_process = 1
    comm.send(data_send, dest=destination_process)
    data_received = comm.recv(source=source_process)
    print("sending data {} to process {}".format(data_send, destination_process))
    print("data received is {}".format(data_received))

