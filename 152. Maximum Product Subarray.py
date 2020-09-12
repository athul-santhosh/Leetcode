class Solution:
    def maxProduct(self, nums):
        arr = nums
        n = len(arr)
        if len(arr) < 1:
            return 0
        current_maximum = current_minimum = maximum = arr[0]
        
        for i in range(1,n):
            temp = current_maximum
            #    Handles             0         +             +           -                 -
            current_maximum = max(arr[i], current_maximum * arr[i], current_minimum * arr[i])
            # this helps to find the smallest - ve element
            current_minimum = min(temp * arr[i] , current_minimum * arr[i] , arr[i])
            # maximum helps to catch the maximum product 
            maximum = max(current_maximum , maximum)

        return maximum
athul = Solution()
print(athul.maxProduct([2,4,8,-8]))