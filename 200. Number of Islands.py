class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        def dfs(grid,row,col):
            
            if row > len(grid)-1 or col > len(grid[0])-1 or col < 0 or row < 0:
                return 
            if grid[row][col] == '0':
                return 
            
            grid[row][col] = '0'
            #up down right left
            dfs(grid,row -1,col)
            dfs(grid,row +1,col)
            dfs(grid,row,col -1)
            dfs(grid,row,col + 1)
            
            
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(grid,row,col)
                    island += 1
                    
        return island