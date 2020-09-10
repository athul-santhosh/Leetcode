class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        if len(words) != len(pattern):
            return False
        d = {}
        
        for i in range(len(words)):
            if pattern[i] not in d and words[i] in d.values():
                return False
            elif pattern[i] not in d:
                d[pattern[i]] = words[i]
            elif pattern[i] in d:
                x = d.get(pattern[i])
                if x == words[i]:
                    continue
                else:
                    return False
        #print(d)
        return True
# Time => O(n)             Space => O(n)

athul = Solution()
x = athul.wordPattern("aaba","dog dog cat dog")
print(x)