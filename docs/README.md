# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Общее описание решения
## Square
- Задавая одну сторону находит площадь квадрата и его периметр
## Circle
- Задавая радиус находит площадь круга и его периметр 

# Описание каждой функции с примерами вызова
## Функции для квадрата
### area(a) - Нахождение площади квадрата
- Принимает число a (одну из сторон), возвращает квадрат числа a (его площадь)
```python
def area(a):   #(a = 5)
    return a * a   #(вернет число 25)
```
### perimeter(a) - Нахождение периметра квадрата
- Принимает число a (одну из сторон), возвращает число a умнотженное на 4 (его периметр)
```python
def perimeter(a):   #(a = 5)
    return 4 * a   #(вернет число 20)
```

## Функции для круга
### area(a)
- Принимает число r (радиус круга), возвращает число π * r² (площадь круга)
```python
def area(r):   #(a = 4)
    return math.pi * r * r   #(вернет число 50,24)
```
### perimeter(r)
- Принимает число r (радиус круга), возвращает число 2 * π * r (периметр круга)
```python
def perimeter(r):   #(a = 4)
    return 2 * math.pi * r   #(вернет число 25,12)
```

# История изменения проекта
```git
da74298 (HEAD -> edited_documentation) Добавил блоки комментариев для другого файла
7fd2e4b Добавил блоки комментариев для 2-х функций
86edb1c (origin/release) L-05: Update Docs. Add user agreement info
438b89a L-05: Add user agreement
6adb962 L-03: Docs added
3049431 (origin/feature) L-04: Add rectangle.py
b5b0fae (origin/develop) L-04: Update docs for calculate.py
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added
d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
8ba9aeb L-03: Circle and square added
```

