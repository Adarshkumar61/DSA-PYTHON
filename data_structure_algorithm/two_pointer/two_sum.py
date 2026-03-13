# array  = [1,2,3,4,5,6] # array should be sorted for two pointer approach
# target = 7

# left = 0
# right = len(array)-1

# while left < right :
#     summ = array[left] + array[right]
#     if summ == target:
        
#         print('target is :', target, 'and pair is: ', array[left], array[right])
#         break
    
#     elif summ > target: #moving right ← value decreases
#         right -=1
#     elif summ < target:
#         left +=1

#check if the given array is palindrome or not
#using two pointer approach
# arr = [1,2,3,2,1, 1]

# left = 0
# right = len(arr)-1

# is_palindrome = True

# while left < right:

#     if arr[left] != arr[right]:
#         is_palindrome = False
#         print('not a palindrome')
#         break

#     left += 1
#     right -= 1

# print(is_palindrome)

# def twoSum(self, nums, target):

#         d = {}

#         for i in range(len(nums)):
#             need = target - nums[i]

#             if need in d:
#                 return [d[need], i]

#             d[nums[i]] = i
#         return []
# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(0,nums, target))]


# def removeDuplicates(arr):

    # if len(arr) == 0:
    #     return 0

    # slow = 0# we are pointing to the first element in array which is always unique

    # for fast in range(1, len(arr)):

    #     if arr[fast] != arr[slow]: #When: arr[fast] == arr[slow] Condition becomes False,  Python does nothing
    #         slow += 1
    #         arr[slow] = arr[fast]

    # return slow + 1

# removing dublicates:
# arr = [1,2,4, 4, 4, 5,5,5, 6,7, 8,8 ,8, 9]

# slow = 0
# for fast in range(1, len(arr)):
#     if arr[fast] != arr[slow]: #Is the current number different from the last unique number
#         slow+=1
#         arr[slow] = arr[fast]
# print(slow+1)
# print(arr[:slow+1])
"""We have:

slow → points to last unique element

fast → points to current element we are checking

So this condition is asking:

Is current element NEW ?
OR is it DUPLICATE ?"""

#move zero to end of array :
def movezeroes(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast]!= 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow+=1
    return arr
arr = [0,1,0,3,12]
print(movezeroes(arr))
