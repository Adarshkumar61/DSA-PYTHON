def concat(arr):
    n = len(arr)
    ans = [0]* (2*n)

    for i in range(n):
        ans[i] = arr[i]
        ans[i+n] = arr[i]
    return ans
arr = [1, 2, 3]
print(concat(arr))
# explaination : 
"""teration 1 → i = 0
Line 1
ans[i] = arr[i]

So:

ans[0] = arr[0] = 1

Array now:

[1, 0, 0, 0, 0, 0]
Line 2
ans[i+n] = arr[i]

Important:

i+n = 0 + 3 = 3

So:

ans[3] = arr[0] = 1

Array becomes:

[1, 0, 0, 1, 0, 0]
🔎 Iteration 2 → i = 1
First line
ans[1] = arr[1] = 2

Array:

[1, 2, 0, 1, 0, 0]
Second line
i+n = 1 + 3 = 4

So:

ans[4] = arr[1] = 2

Array:

[1, 2, 0, 1, 2, 0]
🔎 Iteration 3 → i = 2
First line
ans[2] = arr[2] = 3

Array:

[1, 2, 3, 1, 2, 0]
Second line
i+n = 2 + 3 = 5

So:

ans[5] = arr[2] = 3

Final array:

[1, 2, 3, 1, 2, 3]
⭐ Final Output
[1, 2, 3, 1, 2, 3]"""