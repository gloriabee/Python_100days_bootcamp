import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number=random.randint(1,100)
print(f"The correct answer is {random_number}")
level=input("Choose a difficulty. Type 'easy' or 'hard':").lower()

def checkNum(life):
    isEnd=False
    while not isEnd and life>0:
        print(f"You have {life} attempts remaining to guess the number.")
        guess=int(input('Make a guess: '))
        if(guess<random_number):
            print('Too Low.')
            life-=1
            print('Guess again.')
        elif(guess>random_number):
            print('Too high')
            life-=1
            print('Guess again.')
        elif(guess==random_number):
            print(f"You got it! The answer was {random_number}")
            isEnd=True
        else:
            print('You lost')

    
if level=='easy':
    life=10
    checkNum(life)
elif level=='hard':
    life=5
    checkNum(life)
else:
    print('Chose wrong level:')
