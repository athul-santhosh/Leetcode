	def deleteDuplicates(self, head: ListNode) -> ListNode:
		#this solution works even if the list is sorted or unsorted but uses an 
		#additional memory space for dictionary
        
        cur = head
        map = {}
        prev =  head
        while cur:
            if cur.val in map:
                prev.next = cur.next
                cur = None
            else:
                map[cur.val] = 1
                prev = cur
            cur = prev.next
        return head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
    	# this solution only works for sorted list i.e the duplicate elements should
    	# adjacnent to each other , it does not uses any auxillary memory

        cur = head
        if cur is None:
        	return None
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
  