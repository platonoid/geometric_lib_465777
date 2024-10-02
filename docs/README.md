# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Общее описание
- Содержит два файла circle.py и rectangle.py с функциями вычисления площади и периметра соответствующих геометрических фигур.

## Функции
# circle.py
- area() принимает число r - радиус окружности, возвращает квадрат этого числа, умноженный на pi.
'''
r = 6
print(area(r)) // 6 * 6 * pi
>> 113,09733552923255
'''
- perimeter() принимает число r - радиус окружности, возвращает это число, умноженное на 2 и на pi.
'''
r = 7
print(perimeter(r)) // 7 * 2 * pi
>> 43,98229715025710
'''
# rectangle.py
- area() принимает число a - сторону квадрата, возвращает квадрат этого числа - площадь фигуры.
'''
a = 8
print(area(a)) // 8 * 8 
>> 64
'''
- perimeter() принимает число a - сторону квадрата, возвращает это число, умноженное на 4 - периметр фигуры.
'''
a = 8
print(perimeter(a)) // 8 * 4 
>> 32
'''

## История изменения
commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (HEAD -> git2lab, origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

