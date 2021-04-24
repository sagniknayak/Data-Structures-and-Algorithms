class Node:
    '''
     This class defines the Nodes of the Linked List and their properties and methods.
    '''
    def __init__(self, data=None, next=None):
        '''
        __init__ This initializes a Node of the Linked List

        Args:
            data (<LinkedListElement>, optional): Value to be stored in the Node. Defaults to None.
            next (Node, optional): Link to the successive Node. Defaults to None.
        '''
        self._info = data
        self._link = next

    def get_link(self):
        '''
        get_link Get link of the successive Node.

        Returns:
            Node: The successive Node
        '''
        return self._link

    def get_value(self):
        '''
        get_value Get the value stored in the Node.

        Returns:
            <LinkedListElement>: The value stored in the Node.
        '''
        return self._info

    def set_value(self, data):
        '''
        set_value Set the value stored in the Node

        Args:
            data (<LinkedListElement>): Value to be stored in the Node.
        '''
        self._info = data

    def set_link(self, link):
        '''
        set_link Set the link to the successive Node.

        Args:
            link (Node): The successive Node.
        '''
        self._link = link

    def __del__(self):
        '''
        __del__ Prints a message when a Node is destroyed.
        '''
        if self._info is not None:
            print(f"A node with value {self._info} is deleted.")


class LinkedList:
    '''
     This class defines the methods and attributes of the Linked List.
    '''
    def __init__(self):
        '''
        __init__ Initializes the start and size of the Linked List.
        '''
        self._start = None
        self._size = 0

    def get_start(self):
        '''
        get_start Get the start of the Linked List.

        Returns:
            Node: Starting Node of the Linked List.
        '''
        return self._start

    def insert(self, data, loc=None):
        '''
        insert Inserts a Node in the Linked List.

        Args:
            data (<LinkedListElement>): Value to be stored in the Linked List Node.
            loc (int, optional): Valid position in the Linked List where data can be inserted. Defaults to None.

        Returns:
            boolean: Defines if the Node with value 'data' is inserted.
        '''
        if loc is None or 0 <= loc <= self.get_size():
            loc = self.get_size() if loc == None else loc
            new_node = Node(data)

            sentinel = Node(data=None, next=self._start)
            current = sentinel

            for _ in range(loc):
                current = current.get_link()

            new_node.set_link(current.get_link())
            current.set_link(new_node)

            self._start = sentinel.get_link()
            self._size += 1
            return True
        else:
            return False

    def search(self, data, l_range = None, u_range = None):
        '''
        search Search for a value in the Linked List.

        Args:
            data (<LinkedListElement>): This value is to be searched in the Linked List.
            l_range (int, optional): Positional argument for the Linked List from where it would start searching. Defaults to None.
            u_range ([type], optional): Positional argument for the Linked List till which it would search. Defaults to None.

        Returns:
            int: Position of the searched value in the list, returns -1 if not found.
        '''
        l_range = 0 if l_range is None else l_range
        u_range =   self.get_size() if u_range is None else u_range
        cntr = -1
        pos = 0
        current = self._start
        while current is not None:
            if current.get_value() == data and l_range <= pos < u_range:
                cntr = pos
                break
            current = current.get_link()
            pos += 1
        return cntr
    
    def delete(self, data = None, pos = None):
        '''
        delete Deletes a Node from the Linked List

        Args:
            data (<LinkedListElement>, optional): This value is to be searched and then the Node (the first instance) containing it will be deleted. Defaults to None.
            pos (int, optional): Node present at this position is to be deleted. Defaults to None.

        Raises:
            AttributeError: Raised when either both or none of 'data' or 'pos' is provided.

        Returns:
            boolean: Indicates whether the Node is deleted or not.
        '''
        if (data == None) ^ (pos == None):
            if pos == None:
                pos = self.search(data)
            check_val = [i for i in range(self.get_size())]
            if pos != -1 and pos in check_val:
                sentinel = Node(next=self._start)
                current = sentinel
                for _ in range(pos):
                    current = current.get_link()
                current.set_link(current.get_link().get_link())
                self._start = sentinel.get_link()
                self._size -= 1
                return True
            else:
                return False
        else:
            raise AttributeError("You cannot specify both or none of data and position to delete simultaneously.")

    def get_size(self):
        '''
        get_size Get the current size of the Linked List

        Returns:
            int: Current size of the Linked List
        '''
        return self._size

    def __str__(self):
        '''
        __str__ This is called when printing an object of this class.

        Returns:
            string: Linked List representation.
        '''
        node = self._start
        linked_list = 'START->'
        while node is not None:
            value = node.get_value()
            node = node.get_link()
            linked_list += f'[{value}]->'
        linked_list += 'NULL'
        return linked_list
