
def life_in_weeks(age):
    left_years=90-age
    left_weeks=left_years*52
    print(f'You have {left_weeks} weeks left.')

age=int(input('Enter your current age: '))
life_in_weeks(age)

