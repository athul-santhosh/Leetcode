# sorted rotated array
# finding the pivot
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        
        while low <= high:
            
            mid = (low + high ) // 2
            
            if not nums[mid-1] < nums[mid] < nums[mid +1]:
                return nums[mid+1]

            if nums[mid] > nums[high]:
                low = mid +1
            else:
                high = mid - 1
        pivot = nums[mid + 1]
                
        def binary_search(low,high,target):
            while low <= high:
                mid = (low + high)  // 2
                if nums[mid] > target:
                    high = mid - 1 
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] == target:
                    return mid
            return -1
                
            
                
        if target > nums[low]:
            binary_search(low,pivot-1,target)
        elif target < nums[low]:
            binary_search(pivot,high,target)

# this soluion has two passes all toegether O(log n) + O(log n) => O(log n) time O(1). space

def sorted_rotated_search(nums , target):

    low = 0
    high = len(nums) -1

    while low <= high:

        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[low]:                     # very important 

            if nums[low] <= target <= nums[mid]:       # using equals very important else edge cases may show error
                high = mid - 1
            else:
                low = mid + 1
        else:

            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1  
m = [7,9]
for i in m:
    print(sorted_rotated_search([3,1,7,9],i))

# O(log N) time O(1) space
                    