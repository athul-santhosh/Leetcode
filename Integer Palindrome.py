class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        p = 0
        if x<0:
            return False
        while x != 0:
            p =p*10 + x%10
            x=x//10
        if p == temp:
            return True
        else:                             
            return False                 
        #return(x==int(str(x)[::-1]))
         






