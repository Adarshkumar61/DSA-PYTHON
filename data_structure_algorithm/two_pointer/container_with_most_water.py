def max_water(arr):
    left = 0
    right = len(arr)-1

    max_water = 0
    while left < right:
        width = right - left
        height = min(arr[left], arr[right])
        water = width * height
        max_water = max(max_water, water)
        
        if arr[left] < arr[right]: # Move the pointer which has the smaller height
                                # cuz shorter height control the water level
            left +=1
        else:
            right -=1
    return max_water

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water(arr))


"""
Container With Most Water

We use two pointers:
left  -> start of array
right -> end of array

Area formula:
width = right - left
height = min(arr[left], arr[right])
area = width * height

Why move the smaller height pointer?
Because the smaller wall is the limiting wall.
If we move the taller wall, width becomes smaller but height limit
usually stays the same, so area will not improve.

So:
- if left height is smaller, move left forward
- else, move right backward

Time Complexity: O(n)
Space Complexity: O(1)
"""
"""Why start from 0 ?
Because:

Water can never be negative

Minimum possible water = 0

So we start with smallest safe value.
 What happens during loop

Each step we calculate:

water = width * height

Then we update:

max_water = max(max_water, water)

Meaning:

“If new water is bigger → store it.”"""
