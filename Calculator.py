import math

shape = 0

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

def calculate_addition(number1, number2):
    return number1 + number2

def calculate_subtraction(number1, number2):
    return number1 - number2

def calculate_multiplication(number1, number2):
    return number1 * number2

def calculate_division(number1, number2):
    return number1 / number2

def calculate_exponent(number1, number2):
    return number1 ** number2

def calculate_square_root(number1):
    return number1 ** 0.5

while True:
    action = input("Enter 'area', 'perimeter', 'addition', 'subtraction', 'multiplication', 'division', 'exponents' or 'square root' (or 'exit' to quit): ").lower()

    if action == 'exit':
        break
    if action == "area" or action == "perimeter":
        shape = input("Enter 'circle', 'triangle', 'square', or 'rectangle' (or 'exit' to quit): ").lower()
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
    if action == "area" or action == "perimeter":
        print(f"The {action} of the {shape} is: {result}")

    elif action == "addition":
        number1 = float(input("What is the first number you want to add: "))
        number2 = float(input("What is the second number you want to add: "))
        result = calculate_addition(number1, number2)
        print(result)
    
    elif action == "subtraction":
        number1 = float(input("What is the first number you want to subtract: "))
        number2 = float(input("What is the second number you want to subtract: "))
        result = calculate_subtraction(number1, number2)
        print(result)

    elif action == "multiplication":
        number1 = float(input("What is the first number you want to multiply: "))
        number2 = float(input("What is the second number you want to multiply: "))
        result = calculate_multiplication(number1, number2)
        print(result)
        
    elif action == "division":
        number1 = float(input("What is the first number you want to divide: "))
        number2 = float(input("What is the second number you want to divide: "))
        result = calculate_division(number1, number2)
        print(result)
    elif action == "exponents":
        number1 = float(input("What is the first number you want to use: "))
        number2 = float(input("What number do you want to raise the first number to the power of: "))
        result = calculate_exponent(number1, number2)
        print(result)
    elif action == "square root":
        number1 = float(input("What is the number you want to find the square root of: "))
        result = calculate_square_root(number1)
        print(result)



