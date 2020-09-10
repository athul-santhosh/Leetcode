class Solution:
    def fourSum(self,nums,target):
        arr = nums
        if len(arr) < 4:
            return []
        arr.sort()
        n = len(arr)
        result = []
        for i in range(n):
            for j in range(i+1,n):
                r = target - (arr[i] + arr[j])
                low = j+1
                high = n - 1
                while low < high:
                    if r > arr[i]+ arr[j]:
                        low += 1
                    elif r < arr[i] + arr[j]:
                        high -= 1
                    else:
                        #if arr[i] != arr[j] and  arr[low] != arr[high] and arr[i] != arr[low]:
                        print("hi")
                        break
                        #result.append([arr[i],arr[j],arr[high],arr[low]])
        return result

athul = Solution()
print(athul.fourSum([1, 0, -1, 0, -2, 2],0))