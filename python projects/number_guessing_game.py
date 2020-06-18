import random

answer = 'y'

while answer == 'y':
    num = random.randint(1,20)
    ans = 'y'
    
    print('NUMBER GUESSING GAME!')
    print('Guess the number we have chosen between 1 and 20')
    
    while ans == 'y':
        x = input()
        
        while type(x) != int:
            try:
                x = int(x)
                print(x)
            except ValueError:
                print('That\'s not a number. Try again.' )
                x = input()
        
        if x == num:
            print('You got it!')
            ans = 'n'
        elif x < num:
            print('Too low! Try again?(y/n)')
            ans = input().lower()   
            print(ans)
        else:
            print('Too high! Try again?(y/n)')
            ans = input().lower()
            print(ans)
    print('Play again?(y/n)')
    answer = input().lower()