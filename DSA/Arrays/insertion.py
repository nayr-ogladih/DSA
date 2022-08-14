"""shifting to the right by one"""



def insert(self, idx, item):
    assert 0 <= idx < self.size

    if self.size == self._capacity:

        self.expand_capacity()

    for p in range(self.size - 1, idx - 1, -1):
        self.memory[p + 1] = self.memory[p]
    self.memory[idx] = item
    self.size += 1