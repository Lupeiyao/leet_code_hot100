


class MedianFinder:

    def swap(self, heap, i, j):
        tmp = heap[i]
        heap[i] = heap[j]
        heap[j] = tmp

    def buildMaxTreeUp(self, i):
        father = (i - 1) // 2
        if father >= 0 and self.max_heap[i] > self.max_heap[father]:
            self.swap(self.max_heap, i, father)
            self.buildMaxTreeUp(father)


    def buildMinTreeUp(self, i):
        father = (i - 1) // 2
        if father >= 0 and self.min_heap[i] < self.min_heap[father]:
            self.swap(self.min_heap, i, father)
            self.buildMinTreeUp(father)

    def buildMaxTreeDown(self, i):
        l = i * 2 + 1
        r = i * 2 + 2
        max_idx = i
        if l < self.max_size and self.max_heap[l] > self.max_heap[max_idx]:
            max_idx = l
        if r < self.max_size and self.max_heap[r] > self.max_heap[max_idx]:
            max_idx = r 
        if i != max_idx:
            self.swap(self.max_heap, i, max_idx)
            self.buildMaxTreeDown(max_idx)

    def buildMinTreeDown(self, i):
        l = i * 2 + 1
        r = i * 2 + 2
        min_idx = i
        if l < self.min_size and self.min_heap[l] < self.min_heap[min_idx]:
            min_idx = l
        if r < self.min_size and self.min_heap[r] < self.min_heap[min_idx]:
            min_idx = r 
        if i != min_idx:
            self.swap(self.min_heap, i, min_idx)
            self.buildMinTreeDown(min_idx)

    def __init__(self):
        self.min_heap = []
        self.min_size = 0
        self.max_heap = []
        self.max_size = 0
        

    def addNum(self, num: int) -> None:
        if self.max_size > self.min_size:
            self.min_size += 1
            if num >= self.max_heap[0]:
                self.min_heap.append(num)
                self.buildMinTreeUp(self.min_size - 1)
            else:
                self.min_heap.append(self.max_heap[0])
                self.buildMinTreeUp(self.min_size - 1)
                self.max_heap[0] = num
                self.buildMaxTreeDown(0)
        else:
            self.max_size += 1
            if self.max_size == 1:
                self.max_heap.append(num)
            elif num < self.min_heap[0]:
                self.max_heap.append(num)
                self.buildMaxTreeUp(self.max_size - 1)
            else:
                self.max_heap.append(self.min_heap[0])
                self.buildMaxTreeUp(self.max_size - 1)
                self.min_heap[0] = num
                self.buildMinTreeDown(0)


    def findMedian(self) -> float:
        if self.max_size > self.min_size:
            return self.max_heap[0]
        else:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        
