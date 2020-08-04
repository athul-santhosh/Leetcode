class Solution:
    def romanToInt(self, s):
        RI = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num = 0
        prev = 0
        #XLIX
        for i in s:
            cur = RI[i]
            if cur > prev:
                num += cur - 2*prev
            else:
                num += cur
            prev = cur

            
        return num
p = Solution()
print(p.romanToInt("XXXXXXX"))