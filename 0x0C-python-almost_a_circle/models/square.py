#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """

    def __init__(self, size: int, x=0, y=0, id=None):
        """
        initialization
        arg:
            size: square sides size
            x:side rep
            y:side rep
            id:obj id
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self) -> int:
        """size getter
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """
        size setter
        """
        self.__size = value
        self.width = self.height = value

    def __str__(self) -> str:
        """return string rep"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    def update(self, *args, **kwargs):
        """update arguments"""
        attr = ['id', 'size', 'x', 'y']
        if args:
            for at, numb in zip(attr, args):
                setattr(self, at, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """ square return dict"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': size, 'y': y}
