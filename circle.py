import math

def area(r):
    """
    Calculate the area of a circle given its radius.

    Args:
        r (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * r * r

def perimeter(r):
    """
    Calculate the perimeter (circumference) of a circle given its radius.

    Args:
        r (float): The radius of the circle.

    Returns:
        float: The perimeter of the circle.
    """
    return 2 * math.pi * r

