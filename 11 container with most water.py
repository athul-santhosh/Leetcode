    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) -1 
        max_area = 0
        while low <= high:
            dist = high - low
            current_area = dist * min(height[low],height[high])
            #print(current_area)
            max_area = max(max_area,current_area)
            if height[low] > height[high]:
                high = high -1
            else:
                low = low + 1
        return max_area