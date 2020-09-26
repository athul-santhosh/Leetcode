#longest substring without repeating characetr

 class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        low = 0
        high = 0
        maxlen = 0
        seen = set()
        while high <len(s):

            if s[high] not in seen:   
                seen.add(s[high])
                high += 1
                
            elif s[high] in seen:                     # the most important part
                seen.remove(s[low])
                low += 1
            
            maxlen = max(maxlen,high - low)
        return maxlen

