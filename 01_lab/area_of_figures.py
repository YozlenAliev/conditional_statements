from math import pi

figure_type = input()
result = ""

if figure_type == "square":
    square = float(input())
    result = square ** 2
elif figure_type == "rectangle":
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif figure_type == "circle":
    radius = float(input())
    result = pi * radius ** 2
elif figure_type == "triangle":
    side_lenght = float(input())
    side_height = float(input())
    result = side_height * side_lenght / 2

print("%.3f" % result)
