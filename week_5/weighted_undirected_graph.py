
class Edge:
    def __init__(self, to, weight):
        self.connected_vertex = to
        self.weight = weight
    
    def __str__(self):
        return "Edge, connected to:{}, weight:{}".format(self.connected_vertex, self.weight)
    
class WeightedGraph:
    def __init__(self):
        self.adjacency_matrix = {}
    
    def add_edge(self, v, w, weight):
        if v not in self.adjacency_matrix:
            self.adjacency_matrix[v] = []
        
        if w not in self.adjacency_matrix:
            self.adjacency_matrix[w] = []
        
        edge_v = Edge(w, weight=weight)
        edge_w = Edge(v, weight=weight)

        self.adjacency_matrix[v].append(edge_v)
        self.adjacency_matrix[w].append(edge_w)

        print("Added edge from {} to {}, weight {}.".format(v,w,weight))