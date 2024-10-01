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
