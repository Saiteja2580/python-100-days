class Coffee_Machine:
    # data memeners 
    MENU = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                    "milk"  : 0
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
    
    # resources that machine has
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money" : 0
    }


    # printing resources
    def print_resources(self):
        for key in self.resources:
            if key == "water":
                print(f"{key} : {self.resources[key]}ml")
            if key == "milk":
                print(f"{key} : {self.resources[key]}ml")
            if key == "coffee":
                print(f"{key} : {self.resources[key]}g")
            if key == "money":
                print(f"{key} : ${self.resources[key]}")


    # to calculate money enterd by customer and prints whether transaction succesfful or not successful
    #if successful prints enjoy your cofee else money not sufficent
    def calculating_money(self,string):
        print("Insert the coins.")
        quarters = float(input("How many quarters?: "))
        money_dollars = quarters * 0.25
        penny = float(input("How many penny?: "))
        money_dollars = money_dollars+penny*0.01
        nickel = float(input("How many nickel?: "))
        money_dollars = money_dollars+nickel*0.05
        dime = float(input("How many dime?: "))
        money_dollars = money_dollars+dime*0.10
        change = self.checking_money(string,money_dollars)
        if change == 0:
            print(f"Sorry, Money is not sufficient,Money refunded!")
        else:
            print(f"Here is ${round(change,2)} in change.")
            print(f"Here is your {string} 🍵 Enjoy!")

    
    #will check entered item resources with machine resources if resources are enough return empty lacking list and updates the resources 
    # or else return lacking list

    def checking_resourse(self,string):
       lacking_list = []
       if self.MENU[string]["ingredients"]["water"] > self.resources["water"]:
           lacking_list.append("water")
       if self.MENU[string]["ingredients"]["milk"] > self.resources["water"]:
           lacking_list.append("milk")
       if self.MENU[string]["ingredients"]["coffee"] > self.resources["coffee"]:
           lacking_list.append("coffee")
       if lacking_list == []:
           self.resources["water"] = self.resources["water"]-self.MENU[string]["ingredients"]["water"]
           self.resources["milk"] = self.resources["milk"]-self.MENU[string]["ingredients"]["milk"]
           self.resources["coffee"] = self.resources["coffee"]-self.MENU[string]["ingredients"]["coffee"]
       return lacking_list
    


    #it checker wheyher money entered by user is sufficient price for coffe making or not
    def checking_money(self,string,user_cost):
        if self.MENU[string]["cost"] > user_cost:
            return 0
        else :
            self.resources["money"] = self.resources["money"]+self.MENU[string]["cost"]
            return user_cost-self.MENU[string]["cost"]
        




    





















