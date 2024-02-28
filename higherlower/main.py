from game_data import data
from game_data import winner
import art
import random
import os
print(art.logo)
game_over = False
score = 0
player1 = ""
player2 = ""

for i in range(0,50):
    if game_over == False:
        player1 = f"{data[i]['name']}, {data[i]['description']},from {data[i]['country']}"
        followers_count1 = data[i]['follower_count']
        player2 = f"{data[i+1]['name']}, {data[i+1]['description']},from {data[i+1]['country']}"
        followers_count2 = data[i+1]['follower_count']
        print(f"Compare A : {player1}")
        print(art.vs)
        print(f"Compare B : {player2}")
        user_choice = input("Who has more followers?Type 'A' or 'B' : ")
        win = winner(followers_count1,followers_count2)
        if user_choice in win:
            score = score+1
            os.system('cls')
            print(f"You're right! Current score : {score}")
           
        else:
            os.system('cls')
            print(f"You're wrong! Current score : {score}")
            game_over = True




