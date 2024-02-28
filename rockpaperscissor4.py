def computerPrint(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    else:
        print(scissor)

import random

print("----------------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------")
print("""
__________                  __        __________                                      _________        .__                                
\______   \  ____    ____  |  | __    \______   \_____   ______    ____ _______      /   _____/  ____  |__|  ______  ______ ____ _______  
 |       _/ /  _ \ _/ ___\ |  |/ /     |     ___/\__  \  \____ \ _/ __ \\_  __ \     \_____  \ _/ ___\ |  | /  ___/ /  ___//  _ \\_  __ \ 
 |    |   \(  <_> )\  \___ |    <      |    |     / __ \_|  |_> >\  ___/ |  | \/     /        \\  \___ |  | \___ \  \___ \(  <_> )|  | \/ 
 |____|_  / \____/  \___  >|__|_ \     |____|    (____  /|   __/  \___  >|__|       /_______  / \___  >|__|/____  >/____  >\____/ |__|    
        \/              \/      \/                    \/ |__|         \/                    \/      \/          \/      \/                
                                                                                                                                          """)
print("----------------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------")


j =0
while j==0:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
    computer_choice = random.randint(0,2)
    rock = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """

    paper = """
        _______
    ---'    ____)____         
            ______)  
            _______)
            _______)
    ---.__________)
    """

    scissor = """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """


    if user_choice < 0 or user_choice >= 3:
        print("Entered an invalid number !!")
    else:
        computerPrint(user_choice)
        if (user_choice == 0 and computer_choice == 0) or (user_choice == 1 and computer_choice == 1) or (user_choice == 2 and computer_choice == 2):
            print(f"Computer Choice : {computer_choice}")
            computerPrint(computer_choice)
            print("Match Draw !! ")
        elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
            print(f"Computer Choice : {computer_choice}")
            computerPrint(computer_choice)
            print("User Wins !!")
        elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
            print(f"Computer Choice : {computer_choice}")
            computerPrint(computer_choice)
            print("Computer Wins !!")

    j = int(input("Enter 0 to play again, 1 to exit\n"))


    
