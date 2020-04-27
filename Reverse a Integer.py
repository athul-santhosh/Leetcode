class Solution:
    def reverse(self, x: int) -> int:          
        rev = 0                                   #setting reverse to 0
        temp = x                                  #storing value of x to temp  
        if x < 0:
            x = abs(x)                        #converting x to postive if it
        while x != 0:                         #is negative 
            rev = rev*10 + x % 10             # rev*10 cancels out 0s and
            x = x//10                         # aswell as increments 10s
        if -2**31 < rev < 2**31 -1:           # checking the range of revv wehter is in the int range
            if temp > 0:                          
                return rev                         
            else:
                return -rev
        else:
            return 0
                                                
        





