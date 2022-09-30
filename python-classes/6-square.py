#!/usr/bin/python3
"""Module that defines de Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with private size"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.size = size

        if (type(position) is not tuple and position[0] is not int
            and position[1] is not int):
                raise TypeError("position must be a tuple of 2 positive integers")
            
        self.position = position
            
    """Getter methods"""
    @property
    def size(self):
        """Getter method to return the size"""
        return self.__size
    
    @property
    def position(self):
        """Getter method to return the position"""
        return self.__position

    """Setter methods"""
    @size.setter
    def size(self, value):
        """Setter method to modify the size value"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        """Setter method to modify the position value"""
        if (type(value) is not tuple and value[0] is not int
            and value[1] is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
            
        self.__position = value

    """Public instance methods"""
    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print a square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    if (self.__position[0] > 0):
                        for i in range(self.__position[0]):
                            print(" ", end='')
                    print("#", end='')
                print()
