"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

print("""
Welcome to the sassy calculator. Please use this format when using me.

+ 1 2
pow 6
* 3 9

Kthx
		""")

while True:



	input_string = input(">")
	token = input_string.split(" ")
	operators = ["square","cube","mod", "pow","+","-", "*", "/"]


	if token[0] ==  "q":
		print ("Exiting calculator")
		break

	elif token[0] not in operators:
		print("That is not a math operator. Did you even read the first thing I said?")
		continue		

	elif len(token) < 2:
		print("... You're missing something.")
		continue

	elif len(token) == 2:	
		if not token[1].isdigit():
			print ("Uh, that's not even a number. Try to follow directions")
			continue

		elif token[0] == "square":
			print(square(float(token[1])))

		elif token[0] == "cube":
			print(cube(float(token[1])))


		else:
			print("You're missing something, please add another number or use a different operator")
			continue

	elif len(token) == 3:
		if not token[1].isdigit() or not token[2].isdigit():
			print ("Uh oh, someone didn't read what I said in the beginning. You need two numbers for that operator. Duh.")
			continue
		
		elif token[0] == "+":
			print(add(float(token[1]), float(token[2])))

		elif token[0] == "-":
			print(subtract(float(token[1]), float(token[2])))

		elif token[0] == "*":
			print(multiply(float(token[1]), float(token[2])))

		elif token[0] == "/":
			print(divide(float(token[1]), float(token[2])))

		elif token[0] == "pow":
			print(pow(float(token[1]), float(token[2])))

		elif token[0] == "mod":
			print(mod(float(token[1]), float(token[2])))
		else:
			print("That operator doesn't take two numbers. Get it together")			


	elif len(token) > 3:
		print("What are you even doing? That looks nothing like my examples")
		continue

	else:
		print("You broke it, please try harder.")
		continue
