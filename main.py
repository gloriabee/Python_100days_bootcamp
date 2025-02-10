MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0 

isGameContinue=True
while isGameContinue:
    choice=input('What would you like? (expresso/latte/cappuccino):')
    if(choice=='report'):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice=='espresso':
        print('espresso')
    elif choice=='latte':
        print('latte')
    elif choice=='cappuccino':
        print('cappuccino')
    elif choice=='close':
        print('System Closed')
        isGameContinue=False
