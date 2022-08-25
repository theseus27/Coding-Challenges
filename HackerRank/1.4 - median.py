#Input: Array of numbers, odd number of elements
#Output: Median element

def findMedian(arr):
    sortedArr = sorted(arr)
    return sortedArr[len(arr) // 2]