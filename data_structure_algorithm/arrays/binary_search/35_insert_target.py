def binary_search_insert_position(nums, target):
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = (left + right) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid +1
        else:
            right = mid-1
    return left
nums = [1,2,3,6,7,8,9]
target = 5
r = binary_search_insert_position(nums, target)

print(r)