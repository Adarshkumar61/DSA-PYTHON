# row = 5
# col = 5
# for i in range(row):
#     for j in range(col):
#         print("*", end= '')
#     print()
#     #print():
# #moves the cursor to the next row.
# #Without it everything prints in one line.

# # triangle pattern:
# def traingle(row):
#     for i in range(1, row):
#         for j in range(i):
#             print("x", end = '')
         
#         print()
# row = 5
# traingle(row)


# ques = 1
#        12
#        123
#        1234
#        12345


# def traingle_no(row):
#     for i in range(1, row):
#         for j in range(1, i+1):
#             print(j , end= "")
#         print()
# row = 5
# traingle_no(row)


# for i in range(1, 6):
#     for j in range(i):
#         print(i, end = '')
#     print()

# # reverse traingle pattern:
# def reverse_traingle(row):
#     for i in range(1, row):
#         for j in range(row -1):
#             print("x", end= "")
#         print()
# row = 5
# reverse_traingle()

#right traingle pattern:


# row = 5
# for i in range(1, row):
#     for j in range(row - i):
#         print(" ", end= '')
#     for j in range(i):
#         print("x", end= "")
#     print()

# for i in range(1, n+1):

#     # print spaces
#     for j in range(n - i):
#         print(" ", end="")

#     # print stars
#     for j in range(i):
#         print("x", end="")

#     print()
# output:
    #     x
    #    xx
    #   xxx
    #  xxxx 
    # xxxxx


# row = 5
# for i in range(1, row +1):
#     for j in range(row - i+1):
#         print("x", end = "")
#     print()
#output:
# xxxxx
# xxxx
# xxx
# xx
# x

# row = 5

# for i in range(1, row+1):
#     for j in range(row - i):
#         print(" ", end= "")
#     for j in range(i):
#         print("x", end = "")
#     print()
    #output:
    #     x
    #    xx
    #   xxx
    #  xxxx 
    # xxxxx

# row = 5
# for i in range(1, row+1):
#     spaces = row -i
#     stars = 2*i -1
#     for j in range(spaces):
#         print(" ", end = "")
#     for j in range(stars):
#         print("*", end= "")
#     print()
#     output :
#       *
#      ***
#     *****
#    *******
#   *********

# row = 5
# for i in range(1, row+1):
#     space = i-1
#     star = 2*(row-i)+1
#     for j in range(space):
#         print(" ", end= "")
#     for j in range(star):
#         print("*", end= "")
#     print()
    # output :
    # *********
    #  *******
    #   *****
    #    ***
    #     *


# pattern :
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# solution :

# n = 5

# Upper pyramid
# for i in range(1, n+1):

#     spaces = n - i
#     stars = 2*i - 1

#     for j in range(spaces):
#         print(" ", end="")

#     for j in range(stars):
#         print("*", end="")

#     print()

# n =5
# # Lower pyramid
# for i in range(1, n):

#     spaces = i
#     stars = 2*(n-i) - 1

#     for j in range(spaces):
#         print(" ", end="")

#     for j in range(stars):
#         print("*", end="")

#     print()

# output:
# *********
#  *******
#   *****
#    ***
#     *


# for upper pyramid :

# n = 5
# for i in range(1, n+1):
#     space = n -i
#     star = 2 * i -1
#     for j in range(space):
#         print(" ", end= "")
#     for j in range(star):
#         print("*", end= "")
#     print()
# #for lower traingle :
# for i in range(1, n +1):
#     space = i
#     star = 2*(n-i)-1
#     for j in range(space):
#         print(" ", end= "")
#     for j in range(star):
#         print("*", end= "")
#     print()



# question:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# answer :

# right angle then opposite right angle:
n = 7
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end= "")
#     print()
# for i in range(1, n):
#     for j in range(n-i):
#         print("*", end= "")
#     print()


#question :

# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1
# solution:
# n = 5
# for i in range(1, n+1):          # rows
#     for j in range(1, i+1):      # numbers = i (increasing)
#         if (i + j) % 2 == 0:     # even → 1
#             print(1, end=" ")
#         else:                     # odd → 0
#             print(0, end=" ")
#     print()


# question:
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

# approaching by dividing in 2 :
# n = 5
# for i in range(1, n+1):

#     # left numbers
#     for j in range(1, i+1):
#         print(j, end="")

#     for j in range(2*(n -i)):
#         print(" ", end= "")
#     for j in range(i, 0, -1):
#         print( j, end= "")
        
#     print()

# question:
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

# n = 5
# num = 1
# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end = "")
#         num +=1
#     print()


# question : repeating of row no:
# 1
# 22
# 333
# 4444
# 55555
# n = 5
# for i in range(1, n +1):
#     for j in range(1,i+1, -1):
#         print(j, end= "")
#     print()


# question: 
# 1
# 21
# 321
# 4321
# 54321
# n =6 
# for i in range(1, n):
#     for j in range(n -i):
#         print("", end= "")# left aligned do " " for right aligned
#     # for j in range(1,i+1): # if no is ascending 
#     for j in range(i , 0, -1): # if decreasing 
#         print(j, end= "")
#     print()
# n = 6
# for i in range(1, n):
#     for j in range(n -i):
#         print("", end = "") # change the space for direction
#     for j in range(1, i  +1):
#         print(j, end = "")
#     print()



# 1
# 23
# 456
# 78910
# 1112131415

n = 5
for i in range(1, n +1):
    space = n -i
    for j in range(space):
        print("", end= "")
    for j in range(1, i+1):
        print(i, end= "")
    print()