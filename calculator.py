"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

import arithmetic
from functools import reduce


while True:
    input_str = input("> ")
    input_list = input_str.split(" ")

    if input_list[0] == 'q': 
        quit()
    else:
        solution = 0
        float_list = []

        try:
            num1 = 12
            for num in input_list[1:]:
                float_list.append(float(num))            
        except ValueError as e:
            print("You entered an invalid input. Please make sure all your inputs are numbers.")
            continue

        #if len(input_list) > 2:
        #    try:
        #        num2 = float(input_list[2])
        #    except ValueError as e:
        #        print("Invalid input. Please enter a number.")
        #        continue

        num2 = 10

        if input_list[0] == '+':
            #solution = arithmetic.add(num1, num2)
            solution = reduce(lambda x, y: arithmetic.add(x,y), float_list)
        elif input_list[0] == '-': 
            #solution = arithmetic.subtract(num1, num2)
            solution = reduce(lambda x, y: arithmetic.subtract(x,y), float_list)
        elif input_list[0] == '*':
            #solution = arithmetic.multiply(num1, num2)
            solution = reduce(lambda x, y: arithmetic.multiply(x,y), float_list)
        elif input_list[0] == '/':
            #solution = arithmetic.divide(num1, num2)
            solution = reduce(lambda x, y: arithmetic.divide(x,y), float_list)
        elif input_list[0] == 'square':
            solution = arithmetic.square(float_list[0])
        elif input_list[0] == 'cube':
            solution = arithmetic.cube(float_list[0])
        elif input_list[0] == 'pow':
            solution = arithmetic.power(num1, num2)
        elif input_list[0] == 'mod':
            solution = arithmetic.mod(num1, num2)

        else:
            print("Not a valid arithmetic operator. Please enter a real one.")
            continue

        print(solution)

        

    

# Your code goes here
