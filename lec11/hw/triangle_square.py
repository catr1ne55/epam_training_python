"""

This module is for computing the square of the triangle using Heron's formula.

"""
import math


class Point:
    """
    Class which represents coordinates of the point.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)


def get_length(point1, point2):
    """

    The length of the line segment which is presented by two points.

    >>> get_length(Point(1, 2), Point(0, 0))
    2.23606797749979

    >>> get_length(Point(-1, 5), Point(8, -3.5))
    12.379418403139947

    :param point1: First point, or start.
    :type point1: Point
    :param point2: Second point, or the end.
    :type point2: Point
    :return: Length -- the distance between points.
    :rtype float
    """
    x = point2.x - point1.x
    y = point2.y - point1.y
    return math.sqrt(x ** 2 + y ** 2)


def triangle_square(point1, point2, point3):
    """
    Computes the square of the given triangle, represented by its vertexes.

    >>> triangle_square(Point(0, 0), Point(1, 0), Point(2, 0))
    Traceback (most recent call last):
    ...
    Exception: The triangle is degenerated, try again!
    >>> triangle_square(Point(1, 1), Point(-3, -3), Point(2, 2))
    Traceback (most recent call last):
    ...
    Exception: The triangle is degenerated, try again!
    >>> triangle_square(Point(0, 0), Point(1, 0), Point(0, 2))
    1.0


    :param point1: First vertex of the triangle.
    :type point1: Point
    :param point2: Second vertex of the triangle.
    :type point2: Point
    :param point3: Third vertex of the triangle.
    :type point3: Point
    :return: Square of the given triangle.
    :rtype float
    """
    a = get_length(point1, point2)
    b = get_length(point2, point3)
    c = get_length(point1, point3)
    # т.к. мы вводим три произвольные точки,
    # треугольник можно построить всегда, за исключением того случая,
    # когда три точки лежат на одной прямой, чему соответствует следующее условие:
    if a + b == c or b + c == a or a + c == b:
        raise Exception("The triangle is degenerated, try again!")
    else:
        p = (a + b + c) / 2
        square = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return square


def create_point(input_value):
    """
    Create point if all given arguments are numbers.

    >>> print(create_point(['1', '0']))
    Point(1.0, 0.0)

    >>> print(create_point(['1', '!']))
    Traceback (most recent call last):
    ...
    ValueError: The type of given arguments is wrong! It's not number!

    :param input_value: List with coordinates.
    :type input_value: list
    :return: Point(x,y) -- the point with given coordinates.
    :raise ValueError
    """
    try:
        x = float(input_value[0])
        y = float(input_value[1])
    except ValueError:
        raise ValueError("The type of given arguments is wrong! It's not number!")
    return Point(x, y)


def find_square():
    """
    Get input points from user and compute the square of triangle which vertexes are the given points.

    >>> find_square() # этот тест работает,
                      # если вводить следующие значения вершин: (0,0) (1,0) (0,2) - это нужно для того,
                      # чтобы покрыть весь код
    Введите координаты вершин треугольника, площадь которого Вы хотите узнать:
    Вершина 1 > Вершина 2 > Вершина 3 > 1.0

    :return: square of the triangle given in input
    :rtype float
    """
    print("Введите координаты вершин треугольника, площадь которого Вы хотите узнать:")
    input1 = input("Вершина 1 > ").split()
    input2 = input("Вершина 2 > ").split()
    input3 = input("Вершина 3 > ").split()
    p1 = create_point(input1)
    p2 = create_point(input2)
    p3 = create_point(input3)
    return triangle_square(p1, p2, p3)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


