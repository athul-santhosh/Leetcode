
def subarraySum(nums, k):
        C_S_M = {0:1}
        count = 0
        cum_sum = 0
        for i in range(len(nums)):
            
            cum_sum += nums[i]
            
            if cum_sum - k in C_S_M:
                count += C_S_M[cum_sum - k]
                
            if cum_sum not in C_S_M:
                C_S_M[cum_sum] = 1
            else:
                C_S_M[cum_sum] += 1
        return count


print(subarraySum([3,4,7,2,-3,1,4,2],7))