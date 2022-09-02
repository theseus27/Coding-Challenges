        positions[listlength-1], positions[lowmid] = positions[lowmid], positions[listlength-1]
        positions[listlength-2].next = lowmid
        positions[lowmid].next = positions[highmid]
        
        for i in range(lowmid, 0, -1):
            positions[highmid].next = positions[lowmid]
            positions[lowmid] = positions[list]
        
        
        for i in range(0, listlength//2):
            positions[listlength-i] = positions[i].next
            positions[i].next = positions[listlength-i]
        
        print(positions)
        
#"Flip the backhalf"
#012345 -> 012543