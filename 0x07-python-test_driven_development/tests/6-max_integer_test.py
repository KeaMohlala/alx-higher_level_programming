#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positives(self):
        """
        test positive integer lists
        """
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)
        self.assertEqual(max_integer([67, 98, 1000, 200000]), 200000)
        self.assertEqual(max_integer([1, 67, 88, 88, 3]), 88)
        self.assertEqual(max_integer([1, 67, 88, 67, 3]), 88)
        self.assertEqual(max_integer([88]), 88)

    def test_negatives(self):
        """
        test negative integer lists
        """
        self.assertEqual(max_integer([-10, -2, -3, -5]), -2)
        self.assertEqual(max_integer([-67, -98, -1000, -200000]), -67)
        self.assertEqual(max_integer([-1, -67, -88, -88, -3]), -1)
        self.assertEqual(max_integer([-1, -67, -88, -67, -3]), -1)

    def test_mixed(self):
        """
        test mixed (negative and positive integer) lists
        """
        self.assertEqual(max_integer([10, -2, 3, -5]), 10)
        self.assertEqual(max_integer([-67, 98 -1000, 200000]), 200000)
        self.assertEqual(max_integer([1, -67, -88, -88, 3]), 3)
        self.assertEqual(max_integer([1, -67, -88, 67, -3]), 67)

    def test_empty(self):
        """
        Test an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            max_integer(5.0)
            max_integer(6, 0)
            max_integer(6)
            max_integer({"one": 6, "two": 20000})
