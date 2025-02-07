#Display Art
from game_art import logo
from game_art import vs
from game_data import data;
import random;

print(logo)


#Generate a random account from the game data
account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)

def check_answer(user_guess,a_followers,b_followers):
   if a_followers>b_followers:
       return user_guess=='a'
   else: 
       return user_guess=='b'
   
game_should_continue=True
score=0
while game_should_continue:
    #format the account data into printable format
    print(f"Compare A: {account_a["name"]},{account_a["description"]}, from {account_a["country"]}")
    print(vs)
    print(f"Compare B: {account_b["name"]},{account_b["description"]}, from {account_b["country"]}")


    #Ask the user for a guess:
    guess=input('Who has more followers? Type "A" or "B"').lower()

    #Checking if user is correct or wrong
        ## Get follower count of each account
        ## use if statement to check if user is correct
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    # Give user feedback on their guess. 
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    
    
        
    #score keeping
    if is_correct:
        account_a=account_b
        account_b=random.choice(data)
        score+=1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        game_should_continue=False
        
#make the game repeatable. 

#making account at position B become the next account at position A

