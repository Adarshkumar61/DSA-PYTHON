# Optimal Thinking

# Algorithm:

# 1️⃣ Start from last digit
# 2️⃣ If digit < 9 → just add 1 and return
# 3️⃣ If digit == 9 → make it 0 and continue
# 4️⃣ If all digits become 0 → insert 1 at front

def plusone(nums):
    for i in range(len(nums) -1, -1, -1):
        if nums[i] < 9:
            nums[i]+=1
            return nums
        nums[i] = 0
    return [1] + nums

arr = [1,2,3]
print(plusone(arr))

