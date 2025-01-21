import random
word_list=['aardvark','baboon','camel']

#Todo-1 Randomly Choose a word from the word_list and assignment
random_word=random.choice(word_list)

i=0
print('word to guess: ',end='')
while i<len(random_word):
    print('-',end='')
    i+=1
print()

#Todo-2 Ask the user to guess a letter and assign their answer
life=1
answer=''

for life in range(6):
 while(answer!=random_word):
    letter=input('Guess a letter:')
    if letter in random_word:
        i=random_word.index(letter)
        answer+=random_word[i]
    else:
        print('wrong')
life-=1



#Todo-3 Check if the letter the user guessed (guess) is one is wrong if