from machine_module import Coffee_Machine

coffee = Coffee_Machine()
menu = ["espresso","latte","cappuccino"]
#coffee.calculating_money()
machine_on = True
while machine_on:
    user_choice = input("What would you like?(espresso/latte/cappuccino): ")
    if user_choice == "report":
        coffee.print_resources()
    elif user_choice in menu:
        if coffee.checking_resourse(user_choice) == []:
            coffee.calculating_money(user_choice)
        else:
            lacked = coffee.checking_resourse(user_choice)
            print(f"Sorry, there is is not enough {lacked[0]}")
    else:
        machine_on = False
