"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *




# Your code goes here
# add(float, float) → float
# Return the sum of the two inputs.
# subtract(float, float) → float
# Return the second number subtracted from the first.
# multiply(float, float) → float
# Multiply the two inputs together and return the result.
# divide(float, float) → float
# Divide the first input by the second and return the result.
# square(float) → float
# Return the square of the input.
# cube(float) → float
# Return the cube of the input.
# power(float, float) → float
# Raise the first input to the power of the second and return the result.
# mod(float, float) → float
# Divide the first input by the second input and return the remainder.


# # No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

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

		

