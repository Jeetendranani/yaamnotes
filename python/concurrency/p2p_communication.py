# -*- coding: utf-8 -*-
# p2p_communication.py


from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.rank
print("my rank is : ", rank)

if rank == 0:
    data = 100000000
    destination_process = 4
    comm.send(data, dest=destination_process)
    print("sending data {} to process {}".format(data, destination_process))

if rank == 1:
    destination_process = 8
    data = "hello"
    comm.send(data, dest=destination_process)
    print("sending data {}: to processes {}".format(data, destination_process))

if rank == 4:
    data = comm.resv(source=0)
    print("data received is = {}".format(data))

if rank == 8:
    data1 = comm.resv(source=1)
    print("data1 received is {}".format(data1))