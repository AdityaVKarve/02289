from weighted_undirected_graph import WeightedGraph
class Djikstra:
    def __init__(self,graph: WeightedGraph):
        self.graph = graph
    
    def run_djikstra(self, start_vertex):
        visited_nodes = []
        unvisited_nodes = [start_vertex]
        distances = {start_vertex:0}
        ctr = 0
        while unvisited_nodes != []:
            ctr += 1
            current_node = unvisited_nodes[0]
            visibile_edges = self.graph.adjacency_matrix[current_node]
            for v in visibile_edges:
                weight = v.weight
                connected_vertex = v.connected_vertex
                if connected_vertex not in list(distances.keys()):
                    distances[connected_vertex] = distances[current_node] + weight
                elif distances[connected_vertex] > distances[current_node] + weight:
                    distances[connected_vertex] = distances[current_node] + weight
                if connected_vertex not in visited_nodes:
                    unvisited_nodes.append(connected_vertex)
            visited_nodes.append(unvisited_nodes[0])
            del unvisited_nodes[0]

        return dict(sorted(distances.items()))
        
    

