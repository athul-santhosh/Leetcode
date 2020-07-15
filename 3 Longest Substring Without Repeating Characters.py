class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        # naive  , more readable
        m = []
        def is_unique(s):
            if len(s) == len(set(s)):
                m.append(s)
        
        n = len(s)
        sub = []
        for i in range(1,n):                    #. O(n*n) time               # O(n) space
            for j in range(n-i +1 ): 
                sub.append(s[j:j+i])
        for i in sub:                              # O(n) time
            is_unique(i)                         
        return(len(m[-1]))
                                                # total O(n*n*n) = O(n*n)

        #1 optimised. code reduced

        m = []                                        
        n = len(s)
        for i in range(1,n):                    # O(n*n)      #o(n) space
            for j in range(n-i +1 ):
                if len(s[j:j+i]) == len(set(s[j:j+i])):      
                    m.append(s[j:j+i])
        return(len(m[-1]))

        #2 optimised solution                 Sliding Window Approach
 
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max_len = 0
        i = 0
        while i < len(s):                  # O(n)    time        O(n)  space
            count = 0
            word_count = {}
            for j in range(i,len(s)):
                if s[j] not in word_count:
                    word_count[s[j]] = 1
                    count += 1
                else:
                    break
            i += 1
            max_len = max(max_len,count)
        return max_len
    
    # further optimised solution using sliding window technique
    
 def longest_substring_unique(s):

    if len(s) == 0:
        return 0

    last_index_pos = {}

    max_len = start = 0

    for index in range(len(s)):
        #and start <= last_index_pos[s[index]]
        if s[index] in last_index_pos and start <= last_index_pos[s[index]]:
            start = last_index_pos[s[index]] + 1
            print("Index ",index,"start",start)
        else:
            max_len = max(max_len,index - start + 1)
        print(last_index_pos)

        last_index_pos[s[index]] = index
        print("\n")
    print(last_index_pos)
    return max_len


print(longest_substring_unique("baaabcdbd"))
print("\n")

