import string
alphabet=string.ascii_lowercase+string.ascii_uppercase+string.punctuation
print(alphabet)
print(len(alphabet))
# choice=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
# msg=input('Type your message:\n')
# shift=int(input('Type the shift number:\n'))

# Todo-1: Create a function called encrypt() that takes 'original_text' and 'shift_amount' as 2 inputs. 
result=''
textList=[]
def encrypt(msg,shift):
  for char in msg:
    currentI=alphabet.index(char)
    nextI=currentI+shift
    if nextI==len(alphabet):
       currentI=len(alphabet)-nextI
       textList.append(alphabet[currentI])
       result=''.join(textList)
    elif nextI>len(alphabet):
       currentI=nextI-len(alphabet)
       textList.append(alphabet[currentI])
       result=''.join(textList)
    else:
        currentI=currentI+shift
        textList.append(alphabet[currentI])
        result=''.join(textList)
  print(result)
  
encrypt('}~}~',1)
# def cipher(choice):
  
#    if(choice=='encode'):
#     print("Here's the encoded result: ")
#    else:
#     print("Here's the decoded result: ") 



# isEnd=False
# while not isEnd:
#   cipher(choice)
#   decision=input("Type 'yes' if you want to go again, Otherwise type 'no'\n")
#   if(decision=='no'):
#     isEnd=True
#   else:
#     isEnd=False
# print(alphabet)
    



