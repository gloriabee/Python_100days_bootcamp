import string
alphabet=string.ascii_lowercase+string.ascii_uppercase+string.punctuation

# encrypt function
def encrypt(msg,shift):
  cipher_text=""
  for char in msg:
    shifted_position=alphabet.index(char)+shift
    shifted_position%=len(alphabet)
    cipher_text+=alphabet[shifted_position]
  print(f"Here is the encoded result: {cipher_text}")


# decrypt 
def decrypt(msg,shift):
   cipher_text=""
   for char in msg:
      shifted_position=alphabet.index(char)-shift
      cipher_text+=alphabet[shifted_position]
   print(f"Here is the decoded result: {cipher_text}")


isEnd=False
while not isEnd:
     choice=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
     msg=input('Type your message:\n').lower()
     shift=int(input('Type the shift number:\n'))
     if(choice=='encode'):
        encrypt(msg,shift)
     else:
        decrypt(msg,shift)
     decision=input("Type 'yes' if you want to go again, Otherwise type 'no'\n")
     if(decision=='no'):
        isEnd=True
     else:
        isEnd=False

    



