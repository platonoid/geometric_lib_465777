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
