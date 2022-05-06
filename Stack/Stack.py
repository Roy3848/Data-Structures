# PUSH into a stack
# to add elements into the stack

# class for initializing stack
class Stack:
   def __init__(self):
       # initially an empty stack
       self.stack = []

   def add(self, dataval):
# Use list append method to add element
      if dataval not in self.stack:
         self.stack.append(dataval)
         return True
      else:
         return False
# Use peek to look at the top of the stack
   def peek(self):
       return self.stack[-1]

Stack2 = Stack()
Stack2.add(12)
Stack2.add(24)
Stack2.peek()
print(Stack2.peek())
Stack2.add(36)
Stack2.add(48)
print(Stack2.peek())

# POP into a stack
# to remove the elements from the stack

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use list pop method to remove element
    # but if we try to remove elements from the stack
    # then that is called as underflow
    def remove(self):
        # if stack has no elements left
        # then that condition is called as underflow
        if len(self.stack) <= 0:
            return "There are no more elements in the stack."
        # else perform this condition
        else:
            return self.stack.pop()


Stack1 = Stack()
Stack1.add(12)
Stack1.add(24)
Stack1.add(36)
Stack1.add(48)
print(Stack1.remove())
print(Stack1.remove())
