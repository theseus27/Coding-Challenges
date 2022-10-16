#On a bus, infinite seats from 1 to infinity. n people in a queue waiting to be seated. The ith person wants the seat arr[i].
#If the seat required by the person in the front of the queue is empty, they get the seat
#If the seat required by front person is taken, their required seat is incremented by 1, and they are put on the end of the queue

#Given array a, find the final seat number for each person
#Should return an array same length as given

def getSeatsAllocation(arr):
    queue = [(idx, val) for idx, val in enumerate(arr)]
    seats = [0 for _ in range(len(arr))]
    finalSeats = [0 for _ in range(len(arr))]
    
    while len(queue) > 0:
        p = queue.pop(0)
        if seats[p[1]-1] == 0:
            seats[p[1]-1] = 1
            finalSeats[p[0]] = p[1]
        else:
            queue.append((p[0], p[1]+1))
            
    return finalSeats

print(getSeatsAllocation([1,3,3,2,2]))
    
    
"""
STDIN         FUNCTION
-----         --------
5       →     arr[] size n = 5
1       →     arr = [1, 3, 3, 2, 2]
3
3
2
2

STDOUT
-----
1 
3 
4 
2 
5

EXPLANATION
-----
Original index  Seat choice     Seat assigned
[1, 2, 3, 4, 5] [1, 3, 3, 2, 2] [_, _, _, _, _] assign seat 1
[2, 3, 4, 5]    [3, 3, 2, 2]    [1, _, _, _, _] assign seat 3
[3, 4, 5]       [3, 2, 2]       [1, 3, _, _, _] seat 3 is occupied
[4, 5, 3]       [2, 2, 4]       [1, 3, _, _, _] assign seat 2
[5, 3]          [2, 4]          [1, 3, _, 2, _] seat 2 is occupied
[3, 5]          [4, 3]          [1, 3, _, 2, _] assign seat 4
[5]             [3]             [1, 3, 4, 2, _] seat 3 is occupied
[5]             [4]             [1, 3, 4, 2, _] seat 4 is occupied
[5]             [5]             [1, 3, 4, 2, _] assign seat 5
[]              []              [1, 3, 4, 2, 5] done
"""
