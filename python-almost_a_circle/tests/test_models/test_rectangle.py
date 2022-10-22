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
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_width_str(self):
        """Test the Rectangle class with an argument as string"""
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_height_str(self):
        """Test the Rectangle class with an argument as string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_x_str(self):
        """Test the Rectangle class with an argument as string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

    def test_y_str(self):
        """Test the Rectangle class with an argument as string"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_rectangle_all_arg(self):
        """Test the Rectangle class with all arguments"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_width_neg(self):
        """Test the Rectangle class with negative arguments"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_height_neg(self):
        """Test the Rectangle class with negative arguments"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_width_cero(self):
        """Test the Rectangle class with arguments as cero"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_height_cero(self):
        """Test the Rectangle class with arguments as cero"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_x_neg(self):
        """Test the Rectangle class with negative arguments"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_y_neg(self):
        """Test the Rectangle class with negative arguments"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_area_exists(self):
        """Test if the area method exists"""
        self.assertIsNotNone(Rectangle.area)        
