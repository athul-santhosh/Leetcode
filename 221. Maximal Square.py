class Solution:
    def maximalSquare(self, matrix):
        ans = 0
        
        n = len(matrix)
        m = len(matrix[0])
        print(m)
        print(n)
        for i in range(m):
            if matrix[0][i] == '1':
                ans = 1
        for i in range(n):
            if matrix[i][0] == '1':
                ans = 1
                
        
        
        
        for i in range(1,n):
            for j in range(1,m):
                
                if matrix[i][j] == "1":
                    matrix[i][j] = min(int(matrix[i-1][j]),int(matrix[i-1][j-1]),int(matrix[i][j-1])) + 1
                    ans = max(ans,matrix[i][j])
        for i in matrix:
            print(i)
        return ans*ans


            
        
        


ll = Solution()
matrix1= [
[1,0,1,0,0],
[1,0,1,1,1],
[1,1,1,1,1],
[1,0,0,1,0]
]
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(ll.maximalSquare(matrix))
print(ll.maximalSquare(matrix1))