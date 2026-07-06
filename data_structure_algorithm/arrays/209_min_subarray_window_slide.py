# def minSubArrayLen(target, nums):

#     left = 0
#     current_sum = 0
#     min_length = float('inf')

#     for right in range(len(nums)):

#         # Expand the window
#         current_sum += nums[right]

#         # Shrink while window is valid
#         while current_sum >= target:

#             length = right - left + 1

#             if length < min_length:
#                 min_length = length

#             current_sum -= nums[left]
#             left += 1

#     if min_length == float('inf'):
#         return 0

#     return min_length
# nums = [2,3,1,2,4,3]
# target = 7
# print(minSubArrayLen(target, nums))







# def minimum_size_subarray_sum(nums, target):
#     left = 0
#     current_sum = 0
#     min_length = float('inf')
#     base_left = 0
#     base_right = 0

#     for right in range(len(nums)):
#         current_sum += nums[right]
#         while current_sum >= target:
#             length = right - left +1
#             if length < min_length:
#                 min_length = length
#                 base_left = left
#                 base_right = right

#             current_sum -= nums[left]
#             left +=1
#     if min_length == float('inf'):
#         return 0
#     return nums[base_left : base_right + 1]

# nums = [2,3,1,2,4,3]
# target = 7
# r = minimum_size_subarray_sum(nums, target)
# print(r)
















# def minsize_length_to_get_target(arr, t):
#     left = 0
#     min_len = float('inf')
#     current_sum = 0
#     for right in range(len(arr)):
#         current_sum += arr[right]
#     while current_sum >= t:
#         length  =  right - left + 1
#         if length < min_len:
#             min_len  = length
#         current_sum -= arr[left]
#         left += 1
#     # if min_len == float('inf'):
#     #     return 0
#     return min_len

# arr = [2,3,1,2,4,3]
# t = 7

# r = minsize_length_to_get_target(arr, t)
# print(r)


def minsize_best_length_to_get_target(arr, target):
    left = 0
    curr_sum = 0
    min_length = float('inf')
    best_left = 0
    best_right = 0
    for right in range(len(arr)):
        curr_sum += arr[right]
    while curr_sum >= target:
        length = right - left+1
        if length < min_length:
            min_length = length
            best_left = left
            best_right = right
        curr_sum -= arr[left]
        left +=1
    if min_length == float('inf'):
        return 0
    return arr[best_left : best_right + 1]


arr = [2,3,1,2,4]
target = 7
r = minsize_best_length_to_get_target(arr, target)
print(r)
