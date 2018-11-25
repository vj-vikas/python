'''def sort(nums):
	for i in range(5):
		minpos = i
		for j in range(i,6):
			if nums[j]< nums[minpos]:
				minpos = j
		temp = nums[i]
		nums[i] = nums[minpos]
		nums[minpos] = temp

		print(nums) '''
pos = -1
print(pos)

def sort(nums):
	k = len(nums)
	for i in range(k):
		for j in range(k-i-1):
			if nums[j]> nums[j+1]:
				temp =nums[j]
				nums[j]=nums[j+1]
				nums[j+1]=temp
					

nums = [5,3,8,6,7,2]
sort(nums)
print(nums)


u = len(nums)
x=7
l=0

while u >= l:
	mid=(l+u) // 2

	if nums[mid]==x:
		pos=mid
		break	

	else:
		if nums[mid]>x:
			u=mid-1

		else:
			l=mid+1


print(pos)	