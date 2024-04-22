#!/usr/bin/python3
"""
square module
with a class Square that
inherits from Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle:
    - In the file models/square.py
    - Class Square inherits from Rectangle
    - Class constructor: def __init__(self, size, x=0, y=0, id=None)::
        * Call the super class with id, x, y, width and height -
        this super call will use the logic
        of the __init__ of the Rectangle class.
        The width and height must be assigned to the value of size
        * You must not create new attributes for this class,
        use all attributes of Rectangle - As reminder:
        a Square is a Rectangle with the same width and height
        * All width, height, x and y validation must inherit from Rectangle -
        same behavior in case of wrong data
    - The overloading __str__ method should return
    [Square] (<id>) <x>/<y> - <size> - in our case, width or height
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns [Square] (<id>) <x>/<y> - <size>
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute:
        - 1st argument should be the id attribute
        - 2nd argument should be the width attribute
        - 3rd argument should be the height attribute
        - 4th argument should be the x attribute
        - 5th argument should be the y attribute
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
