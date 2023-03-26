#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#ordered = nr_letters + nr_symbols + nr_numbers

password = ""
# Get one random letter for the amount user specified
for i in range(0,nr_letters):
    password += random.choice(letters)
for i in range(0,nr_symbols):
    password += random.choice(symbols)
for i in range(0,nr_numbers):
    password += random.choice(numbers)
print("Password Easy: ",password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

### Creates a randomized version of the password above ###
randomized_password = ""
password2 = list(password)
#for i in password:
#    password2.append(i)
random.shuffle(password2)
for i in password2:
    randomized_password += i
print("Password Hard: ",randomized_password)


# Use a list to make password
password3 = []

for i in range(0,nr_letters):
    password3.append(random.choice(letters))
for i in range(0,nr_symbols):
    password3.append(random.choice(symbols))
for i in range(0,nr_numbers):
    password3.append(random.choice(numbers))
    
random.shuffle(password3)
password3_random = ""
for i in password3:
    password3_random += i
print(f"Different Ordered Hard: {password3_random}")