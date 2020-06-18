import random

print('ROCK PAPER SCISSORS!')

moves = ['rock', 'paper', 'scissors']

def roundWinner(name, user_act, cs_act, user_score, cs_score):
    if user_act == 'rock' and cs_act == 'scissors':
        user_score += 1
    elif user_act == 'paper' and cs_act == 'rock':
        user_score += 1
    elif user_act == 'scissors' and cs_act == 'paper':
        user_score += 1
    elif user_act == 'rock' and cs_act == 'paper':
        cs_score += 1
    elif user_act == 'paper' and cs_act == 'scissors':
        cs_score += 1
    elif user_act == 'scissors' and cs_act == 'rock':
        cs_score += 1
    print(f"{name}: {user_score} - computer: {cs_score}")
    return user_score, cs_score

def rpsWinner(score1, score2):
    if score1 > score2:
        print('Congrats! You win!')
    elif score2 > score1:
        print('Bad luck! you lost!')
    else:
        print('It\'s a draw!')

ans = 'y'
print('Enter your name')
u_name = input()
print(f"Hello {u_name}!")

while ans == 'y':
    u_score = 0
    c_score = 0
    print('How many rounds do you want?')
    num = input()
    
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print('Invalid option, enter a number')
            num = input()
    
    print('START!')
    for i in range(num):
        print('Enter rock, paper or scissors')
        act = input().lower()
    
        while act not in moves:
            print('Invalid. Enter rock, paper or scissors')
            act = input().lower()
        u_score, c_score = roundWinner(u_name, act, random.choice(moves), u_score, c_score)
        
    rpsWinner(u_score, c_score)
    print('Play again?(y/n)')
    ans = input().lower()