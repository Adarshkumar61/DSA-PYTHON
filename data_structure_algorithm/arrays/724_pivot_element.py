def pivot_element(nums):
    left = 0
    total_sum = sum(nums)
    for i in range(len(nums)):
        right_sum = total_sum - left - nums[i]
        if right_sum == left:
            return i
        left+= nums[i]
    return -1


