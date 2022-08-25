#Input: array of numbers
#Output: proportion of numbers that are positive, negative, or zero

def plusMinus(arr):
    denominator: float = len(arr)
    proportions: float = [0, 0, 0]
    
    for i in arr:
        if i > 0: proportions[0] += 1
        elif i < 0: proportions[1] += 1
        else: proportions[2] += 1
    
    print(round(proportions[0]/denominator, 6))
    print(round(proportions[1]/denominator, 6))
    print(round(proportions[2]/denominator, 6))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
