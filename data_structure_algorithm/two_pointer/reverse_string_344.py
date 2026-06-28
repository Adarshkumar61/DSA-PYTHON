# def reverse_array(array):
#     left = 0
#     right = len(array) -1
#     while left < right:
#         # array[left], array[right] = array[right], array[left]
#         temp = array[left]
#         array[left] = array[right]
#         array[right] = temp

#         left+=1
#         right-=1
#     return array

# array = [1,2,3,4,5]
# r = reverse_array(array)
# print(r)



# Write a function:

# def reverse_string(s):

# Input

# ['h','e','l','l','o']

# Expected Output

# ['o','l','l','e','h']

# Rules:

# Don't create another list.
# Use left and right pointers.
# Time: O(n)
# Space: O(1)


def reverse_string(s):
    left = 0
    right = len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]

        left +=1
        right-=1
    return s

s = ['h','e','l','l','o']
r = reverse_string(s)
print(r)