from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_machine = CoffeeMaker()
my_coffee_menu = Menu()
my_coffe_money = MoneyMachine()
#selected_item = MenuItem()

is_on = True

while is_on:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == "off":
        is_on = False
    elif selection == "report":
        my_coffee_machine.report()
        my_coffe_money.report()
    else:
        selected_item = my_coffee_menu.find_drink(selection)
        if selected_item:
            if my_coffee_machine.is_resource_sufficient(selected_item):
                print(f"Please pay ${selected_item.cost} for your {selection}.")
                if my_coffe_money.make_payment(selected_item.cost):
                    my_coffee_machine.make_coffee(selected_item)
            

