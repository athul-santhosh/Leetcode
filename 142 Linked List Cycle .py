# Detecting a Cycle in Linked List 
# Using the floyds hare and tortoise algorithm 

    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head                                             #  set slow and fast to head
        fast = head
        while fast and fast.next:                               # Traverse till the end if it exists,
            slow = slow.next                                    # one pointer will move twice fast as the pointer , if there
                                                                # is a loop they will definetly meet
            fast = fast.next.next 
            if slow == fast:                                    
                break 


        if fast == None or fast.next == None:                   # if there is no loop means fast or fast.next would be None
            return None                                         # this indicates there is no loop
        Striker = head                                          # here we use striker which is set to head ,and either fast  
        while striker != fast:                                  # or slow pointer to reach to the begining of th loop 
            striker = striker.next                              #
            fast = fast.next                                    #
        return fast                                             # we can return striker or fast as both would be pointing to
                                                                # the beginning of the loop

                                                                # A detailed explanntion is provided on the CTCI by Gale L M
`