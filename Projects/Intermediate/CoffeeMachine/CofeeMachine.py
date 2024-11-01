from machine_data import MENU, resources

selection = ""
money = 0

def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: {money}")
    print("")

def enough_resources(user_selection):
    # Get required ingredients for selection
    sel_water = MENU[user_selection]["ingredients"]["water"]
    # Drink may not require milk
    if "milk" in MENU[user_selection]["ingredients"]:
        sel_milk = MENU[user_selection]["ingredients"]["milk"]
    else:
        sel_milk = 0
    sel_coffee = MENU[user_selection]["ingredients"]["coffee"]
    # Check if there's enough resources for selection
    enough_water = resources["water"] - sel_water >= 0
    if not enough_water:
        print("Sorry there is not enough water")
    enough_milk = resources["milk"] - sel_milk >= 0
    if not enough_milk:
        print("Sorry there is not enough milk")
    enough_coffee = resources["coffee"] - sel_coffee >= 0
    if not enough_coffee:
        print("Sorry there is not enough water")
    return enough_water and enough_milk and enough_coffee

def process_payment(user_selection):
    cost = MENU[user_selection]["cost"]
    print(f"Please pay ${cost} for your {user_selection}.")
    print("How would you like to pay:")
    quarters = int(input("quarters : "))
    dimes = int(input("dimes : "))
    nickels = int(input("nickels : "))
    pennies = int(input("pennies : "))
    payment = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if payment < cost:
        print("Sorry that's not enough money. Money Refunded")
        return 0
    else:
        return payment
    
def process_refund(selection_cost, user_payment):
    change = round(user_payment - selection_cost, 2)
    if change > 0:
        print(f"Here is ${change} dollars in change.")

def make_coffee(user_selection):
    # Get required ingredients for selection
    sel_water = MENU[user_selection]["ingredients"]["water"]
    # Drink may not require milk
    if "milk" in MENU[user_selection]["ingredients"]:
        sel_milk = MENU[user_selection]["ingredients"]["milk"]
    else:
        sel_milk = 0
    sel_coffee = MENU[user_selection]["ingredients"]["coffee"]
    # Deplete resources
    resources["water"] -= sel_water
    resources["milk"] -= sel_milk
    resources["coffee"] -= sel_coffee

while selection != "off":
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Check if option is part of the menu
    if selection == "off":
        break
    if selection == "report":
        report()
    elif selection not in MENU:
        print(f"Sorry there's no {selection}. Please choose someting else.")
    else:
        if enough_resources(selection):
            payment = process_payment(selection)
            if payment > 0:
                cost = MENU[selection]["cost"]
                money += cost
                process_refund(cost,payment)
                make_coffee(selection)
                print(f"Here is your {selection}. Enjoy!!!\n")