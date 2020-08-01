    def getDigits(self, n: int) -> list:
        res = []
        while n:
            d, m = divmod(n, 10)
            res.append(m)
            n = d
        return res
    
    def isHappy(self, n: int) -> bool:
        s = set()
        while 1:
            s.add(n)
            get_sum = sum(map(lambda x: x*x, self.getDigits(n)))
            n = get_sum
            if n == 1: return True
            if n in s: return False

    def isHappy(self, n: int) -> bool:
        def squaresum(num):
            result = 0
            while num > 0:
                result += pow((num % 10),2)
                num = num // 10
            return result
        seen = []
        while squaresum(n) not in seen:
            sum1 = squaresum(n)
            if sum1 == 1:
                return True
            else:
                seen.append(sum1)
                n = sum1 
        return False