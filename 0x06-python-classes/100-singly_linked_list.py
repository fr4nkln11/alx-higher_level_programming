#!/usr/bin/python3
""" Singly linked list
This Module defines a class Node
that defines a node of a singly linked list

and a class SinglyLinkedList that defines
a singly linked list by:
"""


class Node:
    """ a class Node that defines
    a node of a singly linked list by:
        Private instance attribute: data:
            property def data(self): to retrieve it
            property setter def data(self, value): to set it:
                data must be an integer,
                otherwise raise a TypeError exception
                with the message data must be an integer

        Private instance attribute: next_node:
            property def next_node(self): to retrieve it
            property setter def next_node(self, value): to set it:
                next_node can be None or must be a Node,
                otherwise raise a TypeError exception
                with the message next_node must be a Node object

        Instantiation with data and next_node:
            def __init__(self, data, next_node=None):
    """

    def __init__(self, data, next_node=None):
        if not type(data) is int:
            raise TypeError("data must be an integer")

        self.__data = data

        if not type(next_node) is Node:
            if next_node is not None:
                raise TypeError("next_node must be a Node object")

        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not type(value) is int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not type(value) is Node:
            if value is not None:
                raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """ a class SinglyLinkedList that defines
    a singly linked list by:
        Private instance attribute: head (no setter or getter)
        Simple instantiation: def __init__(self):
        Should be printable:
            print the entire list in stdout
            one node number by line
        Public instance method: def sorted_insert(self, value):
            that inserts a new Node into the correct
            sorted position in the list (increasing order)
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node into the correct
        sorted position in the list (increasing order)

        Parameters:
            @self: current instance of this class
            @value: value of the new node to be
            inserted

            Returns: nothing
        """

        new_node = Node(value)  # define new node

        if not self.__head:
            # There is no head node
            # let new_node be the head node
            self.__head = new_node
        elif value < self.__head.data:
            temp_node = self.__head
            self.__head = new_node
            self.__head.next_node = temp_node
        elif value > self.__head.data:
            cursor = self.__head

            prev_node = cursor
            while cursor:
                if value > cursor.data:
                    prev_node = cursor
                    cursor = cursor.next_node

                    # if the list is traversed and there is no node
                    # with a value last than the current
                    # then the current node should be inserted
                    # at the end of the list

                    if cursor == None:
                        prev_node.next_node = new_node
                else:
                    new_node.next_node = cursor
                    prev_node.next_node = new_node
                    break

    def __repr__(self):
        linked_list = []
        cursor = self.__head

        while cursor:
            linked_list.append("{:d}".format(cursor.data))
            cursor = cursor.next_node

        return "\n".join(linked_list)

