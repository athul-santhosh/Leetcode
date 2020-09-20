class Solution:
    def checkRecord(self, s: str) -> bool:
        reward = True
        absent = s.count("A")
        if "LLL" in s:
            reward = False
        if absent > 1:
            reward = False
        return reward
athul=Solution()
print(athul.checkRecord("PLALPPL"))      
print(athul.checkRecord("PLALPPLLLLL")) 
print(athul.checkRecord("AAA"))    