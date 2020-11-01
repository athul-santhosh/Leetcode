# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr= []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        decimal_number = 0
        n = len(arr)
        for i in range(n):
            if arr[i] == 1:
                decimal_number += 2**(n-i-1)
        return decimal_number