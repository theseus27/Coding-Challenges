# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:   
        if head.next == None: return
        if head.next.next == None: return
        
        #Make list of nodes
        listlength = 1
        positions = [head]
        start = head
        while(start.next != None):
            positions.append(start.next)
            start = start.next
            listlength += 1
            
        #Create pointers
        lowmid = listlength // 2
        highmid = lowmid + 1            
        head.next = positions[-1]

        #EVEN
        if (listlength % 2 == 0):
            positions[lowmid].next = None
            lowmid -= 1
            while (lowmid > 0):
                positions[lowmid].next = positions[highmid-1]
                positions[highmid].next = positions[lowmid]
                lowmid -= 1
                highmid += 1
        
        #ODD
        else:
            positions[lowmid].next = None
            positions[highmid].next = positions[lowmid]
            lowmid -= 1
            highmid += 1
            while (lowmid > 0):
                positions[highmid].next = positions[lowmid]
                positions[lowmid].next = positions[highmid-1]
                lowmid -= 1
                highmid += 1