from random import randint
'''
ALGORITHM R

OBJECTIVE: To produce a random sample, without replacement, of k items from a population of unknown size n.

ALGORITHM: 
>Initialise a list of size k containing the first k items of a stream.
> For every subsequent element at index i, generate a random number n from 1 to i. If n in range of 1,k, k[n] = element at i.
> Return after stream ends.
>This is the simplest sampling algorithm, and is quite slow.
'''

k = int(input("Enter reservoir size:")) #Reservoir size
reservoir = []

while True:
    stream_element = input("Enter stream character, QUIT/quit to exit:")   #Current stream character
    #Exit condition
    if stream_element == "QUIT" or stream_element == "quit":
        break

    #Initial case, while reservoir is not full
    if len(reservoir) < k:
        reservoir.append(stream_element)
    
    #Normal case, reservoir is full
    else:
        n = randint(1,len(reservoir))
        if n <= k:
            reservoir[n-1] = stream_element
    
        print("Element {} sampled at position {}.".format(stream_element,n-1))

    print("Current reservoir-\n{}".format(reservoir))