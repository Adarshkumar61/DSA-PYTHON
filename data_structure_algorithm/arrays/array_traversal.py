# def buildarray(array):
#     n = len(array)
#     ans = [0] * n

#     for i in range(n):
#         ans[i] = array[array[i]]
#     return ans

# array = [0, 2, 1, 5, 3, 4]
# print(buildarray(array))


nums = [0,2,1,5,3,4]
ans =[]
for i in range(len(nums)):
    ans.append(nums[nums[i]])
print(ans)
#explanation: 



# See Every Single One
# nums = [0, 2, 1, 5, 3, 4]
#         0  1  2  3  4  5
# i = 0
# nums[0] = 0
# "value is 0"
# so open box 0
# nums[0] = 0
#           ↑
#        0 decided to go to box 0
# i = 1
# nums[1] = 2
# "value is 2"
# so open box 2       ← 2 decided this!
# nums[2] = 1
#           ↑
#        2 decided to go to box 2
# i = 2
# nums[2] = 1
# "value is 1"
# so open box 1       ← 1 decided this!
# nums[1] = 2
#           ↑
#        1 decided to go to box 1
# i = 3
# nums[3] = 5
# "value is 5"
# so open box 5       ← 5 decided this!
# nums[5] = 4
#           ↑
#        5 decided to go to box 5













"""nums = [0, 2, 1, 5, 3, 4]
        ↑  ↑  ↑  ↑  ↑  ↑
       b0 b1 b2 b3 b4 b5   ← these are BOXES

nums[0] = 0   ← value inside box 0
nums[1] = 2   ← value inside box 1
nums[2] = 1   ← value inside box 2
nums[3] = 5   ← value inside box 3
nums[4] = 3   ← value inside box 4
nums[5] = 4   ← value inside box 5

ms[ nums[i] ] →  use that value
                   as BOX NUMBER
                   open THAT box → get value inside that box
                   put that value in ans[i]

                   

whatever number is at nums[i]
THAT number becomes the box to open

the VALUE decides the next INDEX




"""



# array concation:
def getConcatenation(nums):

    n = len(nums)
    ans = [0] * (2*n)

    for i in range(n):
        ans[i] = nums[i] #first half
        ans[i+n] = nums[i] #second half

    return ans