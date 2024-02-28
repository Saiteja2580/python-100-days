import calc_module
import os
def calculator():
    print(calc_module.logo)
    first_number = int(input("What's the first number?:"))
    for operator in calc_module.operations:
        print(operator)
    operation = input("Pick an Operation : ")
    result = first_number
    j = 0
    while j == 0:
        second_number = int(input("What's the next number?: "))
        calculating_function = calc_module.operations[operation]
        result = calculating_function(result,second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        first_number = result
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == 'y':
            continue
        else:
            os.system('cls')
            calculator()
        
calculator()