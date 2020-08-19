class Solution:
    def toGoatLatin(self, S: str) -> str:
        # char in vowel
        vowel = "aeiouAEIOU"
        # extract words from S
        s = S.split(" ")
        
        # add ma to vowels and also delete first word from consonants
        for i in range(len(s)):
            # check first letter is a vowel
            add_a = (i+1)* "a" 
            word = s[i]
            if s[i][0] in vowel:
                word = word + str("ma")
                s[i] = word
            else:
                first = s[i][0]                              # if it is consonant omit the first word
                word = word[1:]
                word = word + first + "ma"
                s[i] = word
            s[i] = word + add_a
        # print s as a string
        result = ""
        for i in s:
            result += i + " "
        return result[:-1]


# time O(n)      # O(n) space
        

athul = Solution()
print(athul.toGoatLatin("I speak Goat Latin"))