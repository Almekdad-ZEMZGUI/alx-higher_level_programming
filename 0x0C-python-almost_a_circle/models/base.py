#!/usr/bin/python3
"""
base module
This class will be the “base” of all other classes
in this project. The goal of it is to manage id attribute
in all your future classes and to avoid duplicating the same code
"""


import json
import csv


class Base:
    """
    Class Base:
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None):
    - if id is not None, assign the public instance
    attribute id with this argument value
    you can assume id is an integer and you don’t
    need to test the type of it
    - otherwise, increment __nb_objects and assign the new
    value to the public instance attribute id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        obj = []
        if list_objs is not None:
            for o in list_objs:
                obj.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(obj))

    @staticmethod
    def from_json_string(json_string):
        """
         returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        file_name = cls.__name__ + ".json"
        res = []
        try:
            with open(file_name, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                res.append(cls.create(**instances[i]))
        except Exception:
            pass
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes and deserializes in CSV
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        serializes and deserializes in CSV
        """
        obj = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                obj.append(o)
        return obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
