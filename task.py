import random
import os

# Create a deal_card() function that uses the List below to return a random card
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)
    
# calculate_score()
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return 'draw'
    elif computer_score==0:
        return "Lose,opponent has Blackjack"
    elif user_score==0:
        return "Win With a blackjack"
    elif user_score>21:
        return "You went over, You lose"
    elif computer_score>21:
        return "Opponent went over. You win"
    elif user_score>computer_score:
        return 'You win'
    else:
        return 'You lose'

## Deal user and computer 2 cards
def playGame():
      user_cards=[]
      computer_cards=[]
      computer_score=-1
      user_score=-1
      isGameOver=False

      for _ in range(2):
         user_cards.append(deal_card())
         computer_cards.append(deal_card())

      while not isGameOver: 
         user_score=calculate_score(user_cards)
         computer_score=calculate_score(computer_cards)
         print(f"Your cards {user_cards}, current score: {user_score}")
         print(f"Computer's first cards: {computer_cards[0]}")
         if user_score==0 or computer_score==0 or user_score>21:
            isGameOver=True
         else: 
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal=='y':
               user_cards.append(deal_card())
            else:
               isGameOver=True

      while computer_score!=0 and computer_score<17:
         computer_cards.append(deal_card())
         computer_score=calculate_score(computer_cards)

      print(f"Your Final Hand: {user_cards}, final score: {user_score}")
      print(f"Computer's Final Hand: {computer_cards}, final score: {computer_score}")
      print(compare(user_score,computer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n':")=="y":
    os.system('cls')
    playGame()
