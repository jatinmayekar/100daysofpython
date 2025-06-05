import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to rock paper scissors game\n")
num1 = int(input("Choose : 0 for Rock, 1 for Paper, 2 for Scissors\n"))
if num1 >= 0 and num1 <= 2:
    if num1 == 0:
        print(f"Rock\n {rock}")
    elif num1 == 1:
        print(f"Paper\n {paper}")
    elif num1 == 2:
        print(f"Scissors\n {scissors}")
        
    print("I choose: \n")
    num2 = random.randint(0,2)
    if num2 == 0:
        print(f"Rock\n {rock}")
    elif num2 == 1:
        print(f"Paper\n {paper}")
    elif num2 == 2:
        print(f"Scissors\n {scissors}")

    if (num1 == 0 and num2 == 2) or (num1 == 2 and num2 == 1) or (num1 == 1 and num2 == 0):
        print("\nYou win!")
    elif (num1 == 2 and num2 == 0) or (num1 == 1 and num2 == 2) or (num1 == 0 and num2 == 1):
        print("\nI win!")
    elif num1 == num2:
        print("\nDraw")
else:
    print("invalid choice. GAME OVER")
