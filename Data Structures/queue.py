class Queue:
    '''
     Implementation of Queue
    '''

    def __init__(self, capacity = None):
        '''
        __init__ Initializes the Queue and its variables.

        Args:
            capacity (int, optional): Maximum capacity of the Queue, None refers to undefined capacity. Defaults to None.
        '''
        self._flag_overflow, self._max_capacity = [True, -1] if capacity == None else [False, capacity]
        self._front = self._rear = 0
        self._queue = list()

    def size(self):
        '''
        size Returns the size of the Queue.

        Returns:
            int: Size of the Queue
        '''
        return self._rear - self._front
    
    def full(self):
        '''
        full Returns whether the Queue is full or not.

        Returns:
            boolean: Indicates if the Queue is full or not.
        '''
        return self.size() == self._max_capacity

    def empty(self):
        '''
        empty Returns whether the Queue is empty.

        Returns:
            boolean: Indicates whether the Queue is empty or not.
        '''
        return self.size() == 0

    def en_q(self, element):
        '''
        en_q Enqueues the <QueueElement> into the Queue.

        Args:
            element (<QueueElement>): Element to be enqueued.

        Returns:
            boolean: Indicates whether enqueuing is successful or not.
        '''
        if not self.full():
            self._queue += [element]
            self._rear += 1
            return True
        else:
            return False

    def de_q(self):
        '''
        de_q Dequeues the <QueueElement> from the Queue.

        Returns:
            <QueueElement>: The value dequeued from the Queue.
        '''
        if not self.empty():
            val = self._queue[self._front]
            self._queue[self._front] = None
            self._front += 1
            return val
        else:
            return None

    def front(self):
        '''
        front Returns the front of the Queue.

        Returns:
            int: front location of the Queue.
        '''
        return self._front

    def rear(self):
        '''
        rear Returns rear of the Queue.

        Returns:
            int: rear location of the Queue.
        '''
        return self._rear
