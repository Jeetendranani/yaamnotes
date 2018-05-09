# -*- coding: utf-8 -*-
# with_scatter.py


from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    array_to_share = [i for i in range(1, 3)]
else:
    array_to_share = None

recvbuf = comm.scatter(array_to_share, root=0)
print("process = {} recvbuf = {}".format(rank, array_to_share))
