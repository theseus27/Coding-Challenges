#Given two integer arrayss val and wt, and an integer W which represents knapsack capacity, find the maximum value subset of val such that sum of the weights is less than or equal to W.

def solve(val, wt, W):
    dp = [[0,0]]
    for i in range(len(val)):
        for j in range(len(dp)):
            if wt[i] + dp[j][1] <= W:
                dp.append([val[i]+dp[j][0], wt[i]+dp[j][1]])
    
    vals = [dp[i][0] for i in range(len(dp))]
    return max(vals)
    
print(solve([60,100,120],[10,20,30],50))
print(solve([10,15,5,8,7],[3,5,15,10,10],20))    