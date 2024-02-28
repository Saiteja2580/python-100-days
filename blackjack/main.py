import blackjack_module
import art
import random
import os

choice = input("Do you want to play again a game of Black Jack,Type 'y' for yes or 'n'?:")
if choice == 'y':
    play_again = True
    os.system('cls')
else:
    play_again = False
while play_again == True:

    print(art.logo)

    # cards list representing 11 cards score as 2-9 as their card numbers,ace-1 or 11,jack,queen,king - 10
    cards = [2,3,4,5,6,7,8,9,10,10,10,11]



    user_card = []
    dealer_card = []
    user_score = 0
    dealer_score = 0

    #to get two cards for dealer and user
    for i in range(0,2):
        if i == 0:
            blackjack_module.first_card(user_card)
        else:
            blackjack_module.first_card(dealer_card)


    #to calculate score of user and dealer


    user_score = blackjack_module.score_calc(user_card)
    dealer_score = blackjack_module.score_calc(dealer_card)

    game_over = False
    while game_over == False:


        # prints first time card value sand score
        print(f"Your cards : {user_card},current score : {user_score}")
        print(f"Computer's first card : {dealer_card[0]}")


        # prints as dealer wins if user have more than 21 score and not having a 11 in its card
        if user_score > 21 and 11 not in user_card:
            print(f"Your final hand : {user_card},final score : {user_score}")
            print(f"Computer's final hand : {dealer_card},final score : {dealer_score}")
            print("You went over. You lose 😤")
            game_over = True

        # prints as dealer wins if user have more than 21 score and not having a 11 in its card
        
        
        #ask user whether to get another card or not if score is less than 21
        if user_score <= 21:
            choice = input(f"Type 'y' to get another card, type 'n' to pass : ")
            if choice == 'y':
                user_card.append(random.choice(cards)) 
                user_score = blackjack_module.score_calc(user_card)
                continue
            else:
                if dealer_score > 16:
                    dealer_score = blackjack_module.score_calc(dealer_card)
                    winner = blackjack_module.game_winner(user_score,dealer_score)
                else:
                    dealer_card.append(random.choice(cards))
                    dealer_score = blackjack_module.score_calc(dealer_card)
                    winner = blackjack_module.game_winner(user_score,dealer_score)

                    if dealer_score > 21 and 11 not in dealer_card:
                        print(f"Your final hand : {user_card},final score : {user_score}")
                        print(f"Computer's final hand : {dealer_card},final score : {dealer_score}")
                        print("Opponent went over . You Win 😃")
                        break

                   
                # checks who is winnwe and display the winner
                if winner == "user":
                        print(f"Your final hand : {user_card},final score : {user_score}")
                        print(f"Computer's final hand : {dealer_card},final score : {dealer_score}")
                        print("You Win 😃")
                        game_over = True
                elif winner == "dealer":
                        print(f"Your final hand : {user_card},final score : {user_score}")
                        print(f"Computer's final hand : {dealer_card},final score : {dealer_score}")
                        print("You lose 😤")
                        game_over = True
                else:
                        print(f"Your final hand : {user_card},final score : {user_score}")
                        print(f"Computer's final hand : {dealer_card},final score : {dealer_score}")
                        print("Match Draw 😒")
                        game_over = True



                
        
    # to ask user to play again a agme or  not
    choice = input("Do you want to play again a game of Black Jack,Type 'y' for yes or 'n'?:")
    if choice == 'y':
        play_again = True
        os.system('cls')
    else:
        play_again = False
