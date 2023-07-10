#!/usr/bin/python3
"""class base_geometry
Creates a class
"""


class BaseGeometry:
    """Class with public instance method that raises
    an exception with a message"""

    def area(self):
        """Raises an Exception with the message
        'area() is  not implemented'
        """

        raise Exception('area() is not implemented')
