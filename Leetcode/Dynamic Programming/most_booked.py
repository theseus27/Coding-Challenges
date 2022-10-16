#Given a hotel which has 10 floors [0-9] and each floor has 26 rooms [A-Z]. You are given a sequence of rooms, where + suggests room is booked, - room is freed. You have to find which room is booked maximum number of times.
# You may assume that the list describe a correct sequence of bookings in chronological order; that is, only free rooms can be booked and only booked rooms can be freed. All rooms are initially free. Note that this does not mean that all rooms have to be free at the end. In the case that 2 rooms have been booked the same number of times, return the lexographically smaller room.
# You may assume:
#   N (length of input) is an integer within the range [1, 600]
#   each element of array A is a string consisting of three characters: "+" or 
#       "-"; a digit "0"-"9"; and uppercase English letter "A" - "Z"
#   the sequence is correct. That is every booked room was previously free and 
#       every freed room was previously booked.

#EXAMPLE
# Input: ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
# Output: "1A"
# Explanation: 1A as it has been booked 2 times.

#A-Z --> 0-25 = -65

def solve(input):
    rooms = [[0 for _ in range(26)] for _ in range(10)]
    
    #Put bookings in table
    for i in input:
        if i[0] == '-': continue
        rooms[int(i[1])][ord(i[2])-65] += 1
     
    #Find room with most bookings
    most = 0
    room = ""
    for i in range(10):
        for j in range(26):
            if rooms[i][j] > most:
                most = rooms[i][j]
                room = str(i) + str(chr(j+65))
    return room

print(solve(["+1B", "+3E", "-1B", "+1B", "+1A", "-3E"]))