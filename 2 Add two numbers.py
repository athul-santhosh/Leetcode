    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value = 0
        l3 = headl3 = ListNode()
        while l1 or l2 or value:           #O(max(len(l1),len(l2)))
            if l1:
                value += l1.val
                l1 = l1.next
            
            if l2:
                value += l2.val
                l2 = l2.next
                
            l3.val = value % 10
            value = value // 10
            if l1 or l2 or value:
                
                l3.next = ListNode()               
                l3 = l3.next
        return headl3
                