def triangle_area(a, h): 
    if (a == 0 or h == 0):
        raise ValueError("Стороны должны быть ненулевыми")
    return a * h / 2 

def triangle_perimeter(a, b, c): 
    if (a == 0 or b == 0 or c == 0):
        raise ValueError("Стороны должны быть ненулевыми")
    return a + b + c 
