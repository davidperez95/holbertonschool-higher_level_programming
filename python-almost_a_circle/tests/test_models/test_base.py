#!/usr/bin/python3
"""Contains the tests for the Base class"""
import unittest
from models import base
Base = base.Base


class Test_base_docs(unittest.TestCase):
    """Test the documentation on Base class"""
    def test_module_docstring(self):
        """Tests the module docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

class Test_base(unittest.TestCase):
    """Test the Base class"""
    
