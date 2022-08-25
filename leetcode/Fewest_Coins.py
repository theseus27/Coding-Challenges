def coinChange(coins, amount):
    fewest = 2^33
        
    for i in coins:
        goal = amount
        tries = 0
        curr = 0
        while(goal > 0 and tries < len(coins)):
            tries = 0
            for i in coins:
                if (goal - i) > 0:
                    goal -= i
                    curr += 0
                    continue
                else:
                    tries += 1
        if goal == 0 and curr < fewest:
            curr = fewest
        else:
            print(curr)
    
    if fewest < 2^33: return fewest
    return -1
        
print(coinChange([1, 2, 5], 11))