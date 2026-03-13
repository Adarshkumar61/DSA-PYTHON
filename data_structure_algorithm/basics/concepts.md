loop concept :
Golden Rule (VERY IMPORTANT)

Always ask:

👉 Loop variable is index OR value ?

If loop is:
for i in range(len(arr))

Then use:

arr[i]
If loop is:
for element in arr

Then use:

element

len:
len() Function in Python
✅ Meaning

len() means:

👉 Find how many elements are inside something.

It can be used on:

list

string

tuple

dictionary

set



Range :

range() creates a sequence of numbers.

Loop uses this sequence to run.

✅ Example 1
for i in range(5):
    print(i)

Output:

0
1
2
3
4
⭐ Why not 5 ?

Because:

👉 range(5) means:

start = 0 (default)
end = 5 (not included)

So numbers are:

0 → 4
✅ Example 2 (Start and End)
for i in range(2, 6):
    print(i)

Output:

2
3
4
5

Meaning:

start = 2
end = 6 (not included)
✅ Example 3 (Step / Jump)
for i in range(0, 10, 2):
    print(i)

Output:

0
2
4
6
8

Step = 2 → jump by 2.

🔥 Most Important DSA Use

We combine len + range

arr = [10, 20, 30]

for i in range(len(arr)):
    print(arr[i])
How this works internally
len(arr) = 3

range(3) → 0,1,2

Loop becomes:

i = 0 → arr[0] → 10
i = 1 → arr[1] → 20
i = 2 → arr[2] → 30

This is Array Traversal using index.
