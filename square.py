def square_area(a):
    if (a == 0):
        raise ValueError("Сторона должна быть ненулевой")
    return a * a


def square_perimeter(a):
    if (a == 0):
        raise ValueError("Сторона должна быть ненулевой")
    return 4 * a
