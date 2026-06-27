# def movezero(arr):
#     slow = 0
#     for fast in range(len(arr)):
#         if arr[fast] != 0:
#             arr[slow], arr[fast] = arr[fast], arr[slow]
#             slow +=1
#     return arr
# arr = [1, 0, 3, 0, 6, 3, 0]
# print(movezero(arr))



def movezeroes(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[k] = arr[i]
            k+=1
    while k< len(arr): # this fills the remaining positions with zeros
        arr[k] = 0
        k+=1
    return arr


arr = [1, 0, 3, 0, 6, 3, 0]
r= movezeroes(arr)

print(r)


# Explanation:


# i

# as:

# Scanner

# It checks every element.

# And:

# k

# as:

# Next empty position for a non-zero element