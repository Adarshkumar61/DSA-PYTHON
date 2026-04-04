# taking multiple inputs in one line :

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


# set name and show:
# multiple obj:
# class student:
#     def set_name(self, name):
#         self.name = name #+ ' kumar'

#     def show_name(self):
#         print(self.name + ' kumar')

# s1 = student()
# s2 = student()

# s1.set_name('adarsh'.title())
# s2.set_name('rahul')
# s1.show_name()
# s2.show_name()

#using constructor:
# class student:
#     def __init__(self, name , age):
#         self.name = name 
#         self.age = age
# s1 = student('adarsh', 19)
# print(s1.name)
# print(s1.age)

  
arr = [10, 20, 30]

for i in range(len(arr)):
    print(i)