#taking multiple inputs in one line :

# n = input('enter numbers: ')
# arr = list(map(int, n.split()))
# print(arr)
# # taking list input:

# n = int(input('enter numbers: '))
# arr = list(map(int, input.split))

# take numbers in one line
# arr = list(map(int, input("Enter numbers separated by space: ").split()))

# # print the list
# print("Numbers:", arr)

# # print the sum
# print("Sum:", sum(arr))

# try: 
#     arr = list(map(int, input('enter numbers: ').split()))
#     print(arr)
# except ValueError:
#     print('invalid input, please enter int only')

# printing using class :
# class NumberInput:

#     def get_numbers(self):
#         try:
#             arr = list(map(int, input("Enter numbers: ").split()))
#             return arr
#         except ValueError:
#             print("Please enter only integers!")
#             return []

#     def display(self, arr):
#         if arr:
#             print("Numbers:", arr)
#             print("Sum:", sum(arr))


# obj = NumberInput()

# numbers = obj.get_numbers()
# obj.display(numbers)

