#!/usr/bin/python3
"""Unittest for 6-max_integer"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class Test_max_integer(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_module_docstring(self):
        """Test for module docstring"""
        m = __import__("6-max_integer").__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstrig(self):
        """Test for function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Test for empty list"""
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        """Test for no arguments"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test for one element in the list"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def test_normal_test(self):
        """Test for a max in list"""
        e = [5, 20, 30, 10]
        self.assertEqual(max_integer(e), 30)

    def test_none(self):
        """Test for passing None argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()