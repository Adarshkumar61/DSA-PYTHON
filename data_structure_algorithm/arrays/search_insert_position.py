# def search_insert_position(nums, target):
#     left = nums[0]
#     right = len(nums) -1

#     while left <= right:
#         mid = (left + right) //2

#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left +=1
#         else:
#             right +=1
#     return left

# arr = [1,3,5,6]
# target = 6
# print(search_insert_position(arr, target))

def searchInsert(nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

arr = [1,3,5,6]
target = 5
print(searchInsert(arr, target))