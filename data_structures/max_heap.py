class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)  # add item to the end of the heap
            self.__floatUp(len(self.heap) - 1)  # change its position based on it's value

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):  # show first (biggest) item in the heap
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)  # swap first and last element
            max = self.heap.pop()  # pop last (biggest) element from heap
            self.__bubleDown(1)  # reorder the heap based on values, when new value goes to top
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return  # no reordering since there is only one value here
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)  # here the parent is still the index value that has been swapped up

    def __bubleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        # if there is a left child and it is larger than the current max, swap 'em
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubleDown(largest)  # now check it for new biggest value

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

m = MaxHeap([95, 3, 21])
m.push(10)
print(m.heap) # [0, 95, 10, 21, 3]