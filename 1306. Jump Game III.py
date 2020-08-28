class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        nums = arr
        stack = []
        stack.append(start)
        seen = [0] * len(nums) 
        while len(stack) != 0:
            cur_index = stack.pop() 
            left = cur_index - nums[cur_index]
            right = cur_index + nums[cur_index]

            if left >= 0 and left < len(nums) and seen[left] == 0:
                stack.append(left) 
                seen[left] = 1
                if nums[left] == 0:
                    return True
            if right >= 0 and right < len(nums) and seen[right] == 0:
                stack.append(right)
                seen[right] = 1
                if nums[right] == 0:
                    return True
        return False