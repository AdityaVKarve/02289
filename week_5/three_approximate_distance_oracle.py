from weighted_undirected_graph import WeightedGraph
from djikstra import Djikstra
import math
from random import random


## INITIALISE GRAPH
graph = WeightedGraph()
graph.add_edge(1,2,10)
graph.add_edge(2,3,5)
graph.add_edge(2,9,50)
graph.add_edge(3,4,50)
graph.add_edge(3,5,10)
graph.add_edge(4,6,100)
graph.add_edge(5,9,75)
graph.add_edge(5,10,20)
graph.add_edge(6,10,50)
graph.add_edge(7,10,40)
graph.add_edge(8,9,75)



def pre_processing(graph, djikstra):
    #INITIALISE DJIKSTRA
    


    #GET GAMMA (Probability of picking element)
    gamma = math.pow(len(graph.adjacency_matrix), -1/2)

    R = []

    for i in list(graph.adjacency_matrix.keys()):
        if random() <= gamma:
            R.append(i)

    distance_matrix = {}
    print(R) 
    for i in R:
        distance_matrix[i] = djikstra.run_djikstra(i)

    p = {}
    for i in range(1,11):
        min_distance = 100000
        for r in R:
            if distance_matrix[r][i] < min_distance:
                p[i] = [r,distance_matrix[r][i]]
                min_distance = distance_matrix[r][i]

    S = {}
    for i in range(1,11):
        S[i] = []
        if i in R:
            continue
        distances = djikstra.run_djikstra(i)
        for d in list(distances.keys()):
            if d != i and distances[d] < p[i][1]:
                S[i].append({d:distances[d]})
    print("R")
    print(R)
    print("__________________")
    print("P")
    print(p)
    print("__________________")
    print("S")
    print(S)
    print("__________________")
    return [distance_matrix,S,p]

def query_distance(u,v,R,S,p):
    #Case 1: If u/v in R:
    if u in list(R.keys()):
        print("Case 1")
        return R[u][v]
    elif v in list(R.keys()):
        print("Case 1")
        return R[v][u]

    #Case 2: if u, v in same S:
    for k in S[u]:
        if list(k.keys())[0] == v:
            print("Case 2")
            print(k)
            return k[v]
    for k in S[v]:
        if list(k.keys())[0] == u:
            print("Case 2")
            return k[u]

    #Case 3, if case 1 and 2 not met
    else:
        print("Case 3")
        p_u = p[u][0]
        d_pu = p[u][1]
        p_v = p[v][0]
        d_pv = p[v][1]
        print("p_u:{} d_pu:{} p_v:{} d_pv:{} R_pu:{} R_pv:{}".format(p_u,d_pu,p_v,d_pv,R[p_u][v],R[p_v][u]))
        return min(d_pu + R[p_u][v], d_pv + R[p_v][u])
djikstra = Djikstra(graph=graph)
R,S,p = pre_processing(graph=graph, djikstra = djikstra)
full_djikstra = {}
for i in range(1,11):
    full_djikstra[i] = djikstra.run_djikstra(i)
while True:
    inp_u = int(input("Enter u (q to quit):"))
    inp_v = int(input("Enter v (q to quit):"))
    print("Queried distance:{}".format(query_distance(inp_u,inp_v,R,S,p)))
    print("Actual distance:{}".format(full_djikstra[inp_u][inp_v]))


