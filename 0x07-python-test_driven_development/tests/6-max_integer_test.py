#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    tests the function max_integer
    """

    def test_module_docstring(self):
        module_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_function_docstring(self):
        fun_doc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(fun_doc) > 1)

    def test_max_integer_normal(self):
        self.assertEqual(max_integer([0, 0]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 234, 322, 4456, 5]), 4456)
        self.assertEqual(max_integer([True, False]), True)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-221, -2, -573, -44, -5]), -2)

    def test_max_integer_mixed(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(max_integer([-1, 200, -34, 4, -335]), 200)

    def test_max_integer_single(self):
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([1000]), 1000)

    def test_max_integer_duplicates(self):
        self.assertEqual(max_integer([3, 5, 3, 7, 5, 9]), 9)
        self.assertEqual(max_integer([-333, -5, -43, -7, -5, -9]), -5)
        self.assertEqual(max_integer([-33, -5, 3, -7, 5, -9]), 5)

    def test_max_integer_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")
        self.assertEqual(max_integer("abcd"), "d")
        self.assertEqual(max_integer(["abc", "xyz"]), "xyz")
        self.assertEqual(max_integer(["a", "z"]), "z")
        self.assertEqual(max_integer("1234567890"), "9")

    def test_max_integer_list_of_lists(self):
        list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_integer(list_of_lists), [7, 8, 9])
        list_of_lists = [[0, 0, 0], [-4, -5, 6], [-7, -8, -9]]
        self.assertEqual(max_integer(list_of_lists), [0, 0, 0])

    def test_max_integer_empty(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([None]))

    def test_max_integer_invalid_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three", 4, 5])
        with self.assertRaises(TypeError):
            max_integer({-1, -2, 4, 5})
        with self.assertRaises(TypeError):
            max_integer([None, 2])
        with self.assertRaises(TypeError):
            max_integer(5, 4)


if __name__ == '__main__':
    unittest.main()
