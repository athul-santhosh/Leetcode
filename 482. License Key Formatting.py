class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        string = []
        for i in S:
            if i == "-":
                continue
            elif i.islower():
                string.append(i.upper())
            else:
                string.append(i)
        n = len(string)
        for i in range(n,0,-K):
            string.insert(i,"-")
        if len(string) != 0:        
            string.pop()
        return "".join(string)

#O(n) time     O(n) space
athul = Solution()
print(athul.licenseKeyFormatting("hfsa-dfhjshf-HKH-fdhf34738-JKJjfhe-8",5))