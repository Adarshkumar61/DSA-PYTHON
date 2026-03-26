def searchRange(nums, target):

    def findBound(isFirst):
        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                if isFirst:
                    right = mid - 1   # move left
                else:
                    left = mid + 1    # move right

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    return [findBound(True), findBound(False)]


print(searchRange([5,7,7,8,8,10], 8))