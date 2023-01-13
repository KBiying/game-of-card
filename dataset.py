    sfcs = ["1", "2"]# f      
    vnfs = ["1", "2"]# i 
    servers = ["1", "2" ,"3"]# v
    y_edge_lp = {}
    y_cloud_lp = {}
    timer = {}
    t1 = 10
    t2 = 50
    # Backup cost of sfcs f
    w = {
        "1": 12,
        "2": 12,
    }  

    #每个server上的total resource 
    total_resource = {
        "1": 16,# origin18 test 30
        "2": 18,
        "3": 16,
    }

    # resouces demand of VNFs i of sfcs f
    beta = [   # vnfs
        # 1 2
        [8, 4], # 1 sfcs
        [8, 4], # 2
    ]
    beta = makeDict([sfcs, vnfs], beta, 0)
    # Resource demand on v before deploying static backups server v 被用了的资源
    a_resource = {
        "1": 8,
        "2": 12,
        "3": 4,
    }
    v_resource = {
        "1": 8,
        "2": 4,
    }
    # Server holding the VNF i of   f
    o = [   #vnfs
        # 1    2
        ["1", "2"], # 1 sfcs
        ["2", "3"], # 2
    ]
    o = makeDict([sfcs, vnfs], o, None)
    vnfs_of_sfc = {
        "1":["1", "2"],
        "2":["1", "2"],
    }
    k_set= ["1","2"]                        # 随时到达的动态备份集
    kth = 1                                   # 记录目前的在备份 第k个 dynamic backup
    gama = {                                # resource demand of the dynamic backup k
        "1": 8,
        "2": 4,
    }        
    b_resource = {}                         # compute current resource demand on server v before deploy dynamic backup.
    # o_vnf = {"1":["1","2"], "2":["2","3"]}  # 原vnf1、2存放在哪些server上
    # o_staticBackup = {"1":[], "2":[]}       # 静态备份vnf 1、2 存放在哪些个server上
    o_vnf = {}
    o_staticBackup = {}
    placed_server = {"1":[], "2":[]}        # 放了 vnf1和静态备份的server合集
    deploying = {}
    deploying_list = []                  
    load_max = []
    n = 1
    bound_n = 10                           # n迭代的次数                        
    eta = {}
    overflow = True
    delta = {}
    x = {}
    p = 2
    epsilon = random.uniform(1,(1+p)/p)
    remaining_servers = copy.deepcopy(servers)
    qualified_server = ""   
    
    # init varable
    for k in k_set:
        for v in servers:
            x[(k, v)] = 0
      
    for f in sfcs:
        for i in vnfs:
            if i not in o_vnf:
                o_vnf[i] = []
            o_vnf[i].append(o[f][i])