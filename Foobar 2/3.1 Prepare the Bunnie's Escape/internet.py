import sys
import copy
import itertools
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]

def dijkstra(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    shortest_path = {}

    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value 
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
 
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def solution(map):
    h = len(map)
    w = len(map[0])
    # Give a name to columns and rows
    cols = [str(x) for x in range(w)]
    rows = [chr(x) for x in range(97, (97+h))]
    # Give a name to each node
    nodes = [c+r for (c,r) in itertools.product(rows, cols)]
    # Set the cells at 1, and walls at 1001
    weights = [(item*1000)+1 for sublist in map for item in sublist]
    # Initialize a list for results
    results = []

    for i, weight in enumerate(weights):
        # only run for the walls,
        # changing the value of the
        # specific wall to 1 to remove it
        if weight > 1000:
            new_weights = copy.deepcopy(weights)
            # Removing the wall
            new_weights[i] = weights[i] - 1000
            # Creating the graph
            init_graph = {}
            for node in nodes:
                init_graph[node] = {}

            for i, node in enumerate(nodes):
                # If node i is not the last one
                if i < len(nodes) -1:
                    # and it's not on the rightmost column
                    if (i+1) % w != 0:
                        # Connect with next node (right)
                        init_graph[node][nodes[i+1]] = max(new_weights[i], new_weights[i+1])
                # If node i is not on the last row
                if i < len(nodes) - w:
                    # connect with node below
                    init_graph[node][nodes[i+w]] = max(new_weights[i], new_weights[i+w])
            
            print(init_graph)

            graph = Graph(nodes, init_graph)
            # Find the shortest path for the specific graph
            shortest_path = dijkstra(graph, "a0")

            result = shortest_path[1][nodes[-1]] +1 # add 1 because Dijkstra do not count the starting node as a step
            # Save the result in our list
            results.append(result)
    return min(results) # Return the shortest path

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
