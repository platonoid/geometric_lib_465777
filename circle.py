import math


def area(r):
    ''' Find the area of circle
            Parameters:
                r (double): radius of the circle
            Returned values:
                circle_area (double): area of the circle '''
    return math.pi * r * r


def perimeter(r):
    ''' Find the perimeter of circle
            Parameters:
                r (double): radius of the circle
            Returned values:
                circle_per (double): perimeter of the circle '''
    return 2 * math.pi * r

