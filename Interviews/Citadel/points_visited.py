def getMostVisited(n, sprints):   
    #Base case: 1 number
    if len(sprints) == 1:
        return sprints[0]
    
    #Track how many times each goal is visited
    #Put a buffer for 0
    visits = [0 for _ in range(n+1)]
    for i in range(1, len(sprints)):
        earlier = min(sprints[i-1], sprints[i])
        later = max(sprints[i-1], sprints[i])
        
        visits[earlier] += 1
        if (later != n):
            visits[later+1] -= 1
            
    #Find most visited point
    most = 1
    prev = 0
    for i in range(1, len(visits)):
        visits[i] += prev
        prev = visits[i]
        #Check against most
        if visits[i] > visits[most]:
            most = i
    
    return most
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sprints_count = int(input().strip())

    sprints = []

    for _ in range(sprints_count):
        sprints_item = int(input().strip())
        sprints.append(sprints_item)

    result = getMostVisited(n, sprints)

    fptr.write(str(result) + '\n')

    fptr.close()
