#!/usr/bin/python3
"""
tests for rectangle class
"""

import unittest
import sys
import io
from unittest.mock import patch
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

    def test_update(self):
        """
        tests the update method
        """
        self.r1.update(10, 10, 10, 10, 10)
        self.r2.update(y=1, width=2, x=3, id=89)
        self.r3.update(width=1, x=2)

        self.assertEqual(self.r1.id, 10)
        self.assertEqual(self.r1.y, 10)
        self.assertEqual(self.r2.id, 89)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.x, 2)

    def test_update_combined(self):
        """
        test update method with a combined kwargs and args
        """
        self.r1.update(37, id=3)

    def test_todictionary(self):
        """
        test the to dictionary method
        """
        _dict = {
            "width": 1411, "height": 781, "x": 3,
            "y": 4, "id": self.r3.id
        }

        self.assertEqual(self.r3.to_dictionary(), _dict)

    def test_strmethod(self):
        """
        test the str special method
        """
        _st1 = f"[Rectangle] ({self.r1.id}) 0/0 - 10/2"
        _st2 = f"[Rectangle] ({self.r2.id}) 0/0 - 10/2"
        _st3 = f"[Rectangle] ({self.r3.id}) 3/4 - 1411/781"

        self.assertEqual(self.r1.__str__(), _st1)
        self.assertEqual(self.r2.__str__(), _st2)
        self.assertEqual(self.r3.__str__(), _st3)


class TestDisplayFunction(unittest.TestCase):
    """
    tests the display method
    """

    def setUp(self):
        """
        set up the test environment
        """
        self.r1 = Rectangle(2, 2)
        self.r2 = Rectangle(2, 2, 2, 1)
        self.r3 = Rectangle(10, 5)
        self.r4 = Rectangle(10, 5, 1, 3)
        self.r5 = Rectangle(20, 35)
        self.r6 = Rectangle(20, 35, 2, 1)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.r1.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_r1 = "##\n##\n"

        self.assertEqual(output, expected_output_r1)

    def test_display2(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.r2.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_r2 = "\n" + "  " + "##\n" + "  " + "##\n"

        self.assertEqual(output, expected_output_r2)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.r3.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_r3 = "##########\n" * 5

        self.assertEqual(output, expected_output_r3)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.r4.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_r4 = "\n\n\n" + (" " + "##########\n") * 5

        self.assertEqual(output, expected_output_r4)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.r5.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_r5 = "####################\n" * 35

        self.assertEqual(output, expected_output_r5)

    def test_display1(self):
        """
        tests the display method
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.r6.display()

        sys.stdout = sys.__stdout__

        output = capturedOutput.getvalue()

        expected_output_r6 = "\n" + ("  " + "####################\n") * 35

        self.assertEqual(output, expected_output_r6)
