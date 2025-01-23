import string
def cipher(choice):
   msg=input('Type your message:\n')
   shift=int(input('Type the shift number:\n'))
   if(choice=='encode'):
    print("Here's the encoded result: ")
   else:
    print("Here's the decoded result: ") 

alphabet=string.ascii_lowercase+string.ascii_uppercase+string.punctuation
choice=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n")
isEnd=False
while not isEnd:
  cipher(choice)
  decision=input("Type 'yes' if you want to go again, Otherwise type 'no'\n")
  if(decision=='no'):
    isEnd=True
  else:
    isEnd=False

print(alphabet)
    



