#!/usr/bin/python3
"""j'suis saoulé"""


class Square:
    """class et attribut privé 0 """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
