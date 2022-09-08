#When cars arrive at an intersection, two queues can build up, one for each street
#If in the previous second, no cars passed through, then the first car in the queue for 1st Ave goes first
#If in the previous second, a car passed through the intersection on First Ave, then the first car for 1st Ave goes first
#If in prev second, a car passed through intersection on Main Street, then first car for Main Street goes first

#Passing through the intersection takes 1 second
#For each car, find the time when they will pass through

#getResult(int arrival[n], int street[n]) -> int[n]
#Arrival is time in seconds when the ith car arrives. If arrival[i] = arrival[j] and i < j then car i arrives before car j
#Street is the street the car is passing on: 0 for main, 1 for 1st Ave
#n between (1, 10^5)
#arrival[i] between (0, 10^9) for [0, n-1]
#arrival[i] <= arrival[i+1] for i in [0, n-2]

#EXAMPLE
4,0,0,1,4,4,0,1,1,0 -> 2,0,1,4
4 arrival times: 0, 0, 1, 4
4 streets: 0, 1, 1, 0

import math
import os
import random
import re
import sys




def getResult(arrival, street):
    results = [0 for i in range(len(arrival))]
    last = 0
    
    for i in range(1, len(arrival)-2):
        if arrival[i] == arrival[i+1]:
            if arrival[i]-arrival[i-1] > 1:
                last = 0
            if (last == street[i]):
                arrival[i], street[i], arrival[i+1], street[i+1] =  arrival[i+1], street[i+1], arrival[i], street[i]
     
    time = 0
    for i in range(len(arrival)):
        if arrival[i] == time:
            time += 1
            results[i] = time
        elif arrival[i] > time:
            time = arrival[i]
            results[i] = time
        else:
            results[i] = results[i-1]
            
    return results
            
        
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arrival_count = int(input().strip())

    arrival = []

    for _ in range(arrival_count):
        arrival_item = int(input().strip())
        arrival.append(arrival_item)

    street_count = int(input().strip())

    street = []

    for _ in range(street_count):
        street_item = int(input().strip())
        street.append(street_item)

    result = getResult(arrival, street)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
