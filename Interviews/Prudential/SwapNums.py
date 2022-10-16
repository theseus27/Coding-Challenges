import sys

def swap(line):
    spl = line.split(':')
    nums = spl[0].strip().split(' ')
    swaps = spl[1].strip().split(',')
  
    for i in swaps:
        pos = i.split('-')
        p1 = int(pos[0])
        p2 = int(pos[1])
        nums[p1], nums[p2] = nums[p2], nums[p1]
    
    swapped = ""
    for j in nums:
        swapped += str(j)
        swapped += " "
    return swapped[:-1]
        
    

for line in sys.stdin:
    print(swap(line), end="")
