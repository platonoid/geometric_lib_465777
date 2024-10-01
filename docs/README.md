Эта программа позволяет вычислять площадь и периметр различных геометрических фигур, таких как круг, квадрат, прямоугольник и треугольник. Пользователь вводит тип фигуры, выбирает требуемую операцию (периметр или площадь) и предоставляет необходимые размеры. Программа затем использует встроенные математические формулы для выполнения расчетов и выводит результат.

File circle.py
    import math


    def area(r):
      """
      Calculates the area of a circle.

      Args:
          r: The radius of the circle.

      Returns:
          The area of the circle.
      """
      return math.pi * r * r


    def perimeter(r):
      """
      Calculates the perimeter of a circle.

      Args:
          r: The radius of the circle.

      Returns:
          The perimeter of the circle.
      """
      return 2 * math.pi * r


File square.py
    def area(a):
      """
      Calculates the area of a square.

      Args:
          a: The length of a side of the square.

      Returns:
          The area of the square.
      """
      return a * a


    def perimeter(a):
      """
      Calculates the perimeter of a square.

      Args:
          a: The length of a side of the square.

      Returns:
          The perimeter of the square.
      """
      return 4 * a


File triangle.py
    def area(a, b, c):
      """
      Calculates the area of a triangle using Heron's formula.

      Args:
          a: Length of side a of the triangle.
          b: Length of side b of the triangle.
          c: Length of side c of the triangle.

      Returns:
          The area of the triangle.
      """
      s = (a + b + c) / 2
      return (s * (s - a) * (s - b) * (s - c)) ** 0.5


    def perimeter(a, b, c):
      """
      Calculates the perimeter of a triangle.

      Args:
          a: Length of side a of the triangle.
          b: Length of side b of the triangle.
          c: Length of side c of the triangle.

      Returns:
          The perimeter of the triangle.
      """
      return a + b + c

File calculate.py
    import circle  # Assuming you have a 'circle.py' file with the circle functions
    import square  # Assuming you have a 'square.py' file with the square functions

    figs = ['circle', 'square']
    funcs = ['perimeter', 'area']
    sizes = {'perimeter-circle': 1, 'area-circle': 1, 'perimeter-square': 1, 'area-square': 1}

    def calc(fig, func, size):
      """
      Calculates the area or perimeter of a circle or square.

      Args:
          fig: The type of figure, either 'circle' or 'square'.
          func: The desired calculation, either 'perimeter' or 'area'.
          size: A list of size values for the figure.
                 For circles, it's the radius.
                 For squares, it's the side length.

      Returns:
          None. Prints the result of the calculation.

      Raises:
          AssertionError: If the provided figure or function is invalid.
      """
      assert fig in figs, f"Invalid figure: {fig}. Choose from: {figs}"
      assert func in funcs, f"Invalid function: {func}. Choose from: {funcs}"

      result = eval(f'{fig}.{func}(*{size})')
      print(f'{func} of {fig} is {result}')

    if __name__ == "__main__":
      func = ''
      fig = ''
      size = []

      while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

      while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

      while len(size) != sizes[f"{func}-{fig}"]:
        size = list(map(int, input(
            "Input figure sizes separated by space, 1 for circle and square\n"
        ).split(' ')))

      calc(fig, func, size)



b5b0fae L-04: Update docs for calculate.py
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
