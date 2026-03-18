# def permutations(arr, start):

#     if start == len(arr):
#         print(arr[:])
#         return

#     for i in range(start, len(arr)):

#         arr[start], arr[i] = arr[i], arr[start]

#         permutations(arr, start + 1)

#         arr[start], arr[i] = arr[i], arr[start]   # backtrack



# permutations([1,2,3], 0)


#leet code based:
# def nextPermutation(self, nums):

#         i = len(nums) - 2

#         while i >= 0 and nums[i] >= nums[i+1]:
#             i -= 1

#         if i >= 0:
#             j = len(nums) - 1
#             while nums[j] <= nums[i]:
#                 j -= 1

#             nums[i], nums[j] = nums[j], nums[i]

#         nums[i+1:] = reversed(nums[i+1:])