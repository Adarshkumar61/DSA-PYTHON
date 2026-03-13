# intution : Running sum means:

# At every index → store sum of all previous elements including current

# def running_sum(nums):
#     ans = [0] * len(nums)
#     ans[0] = nums[0]
#     for i in range(1, len(nums)):
#        ans[i] = ans[i-1] + nums[i]
#     return ans
# nums = [4,2, 3, 4]
# print(running_sum(nums))

nums = [4,2, 3, 4]
for i in range(1, len(nums)):
    nums[i] = nums[i] + nums[i-1]
print(nums)
