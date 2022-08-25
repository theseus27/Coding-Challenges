#Input: array of 5 elements
#Output: Minimum and maximum sum of 4/5 elements

def miniMaxSum(arr):
    #Sum all elements, while finding largest and smallest elemenet
    arrSum = 0; minimum = 10**9; maximum = 0;
    for i in arr:
        arrSum += i
        if i > maximum: maximum = i
        if i < minimum: minimum = i
    
    print(str(arrSum-maximum) + " " + str(arrSum-minimum))
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
