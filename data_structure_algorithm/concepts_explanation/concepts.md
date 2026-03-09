.split() 
split only works on strings
when we will use split :
 Use .split() when multiple values are written on the same line.

Example input:

10 20 30 40

Code:

arr = input().split()
print(arr)

Output:

['10','20','30','40']

Self :

  self is important because :

It allows an object to store and access its own data.

 Real World Example

Class:

Student

Objects:

Adarsh
Rahul
Riya

Each student has different:

name
age
marks

self helps store data for each student separately.

9. When You Use self

You use self when:

1️⃣ Accessing object variables

self.name
self.age

2️⃣ Calling another method inside class

self.display()

3️⃣ Storing values inside object

self.speed = speed



10. Important Rule

Inside a class method:

first parameter must be self

Example:

def method(self, x, y):


      __init__ constructor:
       

       