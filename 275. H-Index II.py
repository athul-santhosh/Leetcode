class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        """
        
mid     # 0 1 2 3 4  5   6   7 
        
        # 1 3 8 9 16 17  18 25 
        
n- mid  # 8 7 6 5 4   3  2   1




        """
        if not citations: return 0
        n = len(citations)
        low = 0
        high = n - 1
        max_cit = 0
        while low <= high:
            mid = (low + high) // 2
            if citations[mid] == n - mid:
                return n - mid
            if citations[mid] > n - mid:
                max_cit = max(max_cit, n - mid)
                high = mid - 1
            else:
                low = mid + 1
            
        return max_cit
        
        
        
        
        
        
        

                

            
        
