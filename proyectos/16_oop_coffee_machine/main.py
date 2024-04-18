from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Clases
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

# Reportes
coffee_maker.report()
money_machine.report()

# Bucle
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == 'off':
        # apagar maquina
        is_on = False
    elif choice == 'report':
        # reportes
        coffee_maker.report()
        money_machine.report()
    else:
        # pedir, revisar, pagar cafe
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)          