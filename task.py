#BMI Calculator with Interpretations

weight=float(input('Enter your weight\n'))
height=float(input('Enter your height\n'))
bmi=weight/(height**2)
if bmi>=25:
    print('overweight')
elif bmi>=18.5:
    print('normal weight')
else:
    print('underweight')