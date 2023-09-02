from random import randint
'''
MISSING NUMBER PROBLEM

OBJECTIVE: Given a stream of size n-1 consisting of integers from 1-n, with one number missing, find the missing number using o(log n) space.

ALGORITHM:
Easy. Just sum up each item in the stream, and subtract it from the sum of the first n numbers (n*(n-1)/2)
< k. 
1. Scan the stream
2. Define k-reduced bag "t". Initially, t is empty.
3. Whenever n[i] is scanned,
3.1: If n[i] is not in t, add n[i] to t.
3.2: If n[i] is in t, add n[i] to t.
3.3: If d == k, delete k values from t
'''

n = int(input("Stream size:"))    #n
stream = [i for i in range(1, n)]   #The stream. Currently contains all numbers
popped_element = stream.pop(randint(0,n-1))  #Pop some random element in the list
print("Popped element:{}".format(popped_element))
sum = 0
for stream_element in stream:
    sum += stream_element   #add stream element to sum

missing_element = int(n*(n-1)/2 - sum)  #Get missing element by subbing sum of first n elements and sum of stream

print("Missing element:{}".format(missing_element))
