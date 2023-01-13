import logging
import random
from pulp import *

sfcs = []
vnfs_of_sfc = {}
servers = []
vnfs = []
NUM = 10
num_of_vnfs = 5
total_resource = {}
o = []
for i in range(1,NUM+1):
    sfcs.append(str(i))
print(sfcs)
for i in range(1, num_of_vnfs):
    vnfs.append(str(i))
print("vnfs = ",vnfs)

for f in sfcs:
    vnfs_of_sfc[f] = []
    for i in range(1, num_of_vnfs):
        vnfs_of_sfc[f].append(str(i))
print("vnfs_of_sfc", vnfs_of_sfc)

for i in range(1, NUM+2):
    servers.append(str(i))
print(servers)

v_resource = {}

for i in vnfs:
    v_resource[i] = random.randint(1, 10)
print(v_resource)

for v in servers:
    total_resource[v] = random.randint(5, 30)

print(total_resource)
w = {}
for f in sfcs:
    cost = 0
    for i in vnfs_of_sfc[f]:
        cost += v_resource[i]
    w[f] = cost
print(w)


#随机分配
for j in range(len(sfcs)):
    temp = []
    for i in vnfs:
        place = str(random.randint(1,NUM+1))
        temp.append(place)
    o.append(temp)
print("o = ", o)
o = makeDict([sfcs, vnfs], o, None)
for i in sfcs:
    print("o[i] = ",o[i])
        





