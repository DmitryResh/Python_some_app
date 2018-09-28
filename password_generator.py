import random 

list_of_numbers = list(range(10))

list_of_letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list_of_signs = ["!", "^", "/", "?"]

list_of_values = list_of_numbers+list_of_letters+list_of_letters_upper+list_of_signs+list_of_signs

shuffle_1 = random.shuffle(list_of_values)

shuffle_2 = random.shuffle(list_of_values)

for num in list_of_values[0:10]:
	print(num, end="")