#!/usr/bin/python3
"""
tests for rectangle class
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest. TestCase):
    """
    tests the rectangle class
    """

    def setUp(self):
        """
        set up rectangle instance to be used in the tests
        """
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(10, 2, 0, 0, 12)
        self.r3 = Rectangle(1411, 781, 3, 4)

    def tearDown(self):
        """
        tear down the rectangle instances after each test
        """
        del self.r1
        del self.r2

    def test_setup(self):
        """
        tests init function for each rectangle instance
        """

        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.id, 12)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.height, 2)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_validation(self):
        """
        test validation of setter methods
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")
            r2 = Rectangle(10.2, 2)
            r3 = Rectangle(10, 2, (0, 0))
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, -12)
            r5 = Rectangle(10, 2, 3, -1)

    def test_area(self):
        """
        tests area method
        """
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 1101991)

    def test_missingarguments(self):
        """
        tests for missing positional arguments
        """
        with self.assertRaisesRegex(
            TypeError, "missing 1 required positional argument: 'height'"
        ):
            Rectangle(width=5)

        with self.assertRaisesRegex(
            TypeError, "missing 1 required positional argument: 'width'"
        ):
            Rectangle(height=15)

        with self.assertRaisesRegex(
            TypeError,
            "missing 2 required positional arguments: 'width' and 'height'",
        ):
            Rectangle()

    def test_attributes(self):
        """
        tests attributes before modification
        """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r3.width, 1411)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r3.height, 781)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r3.y, 4)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)

    def test_update_attributes(self):
        """
        tests attributes after modification
        """
        self.r1.width = 2
        self.r2.width = 4
        self.r3.width = 400
        self.r1.height = 10
        self.r2.height = 8
        self.r3.height = 30
        self.r1.x = 6
        self.r2.x = 1
        self.r3.x = 0
        self.r1.y = 2
        self.r2.y = 1
        self.r3.y = 1

        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 4)
        self.assertEqual(self.r3.width, 400)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 8)
        self.assertEqual(self.r3.height, 30)
        self.assertEqual(self.r1.x, 6)
        self.assertEqual(self.r2.x, 1)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 1)
        self.assertEqual(self.r1.y, 2)
        self.assertEqual(self.r2.y, 1)
