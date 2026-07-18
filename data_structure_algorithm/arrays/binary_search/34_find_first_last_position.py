# def find_first_last_position(nums, is_first, target):
#     left = 0
#     right = len(nums) - 1
#     ans = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             ans = mid
#             if is_first:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return ans
# nums = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]
# target = 5
# first_position = find_first_last_position(nums, True, target)
# last_position = find_first_last_position(nums, False, target)
# print(first_position, last_position)



def find_first_last_occurance(nums, isfirst, target):
    left = 0
    right = len(nums) -1
    ans= -1
    while left <= right:
        mid = (left + right) //2
        if nums[mid] == target:
            ans = mid
            if isfirst:
                right = mid-1
            else:
                left = mid+1
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid -1
    return ans
nums = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]
target = 5
first_occurance = find_first_last_occurance(nums, True, target)
last_occurance = find_first_last_occurance(nums, False, target)
print(first_occurance, last_occurance)



# def searchRange(nums, target):

#     def findBound(isFirst):
#         left = 0
#         right = len(nums) - 1
#         ans = -1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 ans = mid
#                 if isFirst:
#                     right = mid - 1   # move left
#                 else:
#                     left = mid + 1    # move right

#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return ans

#     return [findBound(True), findBound(False)]


# print(searchRange([5,7,7,8,8,10], 8))