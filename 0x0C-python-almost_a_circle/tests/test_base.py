#!/usr/bin/python3
"""
Unittest tests for Base Class
"""


from models import base
from models import rectangle
import unittest
import pep8
import json
import os
Base = base.Base
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """
    Pep8 tests/test_models/test_base.py
    """
    def test_pep8(self):
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestBase(unittest.TestCase):
    """
    Tests models/base.py
    """
    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

    def test_id_given(self):
        """
        Test ids when given
        """
        self.assertTrue(Base(789), self.id == 789)
        self.assertTrue(Base(-2), self.id == -2)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(89), self.id == 89)

    def test_id_not_given(self):
        """
        Test ids incremented nb_objects
        """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attr_access(self):
        """
        Test private attributes are not accessible
        """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_invalid_args(self):
        """
        Test too many args
        """
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_class(self):
        """
        Test class created is Base
        """
        self.assertTrue(Base(100), self.__class__ == Base)

    def test_to_json_string(self):
        """
        Test dict given translates into JSON str
        """
        d0 = {"id": 0, "width": 2, "height": 3, "x": 4, "y": 5}
        d1 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        str01 = Base.to_json_string([d0, d1])
        self.assertTrue(type(d0) == dict)
        self.assertTrue(type(str01) == str)
        self.assertTrue(str01,
                        [{"id": 0, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])

    def test_none_to_json_string(self):
        """
        Test no dic given translates into JSON str of empty dic
        """
        d2 = None
        str2 = Base.to_json_string([d2])
        self.assertTrue(type(str2) == str)
        self.assertTrue(str2, "[]")

    def test_empty_to_json_string(self):
        """
        Test empty dic given translates into JSON str of empty dic
        """
        d3 = dict()
        str3 = Base.to_json_string([d3])
        self.assertTrue(len(d3) == 0)
        self.assertTrue(type(str3) == str)
        self.assertTrue(str3, "[]")

    def test_from_json_string(self):
        """
        Test JSON str translates into Python dic
        """
        s0 = '[{"id": 0, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        strs0 = Base.from_json_string(s0)
        self.assertTrue(type(s0) == str)
        self.assertTrue(type(strs0) == list)
        self.assertTrue(type(strs0[0]) == dict)
        self.assertTrue(strs0,
                        [{"id": 0, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(strs0[0],
                        {"id": 0, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_from_none_json_string(self):
        """
        Test no JSON str translates into empty Python dic
        """
        s2 = None
        str2 = Base.from_json_string(s2)
        self.assertTrue(type(str2) == list)
        self.assertTrue(str2 == [])

    def test_from_empty_json_string(self):
        """
        Test no JSON str translates into empty Python dic
        """
        s3 = ""
        str3 = Base.from_json_string(s3)
        self.assertTrue(type(str3) == list)
        self.assertTrue(str3 == [])

    def test_create(self):
        """
        Test transferring attribute dic to another instance
        """
        r = Rectangle(3, 5, 1, 2, 98)
        rdic = r.to_dictionary()
        r2 = Rectangle.create(**rdic)
        self.assertEqual(str(r), '[Rectangle] (98) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (98) 1/2 - 3/5')
        self.assertIsNot(r, r2)

    def test_save_to_file(self):
        """
        Test save to file
        """
        r = Rectangle(1, 7, 34, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r.to_dictionary(), r2.to_dictionary()]),
                file.read())

    def test_save_none_to_file(self):
        """
        Test save None to file
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_empty_none_to_file(self):
        """
        Test save empty list to file
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_load_from_file(self):
        """
        Test load from file
        """
        r = Rectangle(1, 7, 34, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        for k, v in enumerate(recs):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (99) 34/8 - 1/7')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (98) 2/2 - 2/4')

    def test_load_from_none_file(self):
        """
        Test load from None file
        """
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_load_from_empty_file(self):
        """
        Test load from empty file
        """
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)
