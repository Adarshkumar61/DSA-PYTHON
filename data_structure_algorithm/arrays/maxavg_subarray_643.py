def max_average_subarray(nums, k):
    #sum of first k elements
    summ = sum(nums[:k])
    #assuming first sum is max sum
    max_sum = summ

    for i in range(k, len(nums)):
 
        #removing left element and and subtracting from summ
        summ -= nums[i-k]
        # adding one right element and adding to summ
        summ+= nums[i]

        if summ > max_sum:
            max_sum = summ
    return max_sum / float(k)

nums = [1,12,-5,-6,50,3]
k = 3
r = max_average_subarray(nums, k)
print(r)