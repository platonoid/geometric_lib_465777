#Общее описание решения 
Проект geometric_lib - это набор инструментов для работы с геометрическими фигурами на языке Python.
Библиотека предоставляет функции для вычисления периметра и площади таких фигур, как круг и квадрат.

geometric_lib организована модульно:

- Каждый модуль отвечает за определенную фигуру. Например, модуль circle содержит функции для вычисления периметра и площади круга, а модуль square - для квадрата.
- Модули экспортируют свои функции, делая их доступными для использования в других частях программы.

Благодаря такому подходу, geometric_lib обеспечивает удобный и гибкий инструмент для работы с геометрическими фигурами в Python.
 
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`
#Описание каждой функции с примерами вызова 
 
##Circle 
 
area:  
Возвращает значение площади круга с заданным радиусом 
a = 3 
area(a) = 28.274333882308137
 
perimeter 
Возвращает значение периметра круга с заданным радиусом 
a = 3
perimeter(a) = 18.849555921538758
 
##Square 
 
area: 
Возвращает значение площади квадрата с заданной стороной 
a = 3
area(a) = 9
 
perimeter: 
Возвращает значение периметра квадрата с заданной стороной 
a = 3
perimeter(a) = 12
 
##Triangle 
 
area: 
Возвращает полупериметр треугольника с заданными сторонами 
a, b, c = 1, 2, 3 
area(a, b, c) = 3.0 
 
perimeter: 
Возвращает значение периметра треугольника с заданными сторонами 
a, b, c = 1, 2, 3 
perimeter(a, b, c) = 6 
 
##Calculate 
Ничего не возвращает

## История изменения проекта:
commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (HEAD -> develop, origin/develop, apple)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

    L-04: Triangle added

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
(END)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.pycommit b5b0fae727ca72c317c383b39c0af73d6adcd81c (HEAD -> develop, origin/develop, apple)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

    L-04: Triangle added
:
