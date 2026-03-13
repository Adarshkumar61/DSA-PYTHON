palindrome means : Reads the SAME forwards and backwards

Two pointer is used when:

array is sorted
or
we need symmetric comparison
or
we need pair finding
or
we need window movement

Mental Model
Imagine:

Two people walking from both ends of a road
They check things and meet in middle

That is literally how this technique works.


wo Pointer Type 3
👉 Move Zeroes (Very Famous Problem)
iven array:

[0,1,0,3,12]

Move all zeroes to end
Maintain relative order of non-zero elements

Answer:

[1,3,12,0,0]
🧠 Thinking (Same Slow–Fast Logic)

Fast pointer → scans array

Slow pointer → position where next non-zero should go

So idea:

Whenever fast finds non-zero → put it at slow position.