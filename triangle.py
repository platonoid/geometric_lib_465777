def area(a, b, c):
    '''
    
    Вычисляет полупериметр треугольника по заданным длинам сторон. 
    
    Параметры: 
    a (float): длина первой стороны треугольника
    b (float): длина второй стороны треугольника
    c (float): длина третьей стороны треугольника
    
    Возвращаем значение: 
    (float): полупериметр треугольника
    
    Пример вызова: 
    >> area(1, 2, 3)
    3.0
    
    '''
    return (a + b + c) / 2


def perimeter(a, b, c):
    ''' 
    
    Вычисляет периметр треугольника по заданным длинам сторон. 
    
    Параметры: 
    a (float): длина первой стороны треугольника
    b (float): длина второй стороны треугольника
    c (float): длина третьей стороны треугольника
    
    Возвращаем значение: 
    (float): периметр треугольника
    
    Пример вызова: 
    >> perimeter(2, 4, 5)
    11
    
    '''
    return a + b + c
