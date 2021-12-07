"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.

    Returns true if the last element in the stack is not None
    """
    def isFull(self):
        if self.stack[-1] is None:
            return False
        else:
            return True

    """
    isEmpty function to check if the stack is empty.

    Returns true if the first element in the stack is None
    """
    def isEmpty(self):
        if self.stack[0] is None:
            return True
        else:
            return False

    """
    resize function to resize the stack by doubling its size.

    Assumes that resize method will only ever be called when stack is full.
    Uses self.numElems to determine how many new spaces should be added and
    sets these values to None.

    There is no return value.
    """
    def resize(self):
        self.stack = [self.stack[x] if x < self.numElems else None \
        for x in range(2*self.numElems)]
        return

    """
    push function to push a value onto the stack.

    Uses self.top to identify where val should be placed in stack and then
    adjusts values of self.numElems and self.top

    Resizes stack if it is full.

    There is no return value.
    """
    def push(self, val):
        # Resize stack if it is full
        if self.isFull():
            self.resize()
        # Otherwise, push val to the top
        self.stack[self.top + 1] = val
        self.numElems += 1
        self.top += 1
        return

    """
    pop function to pop the value off the top of the stack.

    Uses self.top to return value currently on top of stack. Decreases value
    of self.top and self.numElems by 1, resets previous top value to None, and
    returns previous top value.
    """
    def pop(self):
        # Return none if stack is empty
        if self.isEmpty():
            return None
        top_elem = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        self.numElems -= 1
        return top_elem
