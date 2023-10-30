import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_square_area(side_length):
    return side_length**2

def calculate_square_perimeter(side_length):
    return 4 * side_length

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

while True:
    shape = input("Enter 'circle', 'triangle', 'square', or 'rectangle' (or 'exit' to quit): ").lower()

    if shape == 'exit':
        break

    action = input("Enter 'area' or 'perimeter': ").lower()

    if shape == 'circle':
        radius = float(input("Enter the radius: "))
        if action == 'area':
            result = calculate_circle_area(radius)
        elif action == 'perimeter':
            result = calculate_circle_perimeter(radius)
        else:
            result = "Invalid input"
    elif shape == 'square':
        side_length = float(input("Enter the side length: "))
        if action == 'area':
            result = calculate_square_area(side_length)
        elif action == 'perimeter':
            result = calculate_square_perimeter(side_length)
        else:
            result = "Invalid input"
    elif shape == 'rectangle':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        if action == 'area':
            result = calculate_rectangle_area(length, width)
        elif action == 'perimeter':
            result = calculate_rectangle_perimeter(length, width)
        else:
            result = "Invalid input"
    elif shape == 'triangle':
        if action == 'area':
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            result = calculate_triangle_area(base, height)
        elif action == 'perimeter':
            side1 = float(input("Enter the length of side 1: "))
            side2 = float(input("Enter the length of side 2: "))
            side3 = float(input("Enter the length of side 3: "))
            result = calculate_triangle_perimeter(side1, side2, side3)
        else:
            result = "Invalid input"
    else:
        result = "Invalid input"

    print(f"The {action} of the {shape} is: {result}")

