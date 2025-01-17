# Treasure Island Game

print("Welcome to Treasure Island.\n Your mission is to find the treasure. \n You're at across road. Where do you want to go?\n")
direction=input(' Type \"left\" or \"right\"\n')
if(direction=='left'):
    print("You've come to a lake. There is an island in the middle of the lake.")
    action=input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if(action=='wait'):
        print('You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue.')
        color=input('Which color do you choose?\n')
        if(color=='red'):
            print("It's a room full of fire. Game Over.")
        elif(color=='blue'):
            print('You enter a room of beasts. Game Over')
        elif(color=='yellow'):
            print('You found the treasure! You Win!')
    else:
        print('You get attacked by an angry trout. Game Over.')
else:
    print('You fell into a hole. Game Over')