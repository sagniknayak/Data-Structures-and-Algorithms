class Stack:
    '''
     Implementation of Stack in Python
    '''
    def __init__(self, size = None):
        '''
        __init__ Initializes the Stack.

        Args:
            size (int, optional): Size of the Stack, None indicates indefinite size. Defaults to None.
        '''
        self._flag_overflow, self._max_size = [True, size] if size is not None else [False, -1]
        self._stack = list()
        self._top = -1
    
    def __check_overflow__(self):
        '''
        __check_overflow__ Checks if the Stack is overflowing.

        Returns:
            boolean: Indicates whether the Stack is overflowing.
        '''
        return self._top == self._max_size - 1 if self._flag_overflow else False

    
    def empty(self):
        '''
        empty Checks whether the Stack is empty.

        Returns:
            boolean: Returns whether the Stack is empty.
        '''
        return self._top == -1

    
    def size(self):
        '''
        size Returns the size of the Stack.

        Returns:
            int: Size of the Stack.
        '''
        return self._top + 1

    
    def peek(self):
        '''
        peek Peeks into the Stack.

        Returns:
            (<Stack Element>):  Top Element of the Stack.
        '''
        return self._stack[self._top] if not self.empty() else None

    
    def push(self, element):
        '''
        push Pushes element into the Stack.

        Args:
            element (<Stack Element>): Element to be pushed into the Stack.

        Returns:
            boolean: Conveys if the element is pushed successfully or not.
        '''
        if not self.__check_overflow__():
            self._stack += [element]
            self._top += 1
            return True
        else:
            return False

    def pop(self):
        '''
        pop Pops the top element of the Stack.

        Returns:
            <Stack Element>: The topmost element popped off the Stack.
        '''
        if not self.empty():
            val = self._stack[self._top]
            del self._stack[self._top]
            self._top -= 1
            return val
