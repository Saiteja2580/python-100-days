import random

cards = [2,3,4,5,6,7,8,9,10,10,10,11]


#first two card of user and dealer
def first_card(list):
    for i in range(0,2):
        list.append(random.choice(cards))

#to calculate score
def score_calc(list):
    score = 0
    for i in range(0,len(list)):
        score = score+list[i]
    if score == 21 and 11 in list:
        score = score-11+1
        for i in range(len(list)):
            if list[i] == 11:
                list[i] = 1
        return score
    else:
        return score
    


def game_winner(score_user,score_dealer):
    if score_user > score_dealer:
        return "user"
    elif score_user < score_dealer:
        return "dealer"
    elif score_user == score_dealer:
        return "draw"
    

