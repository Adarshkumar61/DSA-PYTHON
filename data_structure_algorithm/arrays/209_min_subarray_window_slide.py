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







def minimum_size_subarray_sum(nums, target):
    left = 0
    current_sum = 0
    min_length = float('inf')
    base_left = 0
    base_right = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            length = right - left +1
            if length < min_length:
                min_length = length
                base_left = left
                base_right = right

            current_sum -= nums[left]
            left +=1
    if min_length == float('inf'):
        return 0
    return nums[base_left : base_right + 1]

nums = [2,3,1,2,4,3]
target = 7
r = minimum_size_subarray_sum(nums, target)
print(r)
