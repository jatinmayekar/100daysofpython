import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for i in range(0,nr_letters):
    rl = random.randint(0, len(letters) - 1)
    password += letters[rl]
for i in range(0,nr_letters):
    rs = random.randint(0,len(symbols)-1)
    password += symbols[rs]
for i in range(0,nr_letters):
    rn = random.randint(0, len(numbers)-1)
    password += numbers[rn]
print(password)
p = list(password)
random.shuffle(p)
ps = "".join(p)
print(ps)
pss = ""
for c in p:
    pss += c
print(pss)
