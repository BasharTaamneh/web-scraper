

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise Exception("This stack is empty")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.top == None:
            raise Exception("This stack is empty")
        else:
            return self.top.value

    def max_stack(self):
        current = self.top
        if(self.top == None):
            return "stack is empty"
        else:
            # Initializing max with head node data
            max = self.top.value
            while(current != None):
                # If current node's data is greater than max
                # Then, replace value of max with current node's data
                if(max < current.value):
                    max = current.value
                current = current.next
            return  max

    def is_empty(self):
        return self.top is None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(15)
stack.push(3)
stack.push(40)
stack.push(41)
print(stack.max_stack())
