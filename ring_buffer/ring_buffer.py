class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        # If capacity is full overwrite the oldest element with the new element
        self.current += 1
        if self.capacity == self.current:
            self.current = 0

    def get(self):
        newArr = [i for i in self.storage if i != None]
        return newArr
        # return [i for i in self.storage]


# From Readme
buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())  # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())  # should return ['d', 'e', 'f']
