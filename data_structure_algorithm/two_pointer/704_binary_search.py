# this is for sorted array only:

def binary_search(nums, target):
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = (left + right) //2
        
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left  = mid +1
        else:
            right = mid-1
    return -1
nums = [1,2,3,4,5,6,7,8,9]
target = 5
r = binary_search(nums, target)
print(r)