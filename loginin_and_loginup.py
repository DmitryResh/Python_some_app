import sys

dict_1 = {"Dima": "012345", "Ivan": "ssf1d23", "Artur": "434sfs", "Egor": "543210"}

add_login = input("Create a new login: ")

length_login = len(add_login)

if length_login < 3:
	print("Login must contain at least 3 characters")
	sys.exit()
elif add_login in dict_1.keys():
	print("Login already exist")
	sys.exit()
elif add_login.isspace() == True:
	print("Login must contain characters")
	sys.exit()
else:
	add_password = input("Create a new password: ")


length_password = len(add_password)

if length_password < 6:
	print("Password must contain at least 5 characters")
	sys.exit()
elif add_password.isspace() == True:
	print("Login must contain characters")
	sys.exit()
else: 
	dict_1[add_login] = add_password

b = input("Enter your login: ")

if b in dict_1.keys():
	a = input("Enter password: ")
	if dict_1[b] == a:
		print("Hello", b)
	else: print("Uncorrect password")
else: print("Invalid login")
