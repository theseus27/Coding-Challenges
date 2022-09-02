class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:   
        
        #Make list of nodes
        listlength = 1
        positions = [head]
        start = head
        while(start.next != None):
            positions.append(start.next)
            start = start.next
            listlength += 1
        if listlength < 2:  return
        
        head.next = positions[-1]    
        
        #Create pointers
        high = listlength // 2 + 1
        low = high-1 if listlength%2 == 1 else high-2
        positions[high-1].next = None
        
        #Odd
        if listlength%2 == 1:
            positions[high].next = positions[low]
            low -= 1
            high += 1
        
        while (low > 0):
            print(low)
            print(high)
            print("\n")
            positions[low].next = positions[high-1]
            positions[high].next = positions[low]
            low -= 1
            high += 1