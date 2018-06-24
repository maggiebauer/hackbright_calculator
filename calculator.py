"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
	input_string = input(">")
	token = input_string.split(" ")

	if token[0] ==  "q":
		print ("Exiting calculator")
		break

	if token[0] == "+":
		print(add(float(token[1]), float(token[2])))

	if token[0] == "-":
		print(subtract(float(token[1]), float(token[2])))

	if token[0] == "*":
		print(multiply(float(token[1]), float(token[2])))

	if token[0] == "/":
		print(divide(float(token[1]), float(token[2])))

	if token[0] == "square":
		print(square(float(token[1])))

	if token[0] == "cube":
		print(cube(float(token[1])))

	if token[0] == "pow":
		print(pow(float(token[1]), float(token[2])))

	if token[0] == "mod":
		print(mod(float(token[1]), float(token[2])))

