#!/usr/bin/python3
"""
Class that defines a rectangle
"""


class Rectangle:
    """
    creation of class Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Inititializes the instance with an optional
        height and width attribute

        Number of instances incremented during each new
        instance instantiation

        Args:
        width: width of the rectangle
        heigth: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the bigger rectangle based on area

        Args:
        rect_1: first rectangle
        rect_2: 2nd rectangle

        Raises:
        TypeError: if the rectangles being compares are not instances of
        Rectangle

        Returns:
        The biggest rectangle.
        If areas of both rectangles are the same rect_1 is returned
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.width * rect_1.height) > (rect_2.width * rect_2.height):
            return rect_1
        elif (rect_1.width * rect_1.height) < (rect_2.width * rect_2.height):
            return rect_2
        else:
            return rect_1

    @property
    def width(self):
        """
        getter property to retrieve the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter to set the width

        Args:
          value: width of the rectangle

        Raises:
          TypeError: if width is not an integer
          ValueError: if width is less than zero
        """
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """
        getter property to retrieve the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter to set the height attribute

        Args:
          value: height of the rectangle

        Raises:
          TypeError: if value is not an integer
          ValueError: if value is less than zero
        """
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """
        returns the area of the rectangle

        Returns:
        int: are of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        if the height or width are 0, the perimeter will be 0

        Returns:
        perimeter of the rectangle
        """
        p = 2 * (self.width + self.height)
        if self.width == 0 or self.height == 0:
            p = 0
        return p

    def __str__(self):
        """
        special method that provides a string representation
        of the object/instance

        Returns:
        returns string representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(str(self.print_symbol) * self.width
                            for _ in range(self.height))

    def __repr__(self):
        """
        returns string representation of the object to be able to recreate
        using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        special method that prints a message once an object
        has been deleted

        Number of instances is decremented after each
        instance deletion
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
