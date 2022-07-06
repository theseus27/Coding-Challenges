from traceback import print_exception
import draft1 as try1
import draft2 as try2

testArray = [0, 0, 0]

for i in range(1, 10):
    testArray[0] = i
    for j in range(1, 10):
        testArray[1] = j
        for k in range(1, 10):
            testArray[2] = k
            for n in range(1, 30):
                try:
                    sol1 = try1.solution(testArray, n)
                except:
                    print("Exception on sol1: " + str(testArray) + ", " + n)
                    
                try:
                    sol2 = try2.solution(testArray, n)
                except:
                    print("Exception on sol2: " + str(testArray) + ", " + n)
                    
                if (sol1 != sol2):
                    print("Found a difference: " + str(sol1) + str(sol2))

