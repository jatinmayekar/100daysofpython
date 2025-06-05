import random

print("Coin flip toss\n")
num = random.randint(1,100)
if num % 2 == 0:
    print("Heads")
else:
    print("Tails")