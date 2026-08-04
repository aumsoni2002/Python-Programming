import sys

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
    "money": 0.00
}


# TODO: 1. Create a function to show current resource values
def show_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


# TODO: 2. Exit the program with success status code if the input value is 'off'
def turn_off_machine(input_value):
    if input_value == "off":
        sys.exit(0)


# TODO: 3. Create a function to check if the current available resources are sufficient to make the selected drink
def check_resources_sufficient(selected_drink):
    drink_ingredients = MENU[selected_drink]["ingredients"]
    _insufficient_resources = []
    match selected_drink:
        case "espresso":
            if resources["water"] < drink_ingredients["water"]:
                _insufficient_resources.append("water")
            if resources["coffee"] < drink_ingredients["coffee"]:
                _insufficient_resources.append("coffee")
            return _insufficient_resources

        case "latte" | "cappuccino":
            if resources["water"] < drink_ingredients["water"]:
                _insufficient_resources.append("water")
            if resources["coffee"] < drink_ingredients["coffee"]:
                _insufficient_resources.append("coffee")
            if resources["milk"] < drink_ingredients["milk"]:
                _insufficient_resources.append("milk")
            return _insufficient_resources

        case _:
            return _insufficient_resources


# TODO: 4. Create a function to process all coins into dollars
def process_coins(_quarters, _dimes, _nickles, _pennies):
    _quarters = _quarters * 0.25
    _dimes = _dimes * 0.10
    _nickles = _nickles * 0.05
    _pennies = _pennies * 0.01

    _total_dollars = _quarters + _dimes + _nickles + _pennies

    return _total_dollars


# TODO 5:  Create a function to check if money is enough to purchase the drink or not
def check_transaction_successful(_total_dollars, selected_drink):
    _change = 0.00
    _is_enough_money = False
    if _total_dollars >= MENU[selected_drink]["cost"]:
       _change = round(_total_dollars - MENU[selected_drink]["cost"], 2)
       resources["money"] = resources["money"] + MENU[selected_drink]["cost"]
       resources["water"] = resources["water"] - MENU[selected_drink]["ingredients"]["water"]
       resources["coffee"] = resources["coffee"] - MENU[selected_drink]["ingredients"]["coffee"]
       if selected_drink == "latte" or selected_drink == "cappuccino":
           resources["milk"] = resources["milk"] - MENU[selected_drink]["ingredients"]["milk"]

       _is_enough_money = True

    return _is_enough_money, _change

while True:
    user_input = (input("What would you like? (espresso/latte/cappuccino): ")).lower()

    turn_off_machine(user_input)
    if user_input == "reports":
        show_report()
        continue

    insufficient_resources = check_resources_sufficient(user_input)

    if len(insufficient_resources) != 0:
        result = ", ".join(insufficient_resources[:-1]) + ", and " + insufficient_resources[-1] + "."
        print(f"Sorry there is not enough {result}")
        continue

    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    
    total_dollars = process_coins(quarters, dimes, nickles, pennies)
    
    is_enough_money, change = check_transaction_successful(total_dollars, user_input)

    if is_enough_money:
        if change > 0.00:
            print(f"Here is your ${change} change.")

        print(f"Here is your {user_input} ☕️. Enjoy!")

    else:
        print("Sorry that's not enough money. Money refunded.")