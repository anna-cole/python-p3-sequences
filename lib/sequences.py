#!/usr/bin/env python3

# Fibonacci sequence is a sequence in which an element is the sum of its 2 previous elements.
# Use negative indexing to directly access the last two elements of the list: list[-1], list[-2].
# Append to the list the sum of the last 2 elements of the list using the append() method.
# Use an iterator to perform this action (loop) until the length is reached.
# Use conditional statements (if) to append 0 and 1 to the list. If the length is higher than 2, do the looping. 

def print_fibonacci(length):
    list = []
    if length > 0:
        list.append(0)
    if length >= 2:
        list.append(1)
        for i in range(2, length):
            list.append(list[-1] + list[-2])
    
    print(list)
       
print_fibonacci(9)