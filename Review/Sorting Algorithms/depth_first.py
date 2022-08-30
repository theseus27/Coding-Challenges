graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = set()

def dfs(graph, path, target):
    if path[-1] == target:
        return path
    if not graph[path[-1]]:
        return "No path found."
    
    for i in graph[path[-1]]:
        path.append(i)
        dfs(graph, path, target)

print(dfs(graph, ["A"], "D"))