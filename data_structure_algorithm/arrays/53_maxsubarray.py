def maxSubArray(nums):

    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):

        current_sum = max(nums[i], current_sum + nums[i])

        max_sum = max(max_sum, current_sum)

    return max_sum





























# def kadane_algorithm(num):
#     curr_sum = num[0]
#     max_sum = num[0]
#     for i in range(1, len(num)):
#         curr_sum = max(num[i], curr_sum + num[i])
#         max_sum = max(curr_sum, max_sum)
        
#     return max_sum
# num = [4,-1,2]
# r = kadane_algorithm(num)
# print(f'maximum sum of subarray is : {r}')




# returning subarray with index
def max_sub_array_with_indices(nums):
    curr_sum = nums[0]
    max_sum = nums[0]
    start = 0
    end = 0
    temp = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i] + curr_sum:
            curr_sum = nums[i]
            temp = i
        else:
            curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp
            end = i
    return max_sum, nums[start:end+1]
nums = [-2,1,-3,4,-1,2,1,-5,4]
r = max_sub_array_with_indices(nums)
print(f'maximum sum of subarray is : {r[0]} and the subarray is : {r[1]}')



"""
Dry Run
nums = [-2,1,-3,4,-1,2,1,-5,4]

Initially

current_sum = -2
max_sum = -2

start = 0
end = 0
temp_start = 0
i = 1

Current number

1

Should we continue?

-2 + 1 = -1

Start fresh?

1

Choose

1

So

temp_start = 1
current_sum = 1

New best?

Yes.

start = 1
end = 1
max_sum = 1
i = 2

Current number

-3

Continue

1 + (-3) = -2

Start fresh

-3

Choose

-2

No new maximum.

Nothing changes.

i = 3 ⭐

Current number

4

Continue

-2 + 4 = 2

Start fresh

4

Choose

4

So

temp_start = 3
current_sum = 4

New maximum?

Yes.

start = 3
end = 3
max_sum = 4

Notice what happened.

The algorithm remembered that the current best subarray starts at index 3.

Continue...

At -1, 2, and 1, we keep extending the same subarray because continuing is better than starting over.

When current_sum becomes 6, we update:

max_sum = 6
start = 3
end = 6
Final Answer
max_sum = 6
start = 3
end = 6

The subarray is:

nums[start:end+1]

Substitute:

nums[3:7]

Output:

[4, -1, 2, 1]
"""