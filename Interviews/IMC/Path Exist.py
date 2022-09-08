#Input: c, x1, y1, x2, y2
#Move: (x,y) -> (x+y, y)
#      (x,y) -> (x, x+y)
#      (x,y) -> (x+c, y+c)

#All coordinates between 1 and 1000
#C between 1 and 15
#All movement is in a positive direction

squares = [i*i for i in range(32)]
               
def find_path(c, x1, y1, x2, y2) -> bool:
    #print("(" + str(x1) + "," + str(y1) + ") (" + str(x2) + "," + str(y2) + ")")
    if (x1 == x2 and y1 == y2):
        return True
    if (x1 > x2 or y1 > y2):
        return False
    
    return (find_path(c, x1+y1, y1, x2, y2) and not x1+y1+y1 in squares) or (find_path(c, x1, x1+y1, x2, y2) and not x1+x1+y1 in squares) or (find_path(c, x1+c, y1+c, x2, y2) and not x1+y1+c+c in squares)

def canReach(c, x1, y1, x2, y2) -> str:
    if find_path(c, x1, y1, x2, y2):
        return "Yes"
    else:
        return "No"

result = canReach(1,1,4,7,6)
result = canReach(1, 1, 3, 4, 4)
result = canReach(1, 1, 1, 5, 4)
print(result)


# import math
# import os
# import random
# import re
# import sys
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     c = int(input().strip())
#     x1 = int(input().strip())
#     y1 = int(input().strip())
#     x2 = int(input().strip())
#     y2 = int(input().strip())
#     result = canReach(c, x1, y1, x2, y2)
#     fptr.write(result + '\n')
#     fptr.close()

# def get_obstacle(constant, changing, c):
#     obstacle = False
#     if c==0:
#         for i in range(constant, constant+changing):
#             if i+constant in squares: obstacle = True
#     else:
#         for i in range(1, c+1):
#             if constant+changing+2*c in squares: obstacle = True
#     return obstacle