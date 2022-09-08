# hashtag -> marking a part of a ship
# period -> marking an empty cell
#Patrol boats(1), Submarines(2), Destroyers(3)
#Return [#1, #2, #3]
    
def solution(B):
    boats = [0 for _ in range(4)]
    rows = len(B)
    columns = len(B[0])
    
    #Read data into array
    board = []
    for line in B:
        row = []
        for i in line:
            if i == '.':
                row.append(0)
            else:
                row.append(1)
        board.append(row)
    
    #Count boats
    for i in range(rows):
        for j in range(columns):
            ship = []
            if board[i][j] == 1:
                board[i][j] = 0
                ship.append([i,j])
                if i < rows-1 and board[i+1][j] == 1:
                    board[i+1][j] = 0
                    ship.append([i+1,j])
                if j < columns-1 and board[i][j+1] == 1:
                    board[i][j+1] = 0
                    ship.append([i,j+1])
                if len(ship) == 2:
                    for m in ship:
                        k = m[0]
                        l = m[1]
                        if k < rows-1 and board[k+1][l] == 1:
                            board[k+1][l] = 0
                            ship.append([k+1,l])
                        if l < columns-1 and board[k][l+1] == 1:
                            board[k][l+1] = 0
                            ship.append([k, l+1])
                        if l > 0 and board[k][l-1] == 1:
                            board[k][l-1] = 0
                            ship.append([k,l-1])
            boats[len(ship)] += 1
    return boats[1:]
                    
                

result = solution([".##.", "#.#."])
result = solution(['##.', '#.#', '.##'])
#Got 3,0,1 expected 0,0,2
print(result)
