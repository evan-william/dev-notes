def linear_Minsearch(H, min):
    for i in range(len(H) - 1, -1, -1):
        if H[i] == min:
            return i
    
"""
1. range() Function Overview
The range() function generates a sequence of numbers. Its typical usage is:

range(start, stop, step)
Where:

start: The first number in the sequence (inclusive).
stop: The end point of the sequence (exclusive).
step: The difference between each pair of consecutive numbers.

2. Breaking Down range(len(H) - 1, -1, -1)
a. len(H) - 1 (Start)
len(H) gives the total number of elements in the list H.
len(H) - 1 gives the last index of the list because Python indexing starts from 0.

Example:
H = [10, 20, 30, 40, 50]
len(H)          # Output: 5
len(H) - 1      # Output: 4 (last index)
So, if H has 5 elements, len(H) - 1 is 4.

b. -1 (Stop)
This is the exclusive stop point for the sequence.
Since it’s exclusive, the loop will stop before reaching -1.
This setup allows the loop to reach index 0 but not go further.

c. -1 (Step)
The -1 step means the loop will move backwards one step at a time.
It decrements the index by 1 in each iteration.
In essence:

The loop will start at the last index (len(H) - 1), move backwards to the first index (0), and then stop.
"""