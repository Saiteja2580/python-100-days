import os

logo = """
    ___________
   \\         /
    )_______(
    |\"\"\"\"\"\"\"\"|_.-._,.---------.,_.-._
    |       | | |               | | ''-.
    |       |_| |_             _| |_..-'
    |_______| '-' `'---------'` '-'
    )\"\"\"\"\"\"\"(
   /_________\\
   `'-------'`
 .-------------.
/_______________\\
`-'           `-'
"""

def auction_winner(dictionary):
    highest_amount = 0
    winner = ""
    for key in dictionary:
        if dictionary[key] > highest_amount:
            highest_amount = dictionary[key]
            winner = key
    os.system('cls')
    print(f"The winner is {winner} with highest bid of ${highest_amount}.")
