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

n = 5
for i in range(1, n+1):
    space = n -i
    star = 2 * i -1
    for j in range(space):
        print(" ", end= "")
    for j in range(star):
        print("*", end= "")
    print()
#for lower traingle :
for i in range(1, n +1):
    space = i
    star = 2*(n-i)-1
    for j in range(space):
        print(" ", end= "")
    for j in range(star):
        print("*", end= "")
    print()