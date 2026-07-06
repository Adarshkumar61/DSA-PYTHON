# def remove_element(nums, val):
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k +=1
#     return k
# nums = [3,2,3,2,3,4,5,6]
# val = 2
# print(remove_element(nums, val))
# # This will return the number of elements in nums which are not equal to val.


# def remove_element(num, val):
#     k = 0
#     for i in range(len(num)):
#         if num[i]!= val:
#             num[k] = num[i]
#             k+=1
#     return k
# num = [ 2, 4, 5, 3, 3]
# val = 3
# k = remove_element(num, val)
# print(num[:k])



# def removeElement(nums, val):
#         k = 0
#         for i in range(len(nums)):
#                 if nums[i] != val:
#                         nums[k] = nums[i]
#                         k += 1
#         return k


# # if __name__ == "__main__":
# #         # LeetCode example
# nums = [3, 2, 2, 3]
# val = 3
# k = removeElement(nums, val)
#         # print(k)
# print(nums[:k])


# def removing_same_element_in_a_array(arr, value):
#     element = 0
#     for i in range(len(arr)):
#         if arr[i]!= value:
#             arr[element] = arr[i]
#             element+=1
#     return element

# arr = [1,2,4,5,5,3,1,2,3]
# value = 5
# result = removing_same_element_in_a_array(arr, value)
# print(result)
# print(arr[:result])




# def remove_specific_element_from_array(arr, val):
#     k = 0
#     for i in range(len(arr)):
#         if arr[i] != val:
#             arr[k] = arr[i]
#             k+=1
#     return k

# arr = [1,2,4,5,6,6,4,5,6]
# val = 6
# r =  remove_specific_element_from_array(arr, val)
# print(r)
# print(arr[:r])



# def remove_specific_element_from_array(arr, val):
#     k = 0
#     for i in range(len(arr)):
#         if arr[i] == val:
#             continue
#         arr[k] = arr[i]
#         k+=1
#     return k
# arr = [1,2,4,5,6,6,4,5,6]
# val = 6
# r =  remove_specific_element_from_array(arr, val)
# print(r)
# print(arr[:r])



def remove_var_element(nums, value):
    k = 0
    for i in range(len(nums)):
        if nums[i] != value:
            nums[k] = nums[i]
            k+=1
    return k
nums = [1,2,3,5,6,2,3]
value = 3
r = remove_var_element(nums, value)
print(r)
print(nums[:r])