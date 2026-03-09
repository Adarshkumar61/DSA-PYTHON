What is Time Complexity?

We can solve a problem using different logic and different codes. 
Time complexity basically helps to judge different codes and also helps to decide which code is better. 
In an interview, an interviewer generally judges a code by its time complexity.

perfect definition : time complexity of a particular code depends on the given input size, not on the machine used to run the code.

To represent the time complexity, we generally use the Big O notation

three rules, that we are going to follow while calculating the time complexity:

We will always calculate the time complexity for the worst-case scenario.
We will avoid including the constant terms.
We will also avoid the lower values.

to calculate the time complexity of the code, we need to first observe how the loops are working.

remeber always : Big-O keep highest power
example : 
``` 
for i in range(n):
    print(i)

for i in range(n):
    for j in range(n):
        print(i, j)
  here first time complexity: n
  2nd time complexity : n2 
  so n + n2  = as n2 is bigger so :
  final time complexity is :  n2