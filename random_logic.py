import random

print("Welcome To The My Randomiser \nSet The Range Of Random Number")

enter_max = int(input("Enter maximum "))

enter_min = int(input("Enter minimum "))

if enter_max <= enter_min:
	raise SystemExit("Maximum value must be more than Minimum")

number = int(random.uniform(enter_min, enter_max))
print(number)
