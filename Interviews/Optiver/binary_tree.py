def main():
    #Read in tree
    tree_string = "(A,B) (A,C) (B,D) (D,E) (C,F) (E,G)"          #str(input())
    tree_array = tree_string.split(" ")
    for idx in range(len(tree_array)):
        tree_array[idx] = tree_array[idx].strip("(").strip(")")
    
    nodes = []
    parent_nodes = []
    
    #Process each node as a tuple
    for i in tree_array:
        data = i.split(",")
        if data[0] not in parent_nodes:
            nodes.append((data[0], data[1], ""))
            parent_nodes.append(data[0])
        else:
            for idx in range(len(nodes)):
                if nodes[idx][0] == i[0]:
                    nodes[idx] = (data[0], data[1], nodes[idx][1])
                    break
        
    print(nodes)

main()