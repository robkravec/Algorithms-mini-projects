"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.

    Returns true if the rear value in the queue is not None
    """
    def isFull(self):
        if self.queue[self.rear] is None:
            return False
        else:
            return True

    """
    isEmpty function to check if the queue is empty.

    Returns true if the front value in the queue is None
    """
    def isEmpty(self):
        if self.queue[self.front] is None:
            return True
        else:
            return False

    """
    resize function to resize the stack by doubling its size.

    Assumes that resize method will only ever be called when queue is full.
    Uses self.numElems to determine how many new spaces should be added and
    sets these values to None.

    Unwraps queue by setting front and rear indices.

    There is no return value.
    """
    def resize(self):
        self.queue = [self.queue[(self.front + x) % len(self.queue)] \
        if x < self.numElems else None for x in range(2*self.numElems)]
        self.front = 0
        self.rear = self.numElems
        return

    """
    push function to push a value into the rear of the queue.

    Adds val to rear position, increments numElems, and increments value of 
    rear. Wraps rear index, if necessary.

    Resizes queue if it is full.

    There is no return value.
    """
    def push(self, val):
        # Resize queue if it is full
        if self.isFull():
            self.resize()
        # Otherwise, push val to the rear
        self.queue[self.rear] = val
        self.numElems += 1
        self.rear = (self.rear + 1) % len(self.queue)
        return

    """
    pop function to pop the value from the front of the queue.

    Uses self.front to return value currently on top of stack. Increases value
    of self.front and decreases self.numElems by 1. Resets previous front value 
    to None, and returns previous top value. Wraps front index, if necessary.
    """
    def pop(self):
        # Return none if queue is empty
        if self.isEmpty():
            return None
        front_elem = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.numElems -= 1
        return front_elem
