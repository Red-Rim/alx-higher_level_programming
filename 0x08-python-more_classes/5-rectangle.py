#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle():
    """Definition of the class Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize Rectangle attributes"""
        self.width = width
        self.height = height

    def __del__(self):
        """print a msg when a Rectangle is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Width attribute getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width attribute setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height attribute getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height attribute setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area function returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter function returns the rectangle
            perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def print(self):
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return
        for i in range(0, self.__height):
            [print("#", end="") for j in range(0, self.__width)]
            if i < self.__height - 1:
                print()

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width != 0 and self.__height != 0:
            for i in range(0, self.__height):
                [print("#", end="") for j in range(0, self.__width)]
                if i < self.__height - 1:
                    print()
        return ""

    def __repr__(self):
        """repr return a string representation of
            the rectangle
        """
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"
