# (Binary) Min Heap implementation
class MinHeap:
    
    def __init__(self):
        self.array = [None]     # index 0 in array is not used in this min heap implementation
        self.last = 0           # keeps track of last index in array
    
    # helper method for debugging
    def get_heap(self):
        return (self.array, self.last)
    
    # get index of left child of node at index i
    def left_child_index(self, i):      # O(1)
        if 2*i > self.last:
            return None
        else:
            return 2*i
    
    # get index of right child of node at index i
    def right_child_index(self, i):     # O(1)
        if 2*i+1 > self.last:
            return None
        else:
            return 2*i+1
    
    # get index of parent of node at index i
    def parent_index(self, i):          # O(1)
        if i//2 > self.last:
            return None
        else:
            return i//2
    
    # check whether heap is empty
    def is_empty(self):                 # O(1)
        return self.last == 0
    
    # get node with minimum value from heap - from root (node is NOT removed from heap)
    def get_min(self):                  # O(1)
        if self.is_empty():
            return None
        else:
            return self.array[1]
    
    # insert node x to heap (and heapify heap to satisfy min heap property)
    def insert(self, x):                # O(log n)
        self.array.append(x)
        self.last += 1
        i = self.last
        while i > 1 and x < self.array[self.parent_index(i)]:
            self.array[i] = self.array[self.parent_index(i)]
            i = self.parent_index(i)
        self.array[i] = x
    
    # helper method for pop_min() - pushes node at index i down until min heap property is satisfied
    def push_down(self, i):
        # no children
        if self.left_child_index(i) == None:
            return
        # only left child
        elif self.left_child_index(i) == self.last:
            smaller_child_index = self.left_child_index(i)
        # both left and right child
        else:
            if self.array[self.left_child_index(i)] < self.array[self.right_child_index(i)]:
                smaller_child_index = self.left_child_index(i)
            else:
                smaller_child_index = self.right_child_index(i)
        if self.array[i] > self.array[smaller_child_index]:
            # swap
            temp = self.array[smaller_child_index]
            self.array[smaller_child_index] = self.array[i]
            self.array[i] = temp
            # recursive call
            self.push_down(smaller_child_index)
    
    # pop node with minimum value from heap - from root (node IS removed from heap) and heapify heap to satisfy min heap property
    def pop_min(self):                  # O(log n)
        if self.is_empty():
            return None
        else:
            result = self.array[1]
            if self.last == 1:
                self.array.pop()
            else:
                self.array[1] = self.array.pop()
            self.last -= 1
            self.push_down(1)
            return result


