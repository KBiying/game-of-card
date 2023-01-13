from pulp import *
import numpy as np

    # # ----------------- Problem --------------------------
    # prob2 = LpProblem("minimzie load", sense=LpMinimize)

    # # ----------------- Variables ------------------------
    # z = pulp.LpVariable.dicts('z', indices = (k_set, servers), lowBound = 0, upBound= 1, cat = LpContinuous)

    # # ---------------- -Objective ------------------------
    # for v in servers:
    #     prob2 += b_resource[v]/total_resource[v] + pulp.lpSum((gama[k] / total_resource[k]) * z[k][v] for k in k_set)
    
    # # ----------------- Constraints ----------------------
    # for v in servers:
    #     prob2 += b_resource[v]/total_resource[v] + pulp.lpSum((gama[k] / total_resource[k]) * z[k][v] for k in k_set) <= 1
    
    # for k in k_set:
    #     prob2 += pulp.lpSum(z[k][v] for v in servers) == 1
    
    # for k in k_set:
    #     for v in placed_server:
    #         prob2 += z[k][v] == 0 
    # # ---------------- Solving ---------------------------
    # prob2.solve()

    # for v in prob2.variables():
    #     logging.info('{} = {}'.format(v.name, v.varValue))
    
    # x = {}

    # for k in k_set:
    #     for v in servers:
    #         x[(k, v)] = z[k][v].value()
sfcs = ["1", "2"]# f      
vnfs = ["1", "2"]# i 
servers = ["1", "2" ,"3"]# v
o = [   #vnfs
        # 1    2
        ["1", "2"], # 1 sfcs
        ["2", "3"], # 2
    ]
o = makeDict([sfcs, vnfs], o, None)
o_vnf = {}

