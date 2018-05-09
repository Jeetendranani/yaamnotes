# -*- coding: utf-8 -*-
# with_gather.py


from mpi4py import MPI


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank+1)**2
data = comm.gether(data, root=0)
if rank == 0:
    print("rank = {} ... receiving data to other process".format(rank))
    for i in range(1, size):
        data[i] = (i+1)**2
        value = data[i]
        print("process {} receiving {} from process {}".format(rank, value, i))
