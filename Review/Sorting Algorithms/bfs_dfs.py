def bfs(graph, root, target):
    visited = {root}
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node == target:
            print("Found " + str(node))
            return
        print("Check " + str(node))
        
        for i in graph[node]:
            if i not in visited:
                queue.append(i)
                visited.add(i)         
    print("Failed to find " + str(target))

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def main():
    graph = {
        '5' : ['3','7'],
        '3' : ['2', '4'],
        '7' : ['8'],
        '2' : [],
        '4' : ['8'],
        '8' : []
    }
    
    bfs(graph, "5", "4")
    dfs(set(), graph, '5')
    
if __name__ == "__main__":
    main()