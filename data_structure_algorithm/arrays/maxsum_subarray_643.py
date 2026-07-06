# def maxsum_subarray(arr, val):
#     window_sum = sum(arr[:val])
#     max_sum = window_sum

#     for i in range(val, len(arr)):
#         window_sum -= arr[i - val]

#         window_sum += arr[i]

#         if window_sum > max_sum:
#             max_sum = window_sum
#     return max_sum

# arr = [2,1,5,1,3,2]
# val = 3
# r = maxsum_subarray(arr, val)
# print(f'max sum of array of 3 joint element is : {r}')

 

"""
Dry Run (This Is the Most Important Part)

Array

2 1 5 1 3 2

Window size

k = 3
First Window
2 1 5

Sum

8

Variables

window_sum = 8
max_sum = 8
Loop Starts
i = 3

Current element

1

Current window

2 1 5

Need next window

1 5 1
Remove
window_sum -= arr[i-k]

Substitute values

window_sum -= arr[3-3]
window_sum -= arr[0]
window_sum -= 2

Result

8 → 6
Add
window_sum += arr[i]

becomes

window_sum += arr[3]
window_sum += 1

Result

6 → 7

Now

window_sum = 7

Maximum

8

No update.

Next Iteration
i = 4

Need

5 1 3

Current sum

7

Remove

arr[1]

Remove

1
7 → 6

Add

arr[4]

Add

3
6 → 9

Now

max_sum = 9
Last Iteration

Need

1 3 2

Remove

5
9 → 4

Add

2
4 → 6

Maximum remains

9

Done.
"""

# final code :
# def max_window_sum(arr, val):
#     summ = sum(arr[:val])
#     max_value = summ
#     for i in range(val, len(arr)):

#         summ -= arr[i - val]
#         summ += arr[i]

#         if summ > max_value:
#             max_value = summ
#     return max_value

# arr = [2,1,5,1,3,2]
# val = 3
# r = max_window_sum(arr, val)
# print(f'max sum of array of 3 joint element is : {r}')