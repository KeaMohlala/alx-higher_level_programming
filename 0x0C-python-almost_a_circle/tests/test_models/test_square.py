#!/usr/bin/python3
"""
tests for square class
"""

import unittest
import sys
import io
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """
    tests the square class
    """

    def setUp(self):
        """
        set up square instance to be used in the tests
        """
        self.s1 = Square(10)
        self.s2 = Square(2, 0, 0, 12)
        self.s3 = Square(1411, 3, 4)

    def tearDown(self):
        """
        tear down the square instances after each test
        """
        del self.s1
        del self.s2
        del self.s3

    def test_setup(self):
        """
        tests init function for each square instance
        """

        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.id, 12)
        self.assertEqual(self.s2.x, 0)
        self.assertEqual(self.s3.size, 1411)
        self.assertTrue(issubclass(Square, Rectangle))

    def test_validation(self):
        """
        test validation of setter methods
        """
        with self.assertRaises(TypeError):
            s1 = Square(10, "2")
            s2 = Square(10.2, 2)
            s3 = Square(10, (0, 0))
        with self.assertRaises(ValueError):
            s4 = Square(-10)
            s5 = Square(10, 3, -1)

    def test_area(self):
        """
        tests area method
        """
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 1990921)

    def test_missingarguments(self):
        """
        tests for missing positional arguments
        """
        with self.assertRaisesRegex(
            TypeError, "missing 1 required positional argument: 'size'"
        ):
            Square(x=15)

        with self.assertRaisesRegex(
            TypeError,
            "missing 1 required positional argument: 'size'",
        ):
            Square()

    def test_attributes(self):
        """
        tests attributes before modification
        """
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 1411)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 0)
        self.assertEqual(self.s3.x, 3)
        self.assertEqual(self.s3.y, 4)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)

    def test_update_attributes(self):
        """
        tests attributes after modification
        """
        self.s1.size = 2
        self.s2.size = 4
        self.s3.size = 400
        self.s1.x = 6
        self.s2.x = 1
        self.s3.x = 0
        self.s1.y = 2
        self.s2.y = 1
        self.s3.y = 1

        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s2.size, 4)
        self.assertEqual(self.s3.size, 400)
        self.assertEqual(self.s1.x, 6)
        self.assertEqual(self.s2.x, 1)
        self.assertEqual(self.s3.x, 0)
        self.assertEqual(self.s3.y, 1)
        self.assertEqual(self.s1.y, 2)
        self.assertEqual(self.s2.y, 1)

    def test_update(self):
        """
        tests the update method
        """
        self.s1.update(10, 10, 10, 10)
        self.s2.update(y=1, size=2, x=3, id=89)
        self.s3.update(size=1, x=2)

        self.assertEqual(self.s1.id, 10)
        self.assertEqual(self.s1.y, 10)
        self.assertEqual(self.s2.id, 89)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.x, 2)

    def test_update_combined(self):
        """
        test update method with a combined kwargs and args
        """
        self.s1.update(37, id=3)

    def test_todictionary(self):
        """
        test the to dictionary method
        """
        _dict = {
            "size": 1411, "x": 3,
            "y": 4, "id": self.s3.id
        }

        self.assertEqual(self.s3.to_dictionary(), _dict)

    def test_strmethod(self):
        """
        test the str special method
        """
        _st1 = f"[Square] ({self.s1.id}) 0/0 - 10"
        _st2 = f"[Square] ({self.s2.id}) 0/0 - 2"
        _st3 = f"[Square] ({self.s3.id}) 3/4 - 1411"

        self.assertEqual(self.s1.__str__(), _st1)
        self.assertEqual(self.s2.__str__(), _st2)
        self.assertEqual(self.s3.__str__(), _st3)


class TestDisplayFunction(unittest.TestCase):
    """
    tests the display method
    """

    def setUp(self):
        """
        set up the test environment
        """
        self.s1 = Square(2, 2)
        self.s2 = Square(2, 2, 1)
        self.s3 = Square(10)
        self.s4 = Square(10, 1, 3)
        self.s5 = Square(20)
        self.s6 = Square(20, 2, 1)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.s1.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_s1 = "##\n##\n"

        self.assertEqual(output, expected_output_s1)

    def test_display2(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.s2.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_s2 = "\n" + "  " + "##\n" + "  " + "##\n"

        self.assertEqual(output, expected_output_s2)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.s3.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_s3 = "##########\n" * 10

        self.assertEqual(output, expected_output_s3)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.s4.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_s4 = "\n\n\n" + (" " + "##########\n") * 10

        self.assertEqual(output, expected_output_s4)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.s5.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_s5 = "####################\n" * 20

        self.assertEqual(output, expected_output_s5)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.s6.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_s6 = "\n" + ("  " + "####################\n") * 20

        self.assertEqual(output, expected_output_s6)
