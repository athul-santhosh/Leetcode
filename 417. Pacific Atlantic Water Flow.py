class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    	cordinates = []
    	# base case
    	if len(matrix) == 0:
    		return cordinates


    	row = len(matrix)
    	col = len(matrix[0])
    	# intitializing both the comparison matrix
    	
    	pacific = [[0 for j in range(col)] for i in range(row)]
    	atlantic = [[0 for j in range(col)] for i in range(row)]
    	
    	mini = float("-inf")

    	def dfs(matrix,row,col,ocean,prev):

    		if row <0 or col <0 or row > len(matrix)-1 or col > len(matrix[0])-1:
    			return

    		elif prev > matrix[row][col]:
    			return
    		elif ocean[row][col] == 1:
    			return

    		ocean[row][col] = 1
    		dfs(matrix,row-1,col,ocean,matrix[row][col]) #U
    		dfs(matrix,row+1,col,ocean,matrix[row][col]) #D
    		dfs(matrix,row,col+1,ocean,matrix[row][col]) #L
    		dfs(matrix,row,col-1,ocean,matrix[row][col]) #R
    	
    	# first row # las row
    	for i in range(0,col):
    		dfs(matrix,0,i,pacific,mini)
    		dfs(matrix,row-1,i,atlantic,mini)
    	# first col # last col
    	for i in range(0,row):
    		dfs(matrix,i,0,pacific,mini)
    		dfs(matrix,i,col-1,atlantic,mini)

    	for i in range(row):
    		for j in range(col):
    			if atlantic[i][j] == 1 and pacific[i][j] == 1:
    				 cordinates.append([i,j])
    	return cordinates