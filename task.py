height=int(input('Enter your height'))
if(height>120):
    print('can ride')
    pay=0
    age=int(input('Enter your age'))
    if(age>18):
        pay+=12
    elif(age>12):
        pay+=7
    else:
        pay+=5
    photo=input('Want photos?')
    if(photo=='yes'):
        pay+=3
        print('The total pay is $',pay)

    print('The total pay is $',pay)   
else:
    print("can't ride")