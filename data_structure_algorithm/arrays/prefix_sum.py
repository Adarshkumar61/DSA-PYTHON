# def prefix_sum(nums):
#     prefix = [0] * len(nums)
#     prefix[0] = nums[0]
#     for i in range(1, len(nums)):
#         prefix[i] = prefix[i-1] + nums[i]
#     return prefix
# nums = [5,10,15,20]
# print(prefix_sum(nums))



def prefix_sum(nums, left_index, right_index):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
    if left_index == 0:
        return prefix[right_index]
    return prefix[right_index] - prefix[left_index -1]

nums = [5,10,15,20]
left_index = 1
right_index = 3
r = prefix_sum(nums, left_index, right_index)
print(f'sum of array from index {left_index} to {right_index} is : {r}')







# def prefix_sum_of_index(nums, left_index, right_index):
#     prefix = [0] * len(nums)
#     prefix[0] = nums[0]
#     for i in range(1, len(nums)):
#         prefix[i] = prefix[i-1]+ nums[i]
#     if left_index == 0:
#         return prefix[right_index]
#     return prefix[right_index] - prefix[left_index-1]
# nums = [5,10,15,20]
# print(prefix_sum_of_index(nums, left_index= 0, right_index= 3))










def pre_sum(nums, right, left):
    pre = [0] * len(nums)
    pre[0] = nums[0]
    for i in range(1, len(nums)):
        pre[i] = pre[i-1] + nums[i]
    if left == 0:
        return pre[right]
    return pre[right] - pre[left -1]
nums = [1,2,3,4,5]
right = 3
left = 1
print(pre_sum(nums, right, left))













