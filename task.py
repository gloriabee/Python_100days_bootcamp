# BMI Calculator

# weight=float(input('Enter your weight\n'))
# height=float(input('Enter your height\n'))
# bmi=weight/(height**2)
# print('BMI is ', bmi)


#Tip Calculator

print('Welcome to the tip calculator!')
total=float(input('What was the total bill? $'))
tip=float(input('How much tip would you like to give?'))
people=int(input('How many people to split the bill?'))
result=(total+(total*0.12))/people
print('Each person should pay: $',round(result,2))

