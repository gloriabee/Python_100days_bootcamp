import random
word_list=['aardvark','baboon','camel']

#Todo-1 Randomly Choose a word from the word_list and assignment
random_word=random.choice(word_list)
print(random_word)

i=0
result=''
print('word to guess: ',end='')
while i<len(random_word):
    result+='-'
    i+=1
print(result)

#Todo-2 Ask the user to guess a letter and assign their answer
# life=1
# answer=''

# for life in range(6):
#  while(answer!=random_word):
#     letter=input('Guess a letter:')
#     if letter in random_word:
#         i=random_word.index(letter)
#         answer+=random_word[i]
#         print('Right')
#     else:
#         print('wrong')
# life-=1

guess=input('Guess a letter: ').lower()
print(guess)

result=''
#Todo-3 Check if the letter the user guessed (guess) is one is wrong if
for i,char in enumerate(random_word):
    if char==guess:
         print(char,end='')
    else:
         print('-',end='')


    