'''
MAX HEAP ALGORITHM

OBJECTIVE: Based on weekplan Streaming 1, question 1 (find k largest elements in an array using RAM model)
I'm solving this question here using a max-heap

ALGORITHM:
We make use of a min-heap to get the n smallest elements of an array.

How a min-heap works:
1. Define a list min_heap
2. Add an element of the array to end of the min_heap list
3. HeapifyUp()
4. To get the n smallest elements:
4.1 Pop root node
4.2 HeapifyDown()
'''

class MinHeap():
    def __init__(self) -> None:
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
            return self.min_heap[self.get_left_child_index]
        except:
            return None
    
    def has_left_child(self,index):
        #Check if there is a left child
        return self.get_left_child_index < len(self.min_heap) - 1
    
    def get_left_child_index(self, index):
        #Get the index of the left child
        return 2*index+1
    
    def get_right_child(self,index):
        #Return right child of the given index
        try:
            return self.min_heap[self.get_right_child_index]
        except:
            return None
    
    def has_right_child(self,index):
        #Check if there is a right child
        return self.get_right_child_index < len(self.min_heap) - 1
    
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
        #Insert a new element to the heap
        try:
            self.min_heap.append(element)
            self.heapify_up()
        except Exception as e:
            print("Exception in insertion:{}".format(e))
    
    def heapify_up(self):
        #Used in inserting, heapify up from the last appended element
        current_index = len(self.min_heap)-1
        while self.has_parent(current_index) and self.get_parent(current_index) > self.min_heap[current_index]:
            self.min_heap[current_index], self.min_heap[self.get_parent_index(current_index)] = self.min_heap[self.get_parent_index(current_index)], self.min_heap[current_index]
            current_index = self.get_parent_index(current_index)
    
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
                return 
    

array = [1,7,6,2,1,6,9,10,20,102,54,-1] #array to be inserted (RAM model)
heap = MinHeap()    #Create heap
k = 5   #Number of elements to get

for e in array:
    #Insert array elements
    heap.insert(e)

#Get k smallest
for i in range(k):
    print(heap.poll())
