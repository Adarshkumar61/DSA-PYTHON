#when array sorted

def two_sum(arr, target):
    left =0
    right = len(arr) -1
    
    while left < right:
        curr_sum = arr[left] +arr[right]
        if curr_sum > target:
            right-=1
        elif curr_sum < target:
            left+=1
        else:
            return [left, right]
 
arr = [2, 7, 11, 15]
target = 9
# print(two_sum(arr, target))
r = two_sum(arr, target)
print(r)
print(arr[r[0]], arr[r[1]])
"""
explanation :When:

left == right

you are pointing to the SAME element.

Example:

[2,7,11,15]
    ↑
   L,R

Now if you calculate:

arr[left] + arr[right]

you're doing:

7 + 7

using the same element twice.

Most Two Sum problems don't allow that.

Therefore we stop at:

while left < right """