import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
password_list = []

if nr_letters > 0:
    for n in range(1,nr_letters+1):
        password += random.choice(letters)
        password_list.append(random.choice(letters))
if nr_symbols > 0:
    for n in range(1,nr_symbols+1):
        password += random.choice(symbols)
        password_list.append(random.choice(symbols))
if nr_numbers > 0:
    for n in range(1,nr_numbers+1):
        password += random.choice(numbers)
        password_list.append(random.choice(numbers))

print(f"Easy Password : {password}")

# ------ Convert to Hard Password ------

# Convert the password to list
password_as_list_of_chars = list(password)

# Shuffle the list
random.shuffle(password_as_list_of_chars)
random.shuffle(password_list)

# Convert the list to string
new_password = "".join(map(str,password_as_list_of_chars))
new_password_list = "".join(map(str,password_list))

print(f"Hard Password(from string) : {new_password}")
print(f"Hard Password(list only): {new_password_list}")
