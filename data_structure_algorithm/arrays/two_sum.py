# def two_sum(nums, target):

#         d = {}

#         for i in range(len(nums)):
#             need = target - nums[i]

#             if need in d:
#                 return [d[need], i]

#             d[nums[i]] = i
#         return []
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))

# def twoSum(self, nums, target):
        
#         hashmap = {}
#         for i in range(len(nums)):
#             required = target - nums[i]
#             if required in hashmap:
#                 return [hashmap[required], i]
#             hashmap[nums[i]] = i
#         return []