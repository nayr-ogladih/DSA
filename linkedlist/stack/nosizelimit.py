# stack is a data structure that stores items in a "Last-in/First-out" manner. (LIFO)

#create stack
#push
#pop
#peek                                CustomStack()
#isEmpty
#isFull
#deleteStack

#create stack using python list
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    #isEmpty method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #push method
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    #pop method
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    #peek method
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]

    #isFull method
    def delete(self):
        self.list = None













customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
print(customStack)