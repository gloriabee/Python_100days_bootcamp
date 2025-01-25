import os
users={}
bids=[]
isEnd=False
while not isEnd:
   name=input('What is your name?: ')
   bid=int(input('What\'s your bid?: $'))
   users[name]=bid
   for name in users:
      bids.append(users[name])
   maxBid=max(bids)
   for name in users:
      if users[name]==maxBid:
         winner=name
   decision=input('If other users who want to bid? ').lower()
   if decision=='yes':
      os.system('cls')
      isEnd=False
   else:
      isEnd=True
print(f'The winner is {winner} with a bid of {maxBid}')  
   

   


