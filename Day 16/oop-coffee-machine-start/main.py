from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    user_input = (input(f"What would you like? {menu.get_items()}: ")).lower()
    if user_input == "off":
        is_machine_on = False
        continue

    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    menu_item_ordered = menu.find_drink(user_input)
    if menu_item_ordered is not None:
        make_drink = coffee_maker.is_resource_sufficient(menu_item_ordered)
        if make_drink:
            customer_paid = money_machine.make_payment(menu_item_ordered.cost)
            if customer_paid:
                coffee_maker.make_coffee(menu_item_ordered)