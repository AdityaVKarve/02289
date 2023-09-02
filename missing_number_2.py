from random import randint
from math import sqrt
'''
MISSING NUMBER PROBLEM

OBJECTIVE: Given a stream of size n-2 consisting of integers from 1-n, with 2 numbers missing, find the missing number using o(log n) space.

ALGORITHM:
1. Given n. Find sum of n numbers (n.(n+1)/2) and sum of squares of n numbers (n.(n+1).(2n+1)/6)
2. Now, sum of n - sum of stream is x + y. Call it A. sum of squares of n - sum of squares of stream is x^2 + y^2. Call it B.
3. Now, A^2 = B + 2xy. Find 2xy as A^2 - B. Let 2xy be C.
4. Now, get (x-y)^2 as  B - C.
5. Thus, get x-y. Call it D.
6. Now, 2x = A+D. Get x and get y from here.
'''

n = int(input("Stream size:"))    #n
stream = [i for i in range(1, n+1)]   #The stream. Currently contains all numbers
popped_element_1 = stream.pop(randint(0,n-1))  #Pop some random element in the list
print(len(stream))
popped_element_2 = stream.pop(randint(0,n-2))
print("Popped elements:{}, {}".format(popped_element_1, popped_element_2))

stream_sum = 0 #Sum of stream
stream_sum_squared = 0 #Sum of squares of stream

total_sum = n*(n+1)/2   #Total sum of n integers
total_sum_squares = n*(n+1)*(2*n+1)/6 #Total sum of squares
for stream_element in stream:  
    #Process stream
    stream_sum += stream_element    
    stream_sum_squared += stream_element**2

A = total_sum - stream_sum
B = total_sum_squares - stream_sum_squared
C = A**2 - B
D = sqrt(B-C)

number_1 = (A+D)/2
number_2 = A-number_1

print("Missing elements:{},{}".format(int(number_1),int(number_2)))


