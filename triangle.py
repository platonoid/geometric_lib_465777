def area(a, b, c):
    """
    Calculate the area of a triangle using the semi-perimeter formula.

    Args:
        a (float): Length of the first side.
        b (float): Length of the second side.
        c (float): Length of the third side.

    Returns:
        float: The area of the triangle.
    """
    return (a + b + c) / 2

def perimeter(a, b, c):
    """
    Calculate the perimeter of a triangle given the lengths of its sides.

    Args:
        a (float): Length of the first side.
        b (float): Length of the second side.
        c (float): Length of the third side.

    Returns:
        float: The perimeter of the triangle.
    """
    return a + b + c
