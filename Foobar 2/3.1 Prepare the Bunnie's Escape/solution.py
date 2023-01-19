import copy
 
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

    max_value = 10000000
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
    r = len(map)
    c = len(map[0])
    rows = [str(i) for i in range(r)]
    cols = [chr(i) for i in range(97, 97+c)]
    
    nodes = []
    weights = []
    results = []
    goal = rows[r-1] + cols[c-1]

    #Set nodes/weights
    for i in range(r):
        for j in range(c):
            nodes.append(rows[i] + cols[j])
            weights.append(1 if map[i][j] == 0 else 1001)

    #Iterate through weights
    for idx, weight in enumerate(weights):
        new_weights = copy.deepcopy(weights)
        if (weight > 1000):
            new_weights[idx] = weight - 1000

        #Build graph
        init_graph = {}
        for node in nodes:
            init_graph[node] = {}
        
        #Connect to right
        for i in range(r):
            for j in range(c-1):
                name = rows[i] + cols[j]
                right = rows[i] + cols[j+1]
                init_graph[name][right] = max(new_weights[nodes.index(name)], new_weights[nodes.index(right)])
        
        #Connect to below
        for i in range(r-1):
            for j in range(c):
                name = str(rows[i]) + cols[j]
                below = str(rows[i+1]) + cols[j]
                init_graph[name][below] = max(new_weights[nodes.index(name)], new_weights[nodes.index(below)])

        results.append(dijkstra(Graph(nodes, init_graph), "0a")[1][goal] + 1)
    return min(results)

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
