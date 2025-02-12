MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def enough_ingredients(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def insert_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def enough_money(cash_coins, drink_cost):
    if cash_coins >= drink_cost:
        change = round(cash_coins-drink_cost, 2)
        print(f"Here is {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry thats not enough money. Money refunded.")
        return False

def make_coffee(drink_name, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {drink_name}, enjoy!!")

machine_on = True

while machine_on:
    a = input("What would you like? (espresso/latte/cappuccino): ")
    if a == "off":
        machine_on = False
    elif a == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[a]
        if enough_ingredients(drink["ingredients"]):
            cash = insert_coins()
            if enough_money(cash, drink["cost"]):
                make_coffee(a, drink["ingredients"])
