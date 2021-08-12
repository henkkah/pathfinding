# (Binary) Min Heap implementation
class MinHeap:
    
    def __init__(self):
        self.array = [None]     # index 0 in array is not used in this min heap implementation
        self.last = 0           # keeps track of last index in array
    
    # helper method for debugging
    def get_heap(self):
        return (self.array, self.last)
    
    # O(1)
    def left_child_index(self, i):
        if 2*i > self.last:
            return None
        else:
            return 2*i
    
    # O(1)
    def right_child_index(self, i):
        if 2*i+1 > self.last:
            return None
        else:
            return 2*i+1
    
    # O(1)
    def parent_index(self, i):
        if i//2 > self.last:
            return None
        else:
            return i//2
    
    # O(1)
    def is_empty(self):
        return self.last == 0
    
    # O(1)
    def get_min(self):
        if self.is_empty():
            return None
        else:
            return self.array[1]
    
    # O(log n)
    def insert(self, x):
        self.array.append(x)
        self.last += 1
        i = self.last
        while i > 1 and x < self.array[self.parent_index(i)]:
            self.array[i] = self.array[self.parent_index(i)]
            i = self.parent_index(i)
        self.array[i] = x
    
    # helper method for pop_min()
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
    
    # O(log n)
    def pop_min(self):
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



# Test
from random import randint
array = [2, 7, 3, 7, 9, 15, 8, 12, 8, 13]
heap = MinHeap()
for _ in range(10):
    one = array[randint(0, len(array)-1)]
    array.remove(one)
    heap.insert(one)
    print("Heap:", heap.get_heap()[0])
    print("Last:", heap.get_heap()[1])
    print("Min:", heap.get_min())
    print()
print("--------------------------------------------------")
for _ in range(10):
    print("Popped:", heap.pop_min())
    print("Heap:", heap.get_heap()[0])
    print("Last:", heap.get_heap()[1])
    print()
