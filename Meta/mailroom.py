"""
Givens 
    N days
    V, an array of len(N) with values of packages being delivered
    C, cost to check mailroom
    S, probability that all packages will be stolen
Find maximum profit

Constraints
    N in [1, 4000]
    V[i] in [0, 1000]
    C in [1, 1000]
    S in [0, 1]
Example 1
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 5
    S = 0.0
    Expects 25
Example 2
    N = 5
    V = [10, 2, 8, 6, 4]
    C = 3
    S = .15
"""

# Ideas
#   For each day, calculate the average probability value then add them up

def maximize_profit_draft_1(N, V, C, S):
    if N == 0:
        return 0.0
    
    checked = [0]
    no_check = [0]
    in_room = [0]

    checked[0] = V[0] - C
    no_check[0] = V[0] * (1.0 - S)
    if checked[0] > no_check[0]:
        in_room.append(0)
    else:
        in_room.append(V[0])


    for i in range(1, N):
        if checked[i-1] > no_check[i-1]:
            val = V[i]
        else:
            val = in_room[i-1] + V[i]
        
        c_val = val - C
        nc_val = val * (1.0 - S)

        checked.append(c_val)
        no_check.append(nc_val)
        in_room.append(V[i])
 
    return max(checked[-1], no_check[-1])

def maximize_profit_draft_2(N, V, C, S):
    if N == 0.0:
        return 0
    
# Calculate when mailroom should be checked
    value = 0
    checks = [0 for i in range(N)]

    for i in range(N):
        value += V[i]

        if i != N-1:
            check = value - C
            nocheck = value*(1-S)
            
            if check >= nocheck:
                checks[i] = 1
                value = 0
        else:
            if value >= C:
                checks[i] = 1
    print(checks)
# Based on the checks, do the probability math
    profit = 0
    value = 0

    for i in range(N):
        value += V[i]
        if checks[i] == 1:
            profit += value-C
            value = 0
        else:
            value = round(value*(1-S), 7)
    
    return profit


def recurse(day, profit, value):


def maximize_profit(N, V, C, S):
    pass

Day 1: 10
Decision: Don't check
85% chance profit=0, value=10
15% chance profit=0, value=0

Day 2: 2
Decision: Don't check
85*85% chance profit=0, value=12
85*15% chance profit=0, value=10

15*85% chance profit=0, value=2
15*15 chance profit=0, value=0


Day 3: 8
Decision: Check
add all the profits



print(maximize_profit(5, [10, 2, 8, 6, 4], 5, 0.0)) # 25.0
print(maximize_profit(5, [10, 2, 8, 6, 4], 3, .15)) # 20.10825000