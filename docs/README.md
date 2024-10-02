# Аннотация к проекту
В этом проекте на языке **python** реализованы функции для вычисления периметра и площади разных фигур, а именно: окружности, прямоугольника, квадрата и треугольника.

# Описание работы функций
## 1. Окружность (circle.py)
### Площадь
#### Аргументы
```
r (int) - радиус окружности
```
#### Реализация
```python
def area(r):
    return math.pi * r * r # здесь math - это стандартная библиотека python
```
### Периметр
#### Аргументы
```
r (int) - радиус окружности
```
#### Реализация
```python
def perimeter(r):
    return 2 * math.pi * r # здесь math - это стандартная библиотека python
```

## 2. Прямоугольник (rectangle.py)
### Площадь
#### Аргументы
```
a (int): длина первой стороны
b (int): длина второй стороны
```
#### Реализация
```python
def area(a, b): 
    return a * b 
```
### Периметр
#### Аргументы
```
a (int): длина первой стороны
b (int): длина второй стороны
```
#### Реализация
```python
def perimeter(a, b): 
    return (a + b) * 2
```

## 3. Квадрат (square.py)
### Площадь
#### Аргументы
```
a (int): длина стороны квадрата
```
#### Реализация
```python
def area(a): 
    return a * a
```
### Периметр
#### Аргументы
```
a (int): длина стороны квадрата
```
#### Реализация
```python
def perimeter(a): 
    return a * 4
```

## 4. Треугольник (triangle.py)
### Площадь
#### Аргументы
```
a (int): длина основания
h (int): высота, проведённая к основанию
```
#### Реализация
```python
def area(a, h): 
    return a * h / 2 
```
### Периметр
#### Аргументы
```
a (int): длина первой стороны
b (int): длина второй стороны
c (int): длина третьей стороны
```
#### Реализация
```python
def perimeter(a, b, c): 
	return a + b + c
```

# История коммитов
+ **8ba9aeb3cea847b63a91ac378a2a6db758682460** - L-03: Circle and square added
+ **d078c8d9ee6155f3cb0e577d28d337b791de28e2** - L-03: Docs added
+ **d080c7888b81955bad2ed78d58ad910526b5132a** - L-04: Triangle added
+ **51c40ebfd0e0b65f52fe5e54740cbb038e492db3** - L-04: Doc updated for triangle
+ **d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71** - L-04: Add calculate.py
+ **b5b0fae727ca72c317c383b39c0af73d6adcd81c** - L-04: Update docs for calculate.py
+ **3958039e9bb70547d5f2a56dd6b8f956a7d84c1b** - add new file rectangle.py with function finding area and perimeter of the rectangle
+ **74969c174e9d103596917d5499cb5cb3751c655d** - add new file triangle.py with function finding area and perimeter of the triangle, fix function finding perimeter of the rectangle in rectangle.py
+ **7d5c88f4b779c1cfecc3a49e288e7de65ddf4048** - fix function finding area of the triangle
+ **b29ffdc43ca006411848c389445ebac1eb95c92b** - add local documentation in every function