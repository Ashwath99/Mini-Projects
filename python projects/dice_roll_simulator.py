import random

print('Do you want to roll a pair of dice?')
ans = input().lower()

def rollDice():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    print(f"You rolled a {num1} and a {num2}!")
    print('Do you want to roll again?')
    ans = input().lower()
    return ans

while ans == 'yes':
    ans = rollDice()

print('Thanks for playing!')