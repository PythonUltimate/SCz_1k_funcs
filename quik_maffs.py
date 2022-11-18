import math


## Basic maths

def summation(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def floor_division(a, b):
    return a // b


def exponent(a, b):
    return a ** b


def square_root(a):
    return math.sqrt(a)


def linear_function(x, a, b):
    return a * x + b


def quadratic_equation(x, a, b):
    return x ** 2 + a * x + b


def factorial_num(x):
    return math.factorial(x)


def triangle_perimeter(a, b, c):
    return a + b + c


def triangle_equilateral_perimeter(a):
    return a ** 2 * math.sqrt(3) / 4


def triangle_area(a, height):
    return 0.5 * a * height


def triangle_equilateral_height(a):
    return a * math.sqrt(3) / 2


def triangle_longest_side(short_side):
    return 2 * short_side


def triangle_middle_side(short_side):
    return short_side * math.sqrt(3)


def rectangle_perimeter(a, b):
    return 2 * a + 2 * b


def square_perimeter(a):
    return 4 * a


def square_area(a):
    return a ** 2


def square_diagonal(a):
    return a * math.sqrt(2)


def rhomboid_perimeter(a, b):
    return 2 * a + 2 * b


def rhomboid_area(a, h):
    return a * h


def deltoid_area(diameter1, diameter2):
    return 0.5 * diameter1 * diameter2


def trapezoid_perimeter(a, b, c, d):
    return a + b + c + d


def trapezoid_area(a, b, height):
    return (a + b) * height / 2


def arc_length(alpha, r):
    return alpha / 360 * 2 * math.pi * r


def arc_area(alpha, r):
    return alpha / 360 * math.pi * r ** 2


def circle_area(r):
    return math.pi * r ** 2


def circle_perimeter(r):
    return 2 * math.pi * r


def circle_diameter(perimeter):
    return perimeter / math.pi


def count_pi(perimeter, diameter):
    return perimeter / diameter


def hexogon_perimeter(a):
    return 6 * a ** 2 * math.sqrt(3) / 4


def cuboid_volume(a, b, c):
    return a * b * c


def cuboid_area(a, b, c):
    return 2 * a * b + 2 * a * c + 2 * b * c


def cuboid_diagonal(a, b, c):
    return math.sqrt(a ** 2 + b ** 2 + c ** 2)


def cuboid_base_diagonal(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def cube_volume(a):
    return a ** 3


def cube_area(a):
    return 6 * a ** 2


def cube_base_diagonal(a):
    return a * math.sqrt(2)


def cube_diagonal(a):
    return a * math.sqrt(3)


def prism_volume(base_area, height):
    return base_area * height


def prism_area(base_area, side_area):
    return 2 * base_area + side_area


def pyramid_volume(base_area, height):
    return 1 / 3 * base_area * height


def pyramid_area(base_area, side_area):
    return base_area * side_area


def tetrahedron_area(a):
    return a ** 2 * math.sqrt(3)


def tetrahedron_volume(a):
    return a ** 3 * math.sqrt(2) / 12


def tetrahedron_height(a):
    return a * math.sqrt(6) / 3


def cylinder_volume(r, height):
    return math.pi * r ** 2 * height


def cylinder_area(r, height):
    return 2 * math.pi * r ** 2 + 2 * math.pi * r * height


def sphere_volume(r):
    return 4 / 3 * math.pi * r ** 3


def sphere_area(r):
    return 4 * math.pi * r ** 2


def pitagoras_equation(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c


def tales_law(x, y, k):
    l = k * x / y
    return l


def change_to_percentage(division):
    return f'{division * 100}%'


def change_to_num_by_proportion(value, base):
    return f'{100 * value / base}%)'


def increase_by_percent(base_value, percent):
    return (percent / 100 + 1) * base_value


def decrease_by_percent(base_value, percent):
    return (1 - percent / 100) * base_value
