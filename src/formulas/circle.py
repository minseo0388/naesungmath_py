import math

class Circle:
    @staticmethod
    def area(radius):
        return math.pi * (radius**2)

    @staticmethod
    def perimeter(radius):
        return 2 * math.pi * radius

    @staticmethod
    def sector_area(radius, k):
        return 0.5 * (radius**2) * k

    @staticmethod
    def sector_angle(radius, arc_length):
        return (180 * arc_length) / (math.pi * radius)

    @staticmethod
    def arc_length(radius, angle_deg):
        return 2 * math.pi * radius * (angle_deg / 360)
