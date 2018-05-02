import unittest
import triangle_square
from triangle_square import Point


class TestTriangleSquare(unittest.TestCase):
    """
    Tests for the triangle_square.py

    """

    def test_wrong_input_data(self):
        """ Tests if input data are not numbers(all or only one argument). """
        with self.assertRaises(ValueError) as ve:
            triangle_square.create_point(['1', '!'])
        self.assertEqual("The type of given arguments is wrong! It's not number!", ve.exception.args[0])

    def test_good_input_data(self):
        """ Tests if all arguments are numbers. """
        self.assertEqual(1.0, triangle_square.triangle_square(Point(0, 0), Point(1, 0), Point(0, 2)))

    def test_get_length(self):
        """ Tests the computation of length. """
        self.assertEqual(2.23606797749979, triangle_square.get_length(Point(1, 2), Point(0, 0)))

    def test_degenerated_triangle(self):
        """ Tests if the triangle is degenerated. """
        with self.assertRaises(Exception) as e:
            triangle_square.triangle_square(Point(0, 0), Point(1, 0), Point(2, 0))
        self.assertEqual('The triangle is degenerated, try again!', e.exception.args[0])


if __name__ == '__main__':
    unittest.main()