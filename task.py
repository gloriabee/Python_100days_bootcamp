import os
users={}
bids=[]
isEnd=False
#Solution 2
def find_highest_bidder(bidding_dictionary):
   highest_bid=0
   for bidder in bidding_dictionary:
      bid_amount=bidding_dictionary[bidder]
      if bid_amount>highest_bid:
         highest_bid=bid_amount
         winner=bidder
   print(f'The winner is {winner} with a bid of {highest_bid}')  
   

while not isEnd:
   # Ask the user for input
   name=input('What is your name?: ')
   bid=int(input('What\'s your bid?: $'))
   # Save data into dictionary
   users[name]=bid
   # Whether if new bids need to be added
   decision=input('If other users who want to bid? ').lower()
   if decision=='yes':
      os.system('cls')
   else:
      os.system('cls')
      isEnd=True
      find_highest_bidder(users)

   

   
   


