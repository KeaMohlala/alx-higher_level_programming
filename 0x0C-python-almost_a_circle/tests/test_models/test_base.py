#!/usr/bin/python3
"""
Unittest for Base superclass
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestID(unittest.TestCase):
    """
    Tests the base class
    """
    b1 = Base()
    b2 = Base()
    b3 = Base(65)
    b4 = Base()
    b5 = Base(6)
    b6 = Base()

    def test_ID(self):
        """
        tests for ID allocation
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 65)
        self.assertEqual(self.b4.id, 3)
        self.assertEqual(self.b5.id, 6)
        self.assertEqual(self.b6.id, 4)
