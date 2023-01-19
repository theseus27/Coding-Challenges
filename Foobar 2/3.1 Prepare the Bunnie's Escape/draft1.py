def solution(map):
    r = len(map)
    c = len(map[0])

    dp = [[0 for i in range(c)] for j in range(r)]
    wall = [[False for i in range(c)] for j in range(r)]

    dp[r-1][c-1] = 1

    #Right Border
    for i in range(r-2, -1, -1):
        if dp[i+1][c-1] == -1:
            dp[i][c-1] = -1
        elif wall[i+1][c-1] == True and map[i][c-1] == 1:
            dp[i][c-1] = -1

        elif map[i][c-1] == 0:
            dp[i][c-1] = dp[i+1][c-1] + 1
            wall[i][c-1] = wall[i+1][c-1]

        else:
            dp[i][c-1] = dp[i+1][c-1] + 1
            wall[i][c-1] = True

    #Bottom Border
    for i in range(c-2, -1, -1):
        if dp[r-1][i+1] == -1:
            dp[r-1][i] = -1
        elif wall[r-1][i+1] == True and map[r-1][i] == 1:
            dp[r-1][i] = -1
        
        elif map[r-1][i] == 0:
            dp[r-1][i] = dp[r-1][i+1] + 1
            wall[r-1][i] = wall[r-1][i+1]
        
        else:
            dp[r-1][i] = dp[r-1][i+1] + 1
            wall[r-1][i] = True

    print(dp)
    print(wall)

    #Build a list of the fastest routes from 0,0 to i,j using a wall and not using a wall

    #Or do it as many times as there are walls, removing a different wall each time

    #Fastest way to get from A to B:
    # A: 0,0 (i, j)
    # B: 3, 3

    # #Do bottom and right walls first
    # for 
    
    # For each square, store a value 'shortest path' and 'wall used'


solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) 
#Should be 7
"""
0 1 1 0
0 0 0 1
1 1 0 0
1 1 1 0
"""