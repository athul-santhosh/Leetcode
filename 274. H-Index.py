class Solution:
    def hIndex(self, citations: List[int]) -> int:

        
        if not citations: return 0
        
        index = len(citations)
        
        count = 0
        
        citations.sort()
        
        while index > 0:
            
            if index <= citations[count]:
                return index
            
            else:
                count += 1
                index -= 1
        return 0
                

            
        
