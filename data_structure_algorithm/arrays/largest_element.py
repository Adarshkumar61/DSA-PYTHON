#largest element in an array :

# array = [5, 3, 7, 2, 9]
# 1st way:
# largest = array[0]
# for i in range(len(array)):
#     if array[i] >  largest:
#         largest = array[i]
# print(f'largest element in {array} is {largest}')
# 2nd way:
# largest = array[0]
# for num in array:
#     if num > largest:
#         largest = num
# print(largest)

# finding second largest:

array = [5, 3, 7, 2, 9]
lar = float('-inf')
sec_lar = float('-inf')

for n in array:
    if n > lar:
        sec_lar = lar
        lar = n
    elif n > sec_lar and n != lar:
        sec_lar = n
print(array, 'second largest in this is: ', sec_lar)

#third largest:

# array = [1,12, 65, 123,66,  4, 54, 166, 127]
# lar = float('-inf')
# sec_lar = float('-inf')
# third_lar = float('-inf')

# for n in array:
#     if n > lar:
#         third_lar = sec_lar
#         sec_lar = lar
#         lar = n
#     elif n > sec_lar and n != lar:
#         third_lar = sec_lar
#         sec_lar = n
        
#     elif n > third_lar and n!= sec_lar and n!= lar:
#         third_lar = n
# print({f'{array}, third largest in this is: {third_lar}'})
# print(third_lar)

#practice:
# def max_element(arr):
#     max_no = arr[0]

#     for i in range(len(arr)):
#         if arr[i] > max_no:
#             max_no = arr[i]
#     return max_no
# arr = [1,2 , 66, 23, 24, 213]
# print(max_element(arr))

#practice:
# def second_largest_element(arr):
#     largest = float('-inf')
#     second_largest = float('-inf')

#     for i in range(len(arr)):
#         if arr[i] > largest:
#             second_largest = largest
#             largest = arr[i]
#         elif arr[i] > second_largest and arr[i]!= largest:
#             second_largest = arr[i]
#     # return second_largest
#     # return largest
# num = [1,2 , 66, 23, 24, 213]
# print(second_largest_element(num))


# practice :
# def third_largest_number(arr):
    # first = float('-inf')
    # second = float('inf')
    # third = float('-inf')

    # for i in range()