import os
def add(num1,num2):
   num1=num1+num2
   return num1
def sub(num1,num2):
   num1=num1-num2
   return num1
def mul(num1,num2):
   num1= num1*num2
   return num1
def div(num1,num2):
   num1=num1/num2
   return num1

logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ '.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ '.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''
print(logo)
result=0

isContinue=True
while isContinue:
   #Asking first number
   num1=int(input("What's the first number?: "))
   isEnd=False
   while not isEnd:
      #Asking operator
      print('+\n-\n*\n/\n')
      operation=input('pick an operation: ')
      #Asking second number
      num2=int(input("What's the next number: "))
      if(operation=='+'):
         result=add(num1,num2)
      elif(operation=='-'):
         result=sub(num1,num2)
      elif(operation=='*'):
         result=mul(num1,num2)
      else:
         result=div(num1,num2)
      print(f"{num1} {operation} {num2} = {result}")
      num1=result
      decision=input("Type 'y' to continue calculating with 15.0 or type 'n' to start a new calculation: ").lower()
      if decision=='n':
         isEnd=True
         os.system('cls')
      else:
         isContinue=True


