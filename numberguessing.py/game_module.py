logo = """
  ________                                       _____        _______                  ___.                    
 /  _____/  __ __   ____    ______  ______      /  _  \       \      \   __ __   _____ \_ |__    ____ _______  
/   \  ___ |  |  \_/ __ \  /  ___/ /  ___/     /  /_\  \      /   |   \ |  |  \ /     \ | __ \ _/ __ \\_  __ \ 
\    \_\  \|  |  /\  ___/  \___ \  \___ \     /    |    \    /    |    \|  |  /|  Y Y  \| \_\ \\  ___/ |  | \/ 
 \______  /|____/  \___  >/____  >/____  >    \____|__  /    \____|__  /|____/ |__|_|  /|___  / \___  >|__|    
        \/             \/      \/      \/             \/             \/              \/     \/      \/         
                                                                                                               
"""





def game_function(times,computer):
    count = times
    computer_number = computer
    while count > 0:
        print(f"You have {count} attempts remaining to guess the number.")
        guessed_number = int(input("Make a Guess : "))
        if guessed_number <computer_number:
            print("Too Low!")
            count -=1
            
        elif guessed_number == computer_number:
            print(f"You got it! The answer was {guessed_number}")
            break
        else:
            print("Too High!")
            count-=1
        if count == 0:
            print("You have run out of guesses, you lose.")