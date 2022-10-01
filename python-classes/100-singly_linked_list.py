#!/usr/bin/python3
"""Module that defines a Node and Singly Linked List class"""


class Node():
    """Defines a Node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to return de data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to modify the data value"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        
        self.__data = value

    @property
    def next_node(self):
        """Getter method to return the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to modify the next node value"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList():
    """Defines a Singly Linded List"""
    def __init__(self):
        self.__head = None