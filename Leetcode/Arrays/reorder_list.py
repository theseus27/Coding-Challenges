class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:    
        mid = end = head
        
        #Find middle node
        while end and end.next:
            mid = mid.next
            end = end.next.next
        
        if mid == end: return
           
        #Sort second half
        prev = None
        curr = mid
        while curr:
            hold = curr.next
            curr.next = prev
            prev = curr
            curr = hold

        #Merge halves
        start = head
        mid = prev
        while mid.next:
            shold, mhold = start.next, mid.next
            start.next = mid
            start = shold
            mid.next = start
            mid = mhold      
    
            
        