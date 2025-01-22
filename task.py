# Start
import random

from hangman_words import word_list
from hangman_art import stages,logo

print(logo)
#Todo-1 Randomly Choose a word from the word_list and assignment
random_word=random.choice(word_list)


#Todo-2 Ask the user to guess a letter and assign their answer
placeholder='Word to guess: '
for position in range(len(random_word)):
    placeholder+='_'
print(placeholder)

        
game_over=False
correct_letters=[]
life=6

while not game_over:
   
   guess=input('Guess a letter: ').lower()
   if guess in correct_letters:
       print(f"You've already guessed {guess}")
   display="Word to guess: "
   for letter in random_word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
   print(display)
   
   if guess not in random_word:
       life-=1
       print(f"You guessed {guess}, that is not in the word. You lose a life.")
       if life==0:
            game_over=True
            print(f"You wrong! That was {letter}")
   if "_" not in display:
        game_over=True
        print("You win.")
   print('You have left ',life,' lives ')
   print(stages[life])


  

