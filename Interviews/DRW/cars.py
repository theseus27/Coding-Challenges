#H[K] denotes the number of hours required to produce the K-th car
#Make N different cars, 0 to N-1
#2 assembly lines, x and y
#Only one car at a time can be produced on each assembly line and you can't switch lines once starting production
#What is the maximum number of different cars that can be produced in the upcoming month?

#EX: H = [1,1,3]    X = 1   Y = 1   -> 2

def recurse(H, X, Y, fac1, fac2, maximum):
    if len(H) == 0: return maximum
    
    #print("X: " + str(X) + " Y: " + str(Y))
    #print("Max: " + str(maximum) + "\n")
    
    print("H: ", end="")
    print(H)
    print("Fac1: ", end="")
    print(fac1)
    print("Fac2: ", end="")
    print(fac2)
    
    smallest = H[0]
    H.pop(0)

    if smallest > X and smallest > Y:
        #print(max(len(fac1)+len(fac2), maximum))
        return max(len(fac1)+len(fac2), maximum)
    elif smallest > X:
        fac2.append(smallest)
        attempt = recurse(H[0:], X, Y-smallest, fac1, fac2, maximum)
        return max(maximum, attempt)
    elif smallest > Y:
        fac1.append(smallest)
        attempt = recurse(H[0:], X-smallest, Y, fac1, fac2, maximum)
        return max(maximum, attempt)
    else:
        fac1.append(smallest)
        attempt1 = recurse(H[0:], X-smallest, Y, fac1, fac2, maximum)
        fac2.append(smallest)
        attempt2 = recurse(H[0:], X, Y-smallest, fac1, fac2, maximum)
        if attempt1 > attempt2:
            fac2.pop()
            return max(maximum, attempt1-1)
        else:
            fac1.pop()
            return max(maximum, attempt2-1)

def solution(H, X, Y):
    #Cut off ones that absolutely won't fit
    H.sort()
    most = X+Y
    sum = 0
    for i in H:
        if most >= i:
            most -= i
            sum += 1
    H = H[:sum]
    print("\n")
    return recurse(H, X, Y, [], [], 0)

result = solution([5,5,4,6],8,8)
print(result)   #2
# result = solution([6,5,5,4,3],8,9)
# print(result)   #4
# result = solution([7,6,5,4,3,2,1],20,4)
# print(result)   #6
        