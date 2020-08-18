class Solution:
    def numsSameConsecDiff(self,N,K):
        n = N
        k = K
        res = []
        if n == 1:
            res = [i for i in range(10)]
            return res
        def dfs(n,k,cur,prev,index,res):
            if index == n-1:   
                res.append(cur)
                return res
            next = prev + k
            if next < 10:
                dfs(n,k,(cur*10)+next,next,index + 1,res)
            next = prev - k
            if next >= 0 and k != 0:
                dfs(n,k,(cur* 10)+next,next,index + 1,res)
			
        for i in range(1,10):
            dfs(n,k,i,i,0,res)
        return res
    




athul = Solution()
print(athul.numsSameConsecDiff(5,3))