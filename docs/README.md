# Calculator Documentation

## General Description

This project is a geometric calculator that allows users to compute the area and perimeter of basic geometric shapes: circles and squares. The calculator is implemented in Python and provides a simple command-line interface for users to input the desired shape, function, and dimensions.

## How to Use the Calculator

1. Run `python calculate.py`.
2. Enter the figure name. Available are Circle and Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

## Math Formulas

### Area
- **Circle**: \( S = \pi R^2 \)
- **Square**: \( S = a^2 \)
- **Triangle**: \( S = \sqrt{p \cdot (p-a) \cdot (p-b) \cdot (p-c)} \) where \( p \) is the semi-perimeter.

### Perimeter
- **Circle**: \( P = 2\pi R \)
- **Square**: \( P = 4a \)
- **Triangle**: \( P = a + b + c \)

## Function Descriptions

### `calc(fig, func, size)`

Calculates the specified function (area or perimeter) for the given figure (circle or square).

- **Args**:
  - `fig` (str): The name of the figure. Must be either 'circle' or 'square'.
  - `func` (str): The function to calculate. Must be either 'perimeter' or 'area'.
  - `size` (list): A list of dimensions required for the calculation (e.g., radius for circle).

### `circle.area(r)`

Calculates the area of a circle given its radius.

- **Args**:
  - `r` (float): The radius of the circle.
- **Returns**: The area of the circle (float).

### `circle.perimeter(r)`

Calculates the perimeter (circumference) of a circle given its radius.

- **Args**:
  - `r` (float): The radius of the circle.
- **Returns**: The perimeter of the circle (float).

### `square.area(a)`

Calculates the area of a square given its side length.

- **Args**:
  - `a` (float): The length of the side of the square.
- **Returns**: The area of the square (float).

### `square.perimeter(a)`

Calculates the perimeter of a square given its side length.

- **Args**:
  - `a` (float): The length of the side of the square.
- **Returns**: The perimeter of the square (float).

### `triangle.area(a, b, c)`

Calculates the area of a triangle using the semi-perimeter formula.

- **Args**:
  - `a` (float): Length of the first side.
  - `b` (float): Length of the second side.
  - `c` (float): Length of the third side.
- **Returns**: The area of the triangle (float).

### `triangle.perimeter(a, b, c)`

Calculates the perimeter of a triangle given the lengths of its sides.

- **Args**:
  - `a` (float): Length of the first side.
  - `b` (float): Length of the second side.
  - `c` (float): Length of the third side.
- **Returns**: The perimeter of the triangle (float).

## Change History

- **Commit Hash**: `d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71` - Add calculate.py
- **Commit Hash**: `51c40ebfd0e0b65f52fe5e54740cbb038e492db3` - Doc updated for triangle
- **Commit Hash**: `d080c7888b81955bad2ed78d58ad910526b5132a` - Triangle added
- **Commit Hash**: `d078c8d9ee6155f3cb0e577d28d337b791de28e2` - Docs added
- **Commit Hash**: `8ba9aeb3cea847b63a91ac378a2a6db758682460` - Circle and square added
