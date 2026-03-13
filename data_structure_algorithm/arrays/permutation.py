def permutation(arr):
    n = len(arr)
    ans = [0]*n

    for i in range(n):
        ans[i] = arr[arr[i]]
    return ans
arr = [0, 2, 1, 5, 3, 4]
print(permutation(arr))

 
 
# permutation code with proper all factor:
def permute(arr, start=0):
    
    if start == len(arr):
        print(arr)
        return

    for i in range(start, len(arr)):
        # fix arr[i] at position 'start'
        arr[start], arr[i] = arr[i], arr[start]   # swap

        permute(arr, start + 1)                    # recurse

        arr[start], arr[i] = arr[i], arr[start]   # swap BACK

arr = [1, 2, 3]
permute(arr)