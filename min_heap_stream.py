'''
MIN HEAP ALGORITHM

OBJECTIVE: Based on weekplan Streaming 1, question 2 (find k largest elements in an array using streaming model)
I'm solving this question here using a min-heap

ALGORITHM:
We make use of a min-heap to get the n smallest elements of a stream.
For a stream, we will have to restrict the size of the heap to the number of elements we want.

How we modify min-heaps for this purpose:
1. Define a list min_heap
2. Add an element of the array to end of the min_heap list
3. HeapifyUp()
4. If heap size > k, delete elements beyond index k
4.1 During insertion, also ensure the left child < the right child
5. To get the n smallest elements:
5.1 Pop root node
5.2 HeapifyDown()
'''
from time import sleep
from random import randint

class MinHeapStream():
    def __init__(self,k) -> None:
        self.k = k
        self.min_heap = []  #The heap list
    
    def peek(self):
        #Return root (minimum element)
        try:
            return self.min_heap[0]
        except Exception as e:
            print("Exception in peeking:{}".format(e))
    
    def get_left_child(self,index):
        #Return left child of the given index
        try:
            return self.min_heap[self.get_left_child_index(index)]
        except:
            return None
    
    def has_left_child(self,index):
        #Check if there is a left child
        return self.get_left_child_index(index) < len(self.min_heap) - 1
    
    def get_left_child_index(self, index):
        #Get the index of the left child
        return 2*index+1
    
    def get_right_child(self,index):
        #Return right child of the given index
        try:
            return self.min_heap[self.get_right_child_index(index)]
        except:
            return None
    
    def has_right_child(self,index):
        #Check if there is a right child
        return self.get_right_child_index(index) < len(self.min_heap) - 1
    
    def get_right_child_index(self, index):
        #Get index of the right child
        return 2*index+2
    
    def get_parent_index(self, index):
        #Get index of the parent of a given node
        return int((index - 1)/2)

    def has_parent(self,index):
        #Check if parent exists
        return self.get_parent_index(index = index) >= 0
    
    def get_parent(self,index):
        #Get value of the parent
        if self.has_parent(index=index):
            return self.min_heap[self.get_parent_index(index = index)]
        else:
            return None
        
    
    def poll(self):
        #Get parent (minimum value), and remove it and heapify down
        try:
            return_item = self.min_heap[0]
            self.min_heap[0] = self.min_heap[-1]
            self.min_heap = self.min_heap[1:]
            self.heapify_down()
            return return_item
        except Exception as e:
            print("Exception in polling:{}".format(e))

    def insert(self, element):
        #Insert a new element to the heap. Restrict size oh heap to k.
        try:
            self.min_heap.append(element)
            self.heapify_up()
            self.min_heap = self.min_heap[0:k]
        except Exception as e:
            print("Exception in insertion:{}".format(e))
    
    def heapify_up(self):
        #Used in inserting, heapify up from the last appended element
        current_index = len(self.min_heap)-1
        while self.has_parent(current_index) and self.get_parent(current_index) > self.min_heap[current_index]:
            self.min_heap[current_index], self.min_heap[self.get_parent_index(current_index)] = self.min_heap[self.get_parent_index(current_index)], self.min_heap[current_index]
            current_index = self.get_parent_index(current_index)
        #We must ensure elft child is smaller than right
        if len(self.min_heap) > 2:
            if self.min_heap[-1] < self.min_heap[-2]:
                self.min_heap[-2], self.min_heap[-1] = self.min_heap[-1], self.min_heap[-2]
    
    def heapify_down(self):
        #Used in polling, heapify down from the root
        current_index = 0
        while(self.has_left_child(current_index)):
            smaller_child_index = self.get_left_child_index(current_index)
            if self.has_right_child:

                if self.get_right_child(index=current_index) < self.get_left_child(index= current_index):
                    smaller_child_index = self.get_right_child_index(current_index)
            
            if self.min_heap[current_index] > self.min_heap[smaller_child_index]:
                self.min_heap[current_index], self.min_heap[smaller_child_index] = self.min_heap[smaller_child_index], self.min_heap[current_index]

            else:
                return None
    


heap = MinHeapStream(5)    #Create heap
k = 3  #Number of elements to get
stream_size = randint(5,10)    #Get a random stream size
print("Stream size:{}".format(stream_size))

for i in range(stream_size):
    random_stream_element = randint(1,1000)
    print("Random stream element: {}".format(random_stream_element))
    heap.insert(random_stream_element)
    print(heap.min_heap)
    sleep(2)


#Get k smallest
for i in range(k):
    print(heap.poll())
