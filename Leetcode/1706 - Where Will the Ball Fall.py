# MEDIUM
# Runtime: 182 ms (Beat 98.29%)
# Memory: 14.2 MB (Beat 98.34%)

""" QUESTION
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.
"""

from typing import List

def findBall(self, grid: List[List[int]]) -> List[int]:
    if (len(grid) == 0 or len(grid[0]) == 0):
        return []

    cols = len(grid[0])
    rows = len(grid)

    result = []

    for i in range(0, cols):
        r = 0
        c = i
        while r < rows and c != -1:
            board = grid[r][c]

            if board == -1:
                if c == 0 or  grid[r][c-1] == 1:
                    c = -1
                else:
                    c -= 1
            else:
                if c == cols-1 or grid[r][c+1] == -1:
                    c = -1
                else:
                    c += 1
            r += 1
        result.append(c)
    
    return result