from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from money_machine import MoneyMachine

mc=MoneyMachine()
cm=CoffeeMaker()
m=Menu()
# mi=MenuItem()

ison=True
while ison:
    option=m.get_items()
    choice=input(f"What would you like to drink? ({option})")
    if choice=='off':
        ison=False
    elif choice=='report':
        cm.report()
        mc.report()
    else:
        drink=m.find_drink(choice)
        if cm.is_resource_sufficient(drink) and mc.make_payment(drink.cost):
                cm.make_coffee(drink)

        
