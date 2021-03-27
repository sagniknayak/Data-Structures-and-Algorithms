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
    
    def __check_underflow__(self):
        '''
        __check_underflow__ Checks if the Stack is underflowing.

        Returns:
            boolean: Indicates whether the Stack is underflowing.
        '''
        return self._top == -1

    def push(self, element):
        '''
        push Pushes element into the Stack.

        Args:
            element (Any): This element is pushed on the top of the Stack.
        '''
        if not self.__check_overflow__():
            self._stack += [element]
            self._top += 1
        else:
            print("Stack Overflowing")

    def pop(self):
        '''
        pop Pops the topmost element of the Stack.
        '''
        if not self.__check_underflow__():
            print(self._stack[self._top])
            del self._stack[self._top]
            self._top -= 1
        else:
            print("Stack Underflowing")
