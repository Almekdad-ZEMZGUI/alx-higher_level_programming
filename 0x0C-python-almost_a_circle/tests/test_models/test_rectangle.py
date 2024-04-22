#!/usr/bin/python3
"""
Unittest tests for Rectangle Class
"""


import os
import pep8
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """
    Pep8 models/rectangle.py and tests/test_models/test_rectangle.py
    """
    def test_pep8(self):
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestBase(unittest.TestCase):
    """
    Tests for models/rectangle.py
    """
    def test_all_attr_given(self):
        """
        Test all attributes match the given
        """
        r1 = Rectangle(30, 20, 1, 2, 98)
        self.assertTrue(r1.width == 30)
        self.assertTrue(r1.height == 20)
        self.assertTrue(r1.x == 1)
        self.assertTrue(r1.y == 2)
        self.assertTrue(r1.id == 98)

    def test_default_attr(self):
        """
        Test attributes
        """
        r2 = Rectangle(5, 4)
        self.assertTrue(r2.width == 5)
        self.assertTrue(r2.height == 4)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)

    def test_attr_validated(self):
        """
        Test attr are validated before set
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("HELLO", 1, 1, 1, 1)
            Rectangle([10, 3], 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {20, }, 1, 1, 1)
            Rectangle(1, {"f": 20}, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, None, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (30, 20), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -98, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -20, 1, 1, 1)

    def test_private_attr_access(self):
        """
        Test private attr not accessible
        """
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_invalid_args(self):
        """
        Test too many args
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 54, 3, 4, 50, 6, 7)
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    def test_class(self):
        """
        Test class created is indeed Rectangle
        """
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)

    def test_area(self):
        """
        area
        """
        self.assertEqual(Rectangle(2, 40).area(), 80)
        self.assertEqual(Rectangle(8, 7, 0, 0).area(), 56)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """
        display
        """
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3).display()
            b = bufr.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_print(self):
        """
        __str__
        """
        r = Rectangle(1, 2, 4, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 4/4 - 1/2')

    def test_update(self):
        """
        update(*args)
        """
        r = Rectangle(34, 2, 30, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(99)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 10/10')
        r.update(99, 1)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/10')
        r.update(99, 1, 2, 3, 40)
        self.assertEqual(str(r), '[Rectangle] (99) 3/40 - 1/2')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(99, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(99, 1, 2, 3, -99)
        r.update(id=53)
        self.assertEqual(str(r), '[Rectangle] (53) 3/40 - 1/2')
        r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(r), '[Rectangle] (44) 770/880 - 990/2')
        r.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(r), '[Rectangle] (4000) 770/880 - 990/2')

    def test_to_dictionary(self):
        """
        to_dictionary
        """
        dic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(dic), dict)
        r2 = Rectangle(10, 10)
        r2.update(**dic)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')
