# leetcode 26 remove duplicates from sorted array
def array_sort(nums):
	if len(nums) == 0:
		return 0
	
	i = 0
	print(len(nums))

	for j in range(1,len(nums)):
		if nums[i] != nums[j]:                 # if we encounter. new element
			i += 1

			nums[i] = nums[j]
	print(nums[:i+1])
	print(len(nums))                            # the array is modified but not shrinked its size
	return i + 1                                # we add 1 to i because indexing is from 0 to n-1



def removeDuplicates(self, nums: List[int]) -> int:
    duplicate = 0
    for element in range(1,len(nums)):
        if nums[duplicate] != nums[element]:
            duplicate += 1
            nums[duplicate] = nums[element]
    return duplicate + 1


def removeDuplicates(self, nums: List[int]) -> int:
    i = 0
    last_num = None
    for num in nums:
        if num != last_num:
            nums[i] = num
            i += 1
        last_num = num
    return i


	


nums =[1,1,1,1,1,4,4,4,4,5,5,5,5,5,7,7]
print(array_sort(nums))