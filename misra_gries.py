'''
MISRA-GRIES ALGORITHM

OBJECTIVE: Given a stream of size n, from a universe of m elements, estimate the "heavy hitters", i.e.
elements that occur more than n/k times, where k >= 2. The algorithm must work on a single pass, and 
due to the nature of streams, it must try to minimise space usage.

ALGORITHM:
We must produce a "k-reduced bag" t. A k-reduced bag is obtained by repeatedly removing k distinct
elements from the stream until it is no longer possible to do so. Thus, a k-reduced bag has a size of 
< k. 
1. Scan the stream
2. Define k-reduced bag "t". Initially, t is empty.
3. Whenever n[i] is scanned,
3.1: If n[i] is not in t, add n[i] to t.
3.2: If n[i] is in t, add n[i] to t.
3.3: If d == k, delete k values from t
'''
t = {}  #The k-reduced bag
k = int(input("K:"))    #K

while True:
    stream_element = input("Enter stream character, QUIT/quit to exit:")   #Current stream character
    #Exit condition
    if stream_element == "QUIT" or stream_element == "quit":
        break
    deleted_keys = []   #List of keys to delete if size of t == k
    try:
        t[stream_element] += 1  #Case 1, element already in t. Just increment size of that counter in t.
    except:
        t[stream_element] = 1   #Case 2, new element in t. Possible to have t == k, check for that.
        if len(t) == k:
            for key in list(t.keys()):
                t[key] -= 1
                if t[key] == 0: #Delete key if it's counter is 0
                    deleted_keys.append(key)
            for d in deleted_keys:  #Outside for loop to safely delete keys
                del t[d]
    
    print("Entered element:{}".format(stream_element))
    print("Current bag-\n{}".format(t))
    print("Deleted keys-\n{}".format(deleted_keys))


