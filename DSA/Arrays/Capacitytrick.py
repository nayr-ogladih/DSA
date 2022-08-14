def append(self, item):
        # 1) create a new array of bigger size
        array_data_type = ctypes.py_object * (self.size + 1)
        new_memory = array_data_type()

        # 2) copy old data
        for i in range(self.size):
            new_memory[i] = self.memory[i]

        # add the new element and increase size
        new_memory[self.size] = item
        self.size += 1

        # use the new memory and delete old one
        del self.memory
        self.memory = new_memory