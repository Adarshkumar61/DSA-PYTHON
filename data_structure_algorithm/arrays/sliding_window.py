# def sliding_window(arr, k):
#     summ = sum(arr[:k])
#     max_sum = summ
#     best_subarray = arr[:k]
#     for i in range(k, len( arr)):
#         summ = summ - arr[i-k] + arr[i]
#         current_subarray = arr[i-k+1 : i+1]
#         if summ > max_sum:
#             max_sum =  summ
#             best_subarray = current_subarray

#     print(f"Max sum: {max_sum}")
#     print(f"Subarray: {best_subarray}")

# arr = [2, 1, 5, 1, 3, 2]
# sliding_window(arr, 3)














# ============================================================
# PROBLEM 1: Maximum sum subarray of size k (fixed window)
# Input: arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3], k = 3
# Output: max sum and the actual subarray
# ============================================================







def max_sum_subarray(arr, k):
    n = len(arr)
    
    if n < k:
        return -1, []
    
    # Step 1: Build the first window of size k
    window_sum = sum(arr[:k])  # sum of first k elements
    max_sum = window_sum
    max_start = 0  # tracks where best window starts
    
    # Step 2: Slide the window from index k to n-1
    for i in range(k, n):
        # Add the new element coming in (arr[i])
        # Remove the element going out (arr[i - k])
        window_sum = window_sum + arr[i] - arr[i - k]
        
        # Update max if current window is better
        if window_sum > max_sum:
            max_sum = window_sum
            max_start = i - k + 1  # window starts here
    
    # Return max sum AND the actual subarray
    result_subarray = arr[max_start : max_start + k]
    return max_sum, result_subarray


# arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# k = 3
# max_sum, subarray = max_sum_subarray(arr, k)
# print(f"Max sum: {max_sum}")        # 17
# print(f"Subarray: {subarray}")      # [9, 2, 6]


# # ============================================================
# # PROBLEM 2: Smallest subarray with sum >= target (variable window)
# # Input: arr = [2, 3, 1, 2, 4, 3], target = 7
# # Output: length of smallest subarray + the subarray itself
# # ============================================================

# # def smallest_subarray_with_sum(arr, target):
# #     n = len(arr)
    
# #     left = 0           # left pointer of window
# #     window_sum = 0     # current window sum
# #     min_len = float('inf')
# #     best_left = 0
# #     best_right = 0
    
# #     for right in range(n):         # right pointer expands window
# #         window_sum += arr[right]   # add new element into window
        
# #         # Shrink window from left as long as condition is met
# #         while window_sum >= target:
# #             # Check if this is the smallest window so far
# #             current_len = right - left + 1
# #             if current_len < min_len:
# #                 min_len = current_len
# #                 best_left = left
# #                 best_right = right
            
# #             window_sum -= arr[left]  # remove leftmost element
# #             left += 1                # shrink window from left
    
# #     if min_len == float('inf'):
# #         return 0, []   # no valid subarray found
    
# #     result_subarray = arr[best_left : best_right + 1]
# #     return min_len, result_subarray


# # arr = [2, 3, 1, 2, 4, 3]
# # target = 7
# # length, subarray = smallest_subarray_with_sum(arr, target)
# # print(f"Min length: {length}")    # 2
# # print(f"Subarray: {subarray}")    # [4, 3]





# longest subarray with at most k distinct characters (variable window):
# def longest_subarray(arr, k):

#     left = 0
#     current_sum = 0
#     max_length = 0

#     for right in range(len(arr)):

#         current_sum += arr[right]

#         while current_sum > k:
#             current_sum -= arr[left]
#             left += 1

#         max_length = max(max_length, right - left + 1)

#     return max_length


# arr = [4, 2, 1, 7, 3]
# print(longest_subarray(arr, 8))







# def longest_length_to_get_target(nums, target):
#     left = 0
#     curr_sum = 0
#     max_length = 0
#     for right in range(len(nums)):
#         curr_sum += nums[right]
#         while curr_sum > target:
#             curr_sum -= nums[left]
#             left+=1
#         max_length = max(max_length, right - left + 1)
#     return max_length
# nums = [4, 2, 1, 7, 3]
# print(longest_length_to_get_target(nums, 7))




# def sliding_target_window(nums, target):
#     left = 0
#     curr_sum = 0
#     max_length = 0
#     for right in range(len(nums)):
#         curr_sum += nums[right]
#         while curr_sum > target:
#             curr_sum -= nums[left]
#             left +=1
#         max_length = max(max_length, right - left +1)
#     return max_length

# nums = [4, 2, 1, 7, 3]
# target = 7
# print(sliding_target_window(nums, target))











def sliding_window(nums, target):
    left = 0
    curr_sum = nums[0]
    max_sum = nums[0]
    for i in range(1,len(nums)):
        curr_sum += nums[i]
        while curr_sum > target:
            curr_sum -= nums[left]
            left +=1

        max_sum = max(max_sum, i -left +1)
    return max_sum
nums = [4, 2, 1, 7, 3]
target = 7
print(sliding_window(nums, target))
