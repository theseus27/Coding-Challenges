# - Comparison based sorting algorithm
# - Divides dataset into groups of at most 2
# - Moves smaller number to left of pair
# - Compares left most elements of 2 leftmost pairs creating a sorted group of four with the smallest numbers on the left and largest on the right
# - Process is repeated until there is only one store

def merge(data, temp, start, mid, end):
    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:
        if data[i] < data[j]:
            temp[k] = data[i]
            i = i + 1
        else:
            temp[k] = data[j]
            j = j + 1     
        k = k + 1  
    while i < len(data) and i <= mid:
        temp[k] = data[i]
        k = k + 1
        i = i + 1 
    for i in range(start, end + 1):
        data[i] = temp[i]
        
def sort(data):
    low = 0
    high = len(data) -1
    temp = data.copy()
    block_size = 1
    while block_size <= high - low:
        for i in range(low, high, 2*block_size):
            start = i
            mid = i + block_size - 1
            end = min(i + 2*block_size - 1, high)
            merge(data, temp, start, mid, end)
        block_size = block_size * 2

odd_data = [10, 8, 7, 0, 5, 6, 4, 2, 9]
even_data = [10, 1, 9, 2, 5, 8, 6, 3]
repeated_data = [1, 5, 7, 1, 2]
negative_data = [9, -2, 0, 5, -4]
sort(odd_data)
print(odd_data)
sort(even_data)
print(even_data)
sort(repeated_data)
print(repeated_data)
sort(negative_data)
print(negative_data)