s  = "abcefghijk"
vowel = "aeiou"
s = list(s)
stack_index = []
stack_char = []
        
for i in range(len(s)):
    if s[i] in vowel:
        stack_index.append(i)
        stack_char.append(s[i])
j = len(stack_char)-1
for i in stack_index:
    s[i] = stack_char[j]
    j -= 1
s = ("").join(s)
return(s)

def reverseVowels(self, s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U'}
    n = len(s)
    res = list(s)
        
    i,j = 0, n-1
    while (i <= j):
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            res[i] = s[j]
                
            res[j] = s[i]
            i += 1
            j -= 1
    return "".join(res)    