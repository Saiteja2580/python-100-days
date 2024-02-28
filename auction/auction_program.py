import os
import art

print(art.logo)
choice = 'yes'
auction_dictionary = {}
while choice != "no":
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    auction_dictionary[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.")
    if choice == 'yes':
        os.system('cls')
        continue
art.auction_winner(auction_dictionary)