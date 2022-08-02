from menu import *
MONEY = 0


def start():
    """Start the machine"""
    print("What would you like?", end=" ")
    option = input("(espresso/latte/cappuccino): ").lower()
    if option == "report":
        report()
        start()
    elif option == "off":
        return
    elif option == "latte" or option == "cappuccino" or option == "espresso":
        if resources["water"] < MENU[option]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            start()
        elif option != "espresso" and (resources["milk"] <
                                       MENU[option]["ingredients"]["milk"]):
            print("Sorry there is not enough milk.")
            start()
        elif resources["coffee"] < MENU[option]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            start()
        else:
            coffee(option)
            start()


def report():
    """Print a report of coffee machines' status"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml",
          f"\nCoffee: {coffee}g\nMoney: ${MONEY}")


def coffee(drink):
    """Make the drink the user chose"""
    cost = MENU[drink]["cost"]
    print(f"That will be {cost}")
    total = coins()
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        start()
    print(f"Here is ${round(total - cost, 2)} in change.")
    print(f"Here is your {drink} ☕. Enjoy!")
    update_resources(drink)
    global MONEY
    MONEY += cost


def coins():
    """Recieve user coins"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01


def update_resources(drink):
    """Update the resources of coffee machine"""
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


start()
