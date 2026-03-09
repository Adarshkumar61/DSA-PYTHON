What is an Array?
An array is a linear data structure in which we store data and perform any operation, we can randomly access data in an array

array is a collection of similar types of elements (Homogeneous elements) that have contiguous memory locations i.e One after another.

If you need to access one or more than one element, the process of finding or performing operations on that element becomes very fast because your computer very well knows where the value is located in the memory.

fact : arrays are 0 indexed cause its simplifies the computation
but it acts an extra step of un necessary action of (n-1) for each access 

Arrays can store numbers, strings, boolean values, characters, objects, etc.
 But once you define the type of values that your array will store, all its elements must be of that same type.
  You cannot “insert” different types of data in a single array.

Arrays cannot store heterogeneous data.

Syntax : Data_type  array_name  [Array_size] ;

Summary of the Arrays:

Memory is allocated instantly: After the array is created the memory is allocated instantly and the array is empty until you assign the values.

Elements are located in contiguous manner: So the elements can be accessed very efficiently (direct access, O(1) = constant time) using it’s index values.

Arrays are powerful data structures: The type of elements and the size of the array are fixed and defined when you create it. Arrays store elements of the same type (homogeneous).

Inserting elements: Reach to the end of the array and insert the element. The insertion at the end of the array.
 Insertion takes constant time O(1).
  We can also insert the elements in the middle or the start of the array but it's a bit of a complex process.
Removing elements: Reach to the index and remove the element. The removal operation takes constant time O(1).


STRING :

Strings are like a series of characters stored in a specific order.
Each character in a string is assigned an index, starting from 0. This means the first character is at index 0, the second character at index 1, and so on.

To determine the length of a string, we can use the size or length function. 