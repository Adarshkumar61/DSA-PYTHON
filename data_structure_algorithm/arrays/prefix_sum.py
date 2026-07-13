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










# def pre_sum(nums, right, left):
#     pre = [0] * len(nums)
#     pre[0] = nums[0]
#     for i in range(1, len(nums)):
#         pre[i] = pre[i-1] + nums[i]
#     if left == 0:
#         return pre[right]
#     return pre[right] - pre[left -1]
# nums = [1,2,3,4,5]
# right = 3
# left = 1
# print(pre_sum(nums, right, left))












def pre_s(num):
    prefix  = [0] * len(num)
    prefix[0] = num[0]
    for i in range(1, len(num)):
        prefix[i] = prefix[i-1] + num[i]
    return prefix

num = [1,2,3,4,5]
print(pre_s(num))



"""
DRY RUN:
num = [1, 2, 3, 4, 5]
Step 1
prefix = [0, 0, 0, 0, 0]
Step 2
prefix[0] = num[0]
prefix = [1, 0, 0, 0, 0]
Loop Starts
Iteration 1
i = 1
prefix[1] = prefix[0] + num[1]
= 1 + 2
= 3
prefix = [1, 3, 0, 0, 0]
Iteration 2
i = 2
prefix[2] = prefix[1] + num[2]
= 3 + 3
= 6
prefix = [1, 3, 6, 0, 0]
Iteration 3
i = 3
prefix[3] = prefix[2] + num[3]
= 6 + 4
= 10
prefix = [1, 3, 6, 10, 0]
Iteration 4
i = 4
prefix[4] = prefix[3] + num[4]
= 10 + 5
= 15
prefix = [1, 3, 6, 10, 15]
Loop Ends
return prefix

Output:

[1, 3, 6, 10, 15]
Visualization
num    = [1, 2, 3, 4, 5]
index    0  1  2  3  4

prefix = [1, 3, 6, 10, 15]

Each position stores the sum from index 0 up to that index:

Index	Prefix Value	Meaning
0	1	1
1	3	1 + 2
2	6	1 + 2 + 3
3	10	1 + 2 + 3 + 4
4	15	1 + 2 + 3 + 4 + 5
"""