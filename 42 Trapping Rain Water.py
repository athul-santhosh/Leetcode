    def trap(self, height: List[int]) -> int:
        LR = []
        RL = []
        maxLr = 0
        maxrl = 0
        
        low = 0
        high = len(height) - 1
        
        while low <= high:                                 # determing max lenght from left to right 
            if height[low] > maxLr:
                maxLr = height[low]
            LR.append(maxLr)
            low = low + 1
        #print(LR)
        low = 0
        high = len(height) - 1
        
        while high >= low:                                # determing max length from right to left
            if height[high] > maxrl:
                maxrl = height[high]
            RL.append(maxrl)
            high = high - 1
        RL.reverse()                                      # reversing  RL  as it will be the left right order
        #print(RL)
        min_height = []
        result = []
        for i in range(len(height)):                      # updating min_height with minimum of LR  and RL
            min_height.append(min(LR[i],RL[i]))
        for i in range(len(height)):                      # updating result with differnce of min_heigh and the origanl 
            result.append(abs(min_height[i] - height[i])) # list 
        return(sum(result))                               # O(len(height))   Time       O(len(height)) space

   

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        leftMax = height[0]
        rightMax = height[n - 1]
        left = 0
        right = n - 1
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    res += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    res += rightMax - height[right]
                right -= 1
        return res       

























