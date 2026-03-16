def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k +=1
    return k
nums = [3, 2, 3]
val = 2
print(remove_element(nums, val))
# This will return the number of elements in nums which are not equal to val.