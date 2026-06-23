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
