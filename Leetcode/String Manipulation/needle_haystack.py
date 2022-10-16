#Short
return haystack.index(needle) if needle in haystack else -1

#Longer
for i in range(len(haystack)-len(needle)+1):
    found = True
    j = 0
    while found and j < len(needle):
        if haystack[i+j] != needle[j]: found = False
        j += 1
    if found: return i

return -1