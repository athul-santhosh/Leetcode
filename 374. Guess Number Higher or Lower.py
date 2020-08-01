# guess the number

# guess function return s the following for us

# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
    
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            mid = (low + high ) // 2
            
            if guess(mid) == -1:
                high = mid - 1
            elif guess(mid) == 1:
                low = mid +1
            else:
                return mid