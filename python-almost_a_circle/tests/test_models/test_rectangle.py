#!/usr/bin/python3
"""Contains the tests for the Base class"""
import unittest
from models import rectangle
Rectangle = rectangle.Rectangle


class Test_base_docs(unittest.TestCase):
    """Test the documentation on Rectangle class"""
    def test_module_docstring(self):
        """Tests the module docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests the Rectangle class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

class Test_rectangle(unittest.TestCase):
    """Test the Rectangle class"""
    def test_rectangle(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
