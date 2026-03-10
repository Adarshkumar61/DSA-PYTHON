we don’t need spaces at all for  left aligned patterns mostly.

The Golden Rule 🔑
Every pattern = Outer loop (rows) × Inner loop (columns)
for i in range(rows):      # controls rows (top to bottom)
    for j in range(cols):  # controls columns (left to right)
        print(something)
    print()                # move to next line after each row


    The 3-Step Approach to ANY Pattern
Step 1: Count the rows → that's your outer loop
Step 2: Look at each row → what changes? (spaces, stars, numbers)
Step 3: Find the relationship between i (row) and j (col)