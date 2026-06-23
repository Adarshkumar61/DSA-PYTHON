# def remove_duplicates(arr):

#     k = 0

#     for i in range(1, len(arr)):
#         if arr[i] != arr[k]:
#             k += 1
#             arr[k] = arr[i]
#     return k + 1


# arr = [1, 2, 2, 3, 4, 4, 5]
# k = remove_duplicates(arr)

# print("k =", k)
# print("array =", arr)


# explanation = """
# Start
# arr = [1,2,2,3,4,4,5]
# k = 0
# 👉 Step 1
# i = 1
# arr[i] = 2
# arr[k] = 1

# Different → new unique element

# So:

# k = 1
# arr[1] = 2

# Array:

# [1,2,2,3,4,4,5]
# 👉 Step 2
# i = 2
# arr[i] = 2
# arr[k] = 2

# Same → duplicate → skip

# 👉 Step 3
# i = 3
# arr[i] = 3
# arr[k] = 2

# Different → new unique

# k = 2
# arr[2] = 3

# Array becomes:

# [1,2,3,3,4,4,5]
# 👉 Step 4
# i = 4
# arr[i] = 4
# arr[k] = 3

# Different:

# k = 3
# arr[3] = 4

# Array:

# [1,2,3,4,4,4,5]
# 👉 Step 5
# i = 5
# arr[i] = 4
# arr[k] = 4

# Duplicate → skip

# 👉 Step 6
# i = 6
# arr[i] = 5
# arr[k] = 4

# Different:

# k = 4
# arr[4] = 5

# Final array:

# [1,2,3,4,5,4,5]"""



# def removing_dublicate_in_sorted_array(arr):
#     k = 0
#     #k is the writer. It points to the last position where you wrote a unique value. 
#     # It starts at 0 because index 0 is always unique by defaul
#     for i in range(1, len(arr)):
#         if arr[i] != arr[k]:
#             k +=1
#             arr[k] = arr[i]
#     return k+1

# arr = [1,2,2,3,4,4,5]
# k = removing_dublicate_in_sorted_array(arr)
# print(k)
# print(arr[:k])

# def removing_dublicate_in_sorted_array(arr):
#     k = 0
#     for i in range(1, len(arr)):
#         if arr[i] == arr[k]:
#             continue
#         k+=1
#         arr[k] = arr[i]
#     return k+1

# arr = [1,2,2,3,4,4,5]
# k = removing_dublicate_in_sorted_array(arr)
# print(k)
# print(arr[:k])



# fresh code : 

def remove_element_from_sort_array(arr):
    k = 0
    for i in range(1, len(arr)):
        if arr[i]!= arr[k]:
            k+=1
            arr[k] = arr[i]
    return k+1

arr  = [1,2,4,5,6,6,6]
r = remove_element_from_sort_array(arr)
print(arr[:r])