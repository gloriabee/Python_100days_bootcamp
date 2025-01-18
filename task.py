import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
my_choice=int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
com_choice= random.randint(0,2)
if(my_choice==0):
    print(rock)
elif(my_choice==1):
    print(paper)
else:
    print(scissor)
print('Computer choose: ')
if(com_choice==0):
    print(rock)
elif(com_choice==1):
    print(paper)
else:
    print(scissor)

if(my_choice==com_choice):
    print("It's a draw.")
elif((my_choice==0 and com_choice==2) or (my_choice==2 and com_choice==1) or (my_choice==1 and com_choice==0)):
    print('You Win!')
else:
    print('You lose')


