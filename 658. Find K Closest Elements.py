class Solution:
    def findClosestElements(self, arr,k, x):
        low = 0
        high = len(arr)-k
        
        while low < high:
            mid = low+high //2
            if x-arr[mid] > arr[mid+k] - x:
                low = mid + 1
            else:
                high = mid
        return arr[low:low+k]


ll = Solution()
print(ll.findClosestElements([1,1,1,10,10,10],1,9))
        