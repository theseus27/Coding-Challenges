#Dynamic Programming
def coinChange(coins, amount):
    
    options = [-1]*(amount+1)
    
    options[0] = 0
    
    #Calculate for each smaller value building up to amount
    for i in range(1, amount+1):
        fewest = 2**33
        #Try coins, and can get minimum coins found with result from array
        for coin in coins:
            if i - coin >= 0 and options[i - coin] != -1:
                #Set that amount's min to 1 + the result's min
                fewest = min(fewest, 1 + options[i - coin])
        
        options[i] = fewest if fewest != 2**33 else -1
    
    #Return the min of amount
    return options[amount]

print(coinChange([2],5))  
 

#     fewest = 2^33
        
#     for i in coins:
#         goal = amount
#         tries = 0
#         curr = 0
#         while(goal > 0 and tries < len(coins)):
#             tries = 0
#             for i in coins:
#                 if (goal - i) > 0:
#                     goal -= i
#                     curr += 0
#                     continue
#                 else:
#                     tries += 1
#         if goal == 0 and curr < fewest:
#             curr = fewest
#         else:
#             print(curr)
    
#     if fewest < 2^33: return fewest
#     return -1
        
# print(coinChange([1, 2, 5], 11))