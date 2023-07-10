#!/usr/bin/python3
"""class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes an instance

        Args:
            - width: width
            - height:height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
