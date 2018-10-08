print('Operations now available: "+", "-", "*", "/", "sqrt", "^"')
import math


number_1 = float(input("Enter the number one "))

operation = input("Enter opertation ")
if operation == "sqrt":
	print("\n", "sqrt(",number_1,") =", math.sqrt(number_1))
else:
	number_2 = float(input("Enter the number two "))
	print("\n", number_1, operation, number_2, "=", end=" ")

if operation == "+":
	print( number_1 + number_2 )
elif operation == "-":
	print( number_1 - number_2 )
elif operation == "*":
	print( number_1 * number_2 )
elif operation == "/":
	print( number_1 / number_2 )
elif operation == "^":
	print( number_1**number_2 )
elif operation == "sqrt":
	pass
else:
	print("Please enter the correct operation")
