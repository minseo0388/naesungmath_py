import math

class Quadrilateral:
    @staticmethod
    def parallelogram_area(base_side, height):
        return base_side * height

    @staticmethod
    def rectangle_area(width, height):
        return width * height

    @staticmethod
    def rectangle_diagonal(width, height):
        return math.sqrt(width**2 + height**2)

    @staticmethod
    def rectangle_perimeter(width, height):
        return 2 * (width + height)

    @staticmethod
    def rhombus_area(diagonal1, diagonal2):
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def square_area(side):
        return side**2

    @staticmethod
    def trapezoid_area(a, b, h):
        return 0.5 * (a + b) * h
