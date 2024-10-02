import math

def area(r):
    '''
    Возвращает площадь круга.

        Параметры:
            r (int): радиус круга
        
        Возвращаемое значение:
            math.pi * r * r (int): искомая площадь круга.
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметры:
            r (int): радиус круга
        
        Возвращаемое значение:
            2 * math.pi * r (int): искомый периметр круга.
    '''
    return 2 * math.pi * r

