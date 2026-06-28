# def movezero(arr):
#     slow = 0
#     for fast in range(len(arr)):
#         if arr[fast] != 0:
#             arr[slow], arr[fast] = arr[fast], arr[slow]
#             slow +=1
#     return arr
# arr = [1, 0, 3, 0, 6, 3, 0]
# print(movezero(arr))



# def movezeroes(arr):
#     k = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[k] = arr[i]
#             k+=1
#     while k< len(arr): # this fills the remaining positions with zeros
#         arr[k] = 0
#         k+=1
#     return arr


# arr = [1, 0, 3, 0, 6, 3, 0]
# r= movezeroes(arr)

# print(r)


# Explanation:


# i

# as:

# Scanner

# It checks every element.

# And:

# k

# as:

# Next empty position for a non-zero element





# def compact_sensor_reading(readings):
#     k = 0
#     for i in range(len(readings)):
#         if readings[i] !=0:
#             readings[k] = readings[i]
#             k+=1
#     while k < len(readings):
#         readings[k] = 0
#         k+=1
#     return readings

# readings = [1, 0, 3, 0, 6, 3, 0]
# r = compact_sensor_reading(readings)
# print(r)
# 🏆 Challenge:

# Now that you've mastered this pattern, don't do another LeetCode problem immediately.

# Instead, solve this real interview variation:

# readings = [120, -1, 90, -1, 60, 45, -1]

# Here:

# -1 = invalid reading.
# Move all valid readings to the front.
# Fill the remaining positions with -1.
# Do it in-place using O(1) extra space.

# def good_negative_entries_place(readings):
#     k = 0
#     for i in range(len(readings)):
#         if readings[i] != -1:
#             readings[k] = readings[i]
#             k +=1
#     while k < len(readings):
#         readings[k] = -1
#         k+=1
#     return readings

# readings = [120, -1, 90, -1, 60, 45, -1]
# r = good_negative_entries_place(readings)
# print(r)
