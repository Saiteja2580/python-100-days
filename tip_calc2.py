print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip = (total_bill/100)*tip_percent
total_bill = total_bill+tip
persons = int(input("How many people to split the bill? "))
bill_per_each = round(total_bill/persons,2)
print(f"Each person should pay : ${bill_per_each}")