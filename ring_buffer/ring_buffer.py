class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.last_index = 0

    def append(self, item):
        if self.capacity > len(self.storage):
            self.storage.append(item)
        else:
            self.storage[self.last_index] = item
            self.last_index = (self.last_index + 1) % self.capacity

    def get(self):
        return self.storage
