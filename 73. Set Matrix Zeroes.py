#73. Set Matrix Zeroes

def SetMatrix(matrix):
	n = len(matrix)
	m = len(matrix[0])

	row = []
	col = []

	for i in range(n):
		for j in range(m):
			if matrix[i][j] == 0:
				row.append(i)
				col.append(j)

	def setrow(matrix,row):
		for i in range(m):
			matrix[row][i] = 0

	def setcol(matrix,col):
		for i in range(n):
			matrix[i][col] = 0
	
	for i in row:
		setrow(matrix,i)

	for j in col:
		setcol(matrix,j)

	print(matrix)







SetMatrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]])









































