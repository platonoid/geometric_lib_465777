
import math
def area(r):

    '''
    Принимает число r - радиус круга
    Возвращает площадь круга
    Пример: r=4, area(4)=50.26548245743669
    '''
    return math.pi * r * r
def perimeter(r):
    '''
    Принимает число r - радиус круга
    Возвращает периметр круга
    Пример: r=4, perimeter(4)=25.132741228718345
    '''
    return 2 * math.pi * r