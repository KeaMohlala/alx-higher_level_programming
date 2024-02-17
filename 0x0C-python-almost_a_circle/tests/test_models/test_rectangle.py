#!/usr/bin/python3
"""
tests for rectangle class
"""

import unittest
import sys
import io
import os
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
        del self.r3

    def test_setup(self):
        """
        tests init function for each rectangle instance
        """

        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.id, 12)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.height, 2)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_validation_width_1(self):
        """
        test validation of setter methods for width
        """
        with self.assertRaises(TypeError) as type_error:
            Rectangle("1", 2)
        self.assertEqual(
            type_error.exception.__str__(), "width must be an integer"
        )

    def test_validation_width_2(self):
        """
        test validation of setter methods for width
        """
        with self.assertRaises(ValueError) as value_error:
            Rectangle(-1, 2)
            Rectangle(0, 2)
        self.assertEqual(
            value_error.exception.__str__(), "width must be > 0"
        )

    def test_validation_height_1(self):
        """
        test validation of setter methods for height
        """
        with self.assertRaises(TypeError) as type_error:
            Rectangle(1, "2")
        self.assertEqual(
            type_error.exception.__str__(), "height must be an integer"
        )

    def test_validation_height_2(self):
        """
        test validation of setter methods for height
        """
        with self.assertRaises(ValueError) as value_error:
            Rectangle(1, -2)
        self.assertEqual(
            value_error.exception.__str__(), "height must be > 0"
        )

    def test_validation_x_1(self):
        """
        test validation of setter methods for x
        """
        with self.assertRaises(TypeError) as type_error:
            Rectangle(1, 2, "3")
        self.assertEqual(
            type_error.exception.__str__(), "x must be an integer"
        )

    def test_validation_x_2(self):
        """
        test validation of setter methods for x
        """
        with self.assertRaises(ValueError) as value_error:
            Rectangle(1, 2, -3)
        self.assertEqual(
            value_error.exception.__str__(), "x must be >= 0"
        )

    def test_validation_y_1(self):
        """
        test validation of setter methods for y
        """
        with self.assertRaises(TypeError) as type_error:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(
            type_error.exception.__str__(), "y must be an integer"
        )

    def test_validation_y_2(self):
        """
        test validation of setter methods for y
        """
        with self.assertRaises(ValueError) as value_error:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(
            value_error.exception.__str__(), "y must be >= 0"
        )

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


class TestClsMethods(unittest.TestCase):
    """
    tests for the class methods
    """
    def test_create(self):
        """
        tests the create method no width or height
        """
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': 89, 'width': 1})
            Rectangle.create(**{'id': 89})

    def test_create_rectangle_with_minimal_attributes(self):
        """
        test create method with minimal attributes
        """
        r3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r3.id, 89)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_create_rectangle_with_x_attribute(self):
        """
        test create method with x attribute
        """
        r4 = Rectangle.create(
                **{'id': 89, 'width': 1, 'height': 2, 'x': 3}
        )
        self.assertEqual(r4.id, 89)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 0)

    def test_create_rectangle_with_xy_attributes(self):
        """
        test create method with xy attributes
        """
        r5 = Rectangle.create(
                **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        )
        self.assertEqual(r5.id, 89)
        self.assertEqual(r5.width, 1)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 3)
        self.assertEqual(r5.y, 4)


class TestRectangleFileMethods(unittest.TestCase):
    """
    to test file methods for rectangle
    """
    def setUp(self):
        """
        Create a temporary file to use for testing
        """
        self.temp_file = "temp_file.json"

    def tearDown(self):
        """
        Remove the temporary file after testing
        """
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_save_to_file_none(self):
        """
        test save to file if no inputs is given
        """
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists(self.temp_file))
        with open(self.temp_file, "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_empty_list(self):
        """
        test method if save to file takes an empty list
        """
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(self.temp_file))
        with open(self.temp_file, "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_rectangle(self):
        """
        test method to see the number of tickets
        """
        r = Rectangle(1,  2)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists(self.temp_file))
        with open(self.temp_file, "r") as f:
            content = f.read()
        expected_content = json.dumps([r.to_dictionary()])
        self.assertEqual(content, expected_content)

    def test_load_from_file(self):
        """
        test load from file
        """
        r = Rectangle(1,  2)
        Rectangle.save_to_file([r])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles),  1)
        self.assertEqual(
                loaded_rectangles[0].to_dictionary(), r.to_dictionary()
        )
