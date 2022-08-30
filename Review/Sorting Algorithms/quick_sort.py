#Pick an element (pivot) the leftmost or rightmost
#Reorder array so all elements smaller than pivot go before, all greater after
#Recursively apply to subarray of elements w/ smaller values than pivot

def switch(data, x, y):
    hold = data[x]
    data[x] = data[y]
    data[y] = hold

def find_pivot(data, start, end):
    pivot = data[end]
    curr = start

    for i in range(start, end):
        if data[i] < pivot:
            switch(data, i, curr)
            curr += 1
    
    switch(data, end, curr)
    
    return curr

def quicksort(data, start, end):
    if start >= end:
        return
    
    pivot = find_pivot(data, start, end)
    
    quicksort(data, start, pivot - 1)
    quicksort(data, pivot + 1, end)


odd_data = [10, 8, 7, 0, 5, 6, 4, 2, 9]
even_data = [10, 1, 9, 2, 5, 8, 6, 3]
repeated_data = [1, 5, 7, 1, 2]
negative_data = [9, -2, 0, 5, -4]
quicksort(odd_data, 0, len(odd_data)-1)
print(odd_data)
quicksort(even_data, 0, len(even_data)-1)
print(even_data)
quicksort(repeated_data, 0, len(repeated_data)-1)
print(repeated_data)
quicksort(negative_data, 0, len(negative_data)-1)
print(negative_data)