def minimumBribes(q):
    order = [i for i in range(1, len(q)+1)]
    bribes = 0
    
    while q:
        bribe = order.index(q[0])
        if bribe > 2:
            print("Too chaotic")
            return
        bribes += bribe
        order.remove(q[0])
        q.pop(0)
    print(bribes)

#Doesn't work bc doesn't take into account previous bribes shifting places
"""
def minimumBribes(q):
    bribes = 0
    order = [i for i in range(1,len(q)+1)]
    for i in q:
        if order.index(i) <= 2: bribes += order.index(i)
        else:
            print("Too chaotic")
            return
        order.remove(i)
    print(bribes)
"""
