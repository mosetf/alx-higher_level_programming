#!/usr/bin/python3
""" module rectangle """
from models.base import Base


class Rectangle(Base):
    """
    initializes a rectangle
    arg:
        width: rectangles width
        height:rectangles height
        x: x
        y:y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initilize"""
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        """
        reps a string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def check_type_value(self, name:  str, value: object, greater_equal=False):
        """
        checks type and value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, width: int):
        """
        setter
        """
        self.check_type_value('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, height: int):
        """
        setter
        """
        self.check_type_value('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, x: int):
        """
        setter
        """
        self.check_type_value('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, y: int):
        """
        y setter
        """
        self.check_type_value('y', y, True)
        self.__y = y

    def area(self) -> int:
        """
        retun area
        """
        return self.width * self.height

    def display(self):
        """
        prints rectangle using #
        """
        print('\n'*self.y, end='')
        for lst in range(self.height):
            print(' '*self.x + '#'*self.width)

    def update(self, *args, **kwargs):
        """
        update rectangle attributes
        """

        expect = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                args + expect[len(args):len(expect)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self) -> int:
        """
        rectangle to dictionary
        """

        return {
            'x': self.x, 'y': self.y, 'id': self.id,
            'height': self.height, 'width': self.width}
