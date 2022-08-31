
def ugly(min, max):
    in_range = 0
    
    possible = [1, 3, 5]
    for i in possible:
        if i*3 not in possible and i*3 < max: possible.append(i*3)
        if i*5 not in possible and i*5 < max: possible.append(i*5)
        
    for i in reversed(possible):
        if i > min: in_range += 1
    
    return in_range

print(ugly(300000, 400000))