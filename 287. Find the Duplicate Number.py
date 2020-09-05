class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """     0 1 2 3 4 
        Input: [1,3,4,2,2]
         n+1   
        !         !
        1 -> 3 -> 2 -> 4 -> 2 
                  !----------!
                  
        phase 1 
        
        slow  1 3 2 4 2 
        fast  1 2 2
        
        phase 2
        
        Output: 2
        
        """
        # phase 1
        slow = nums[0]
        fast = nums[nums[0]]
        
        while fast != slow:
            slow = nums[slow] # 1 step
            fast = nums[nums[fast]]  # 2 step 
        slow = 0
        # phase 2
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow 