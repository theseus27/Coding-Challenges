#GRAPHS
    #O(|V| + |E|)

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph.keys():
        return None
    
    for node in graph[start]:
        if node not in path:
            nextpath = find_path(graph, node, end, path)
            if nextpath: return nextpath
    return None

def get_vertices(graph):
    return list(graph.keys())

def get_edges(graph):
    edges = []  #List of sets
    for vertex in graph:
        for relation in graph[vertex]:
            if {vertex, relation} not in edges:
                edges.append({vertex, relation})
    return edges

#Dictionary representation
graph = {
    "a" : ["b","c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["e"],
    "e" : ["d"]
}

print(graph)
print(find_path(graph, "a", "d"))
print(get_vertices(graph))
print(get_edges(graph))