
# def dailyTemperatures(self, T: List[int]) -> List[int]:     # Brute force approach
#        result = [0] * len(T)       							# Time O(n*n) Space O(n)
#         for current in range(len(T)):
#             for next in range(current +1 , len(T)):
#                 if T[next] > T[current]:
#                     result[current] = next - current
#                     break
#         return result

def dailyTemperature(T):                                  # Time O(n) solution
	result = [0] * len(T)

	current = len(T) -1
	stack = []


	while current >= 0:

		if len(stack) == 0:
			stack.append((T[current],current))
			current = current - 1
			
		elif T[current] >= stack[-1][0]:
			stack.pop()
		else:
			result[current] = stack[-1][1] - current
			stack.append((T[current],current))
			current = current - 1
		print(stack)
	print(result)

# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         result, stack = [0] * len(T), []
#         for i, t in enumerate(T):
#             while stack and T[stack[-1]] < t: 
#                 prevIndex = stack.pop()
#                 result[prevIndex] = i - prevIndex
#             stack += i,
#         return result
	



dailyTemperature([89,62,70,58,47,47,46,76,100,70])






            