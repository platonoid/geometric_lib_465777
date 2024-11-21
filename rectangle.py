def rectangle_area(a, b): 
    if (a == 0 or b == 0):
        raise ValueError("Стороны должны быть ненулевыми")
    return a * b 

def rectangle_perimeter(a, b): 
    if (a == 0 or b == 0):
        raise ValueError("Стороны должны быть ненулевыми")
    return 2 * (a + b) 

