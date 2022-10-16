# There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.
# Given an array of n integers, of which represents loads caused by successive processes, return the minimum absolute difference of server loads.

#EXAMPLE
# Input: [1, 2, 3, 4, 5]
# Output: 1
# Explanation:
# We can distribute the processes with loads [1, 2, 4] to the first server and [3, 5] to the second one,
# so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.

#Find a subarray that is closest to 1/2 of total

def solve(loads) -> int:
    half = sum(loads)/2
    loads.sort()
    dp = [loads[0]]
    
    for i in range(1, len(loads)-1):
        for j in range(len(dp)):
            dp.append(dp[j]+i)
            
    closest = sum(loads)
    for i in dp:
        if abs(i-half) < abs(closest-half): closest = i
    
    return int(abs(closest-half)*2)
        
print(solve([1,2,3,4,5]))
print(solve([1,1,1,1,6])) 

#Start by putting the largest and smallest numbers in each array, then going in and putting the number closest to filling the gap, and repeat

# #The first element of s1 and s2 will always be the sum
# l1 = []
# t1 = 0
# l2 = []
# t2 = 0
# loads.sort()

# while len(loads) >= 3:
#     tl += loads[0]
#     l1.append(loads.pop(0))
#     t2 += loads[-1]
#     l2.append(loads.pop())
    
#     if t1 == t2: 
#         continue
    
#     if t1 < t2:
#         closest = 
#         for i in loads:
#             if abs() 
#         t1 += min([abs(loads[i]-(t2-t1)) for i in loads])
#         t1.append()