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