import random
from hangman_words import words_list
from hangman_words import HANGMANPICS
from logo import logo
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print(logo)
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
j = 0
while j ==0:
  choosen_word = random.choice(words_list)
  len_choosen = len(choosen_word)
  len_entered_word = []
  count = 0

  for i in range(0,len_choosen):
      len_entered_word.append('_')
      




  while '_' in len_entered_word:
      guess_letter = input("Guess a Letter : ")
      if guess_letter in len_entered_word:
          print(f"letter {guess_letter} is already guessed,guess any other letter")
          continue
      if guess_letter in choosen_word:
          for i in range(0,len_choosen):
              if choosen_word[i] == guess_letter :
                  len_entered_word[i] = choosen_word[i]
          print(len_entered_word)
      else:
          count+=1
          print(f"letter {guess_letter} is not in word,you lost a life")
          print(len_entered_word)
          print(HANGMANPICS[count-1])
          if count == 7:
              print("You Lose !! Game Over !!")
              break
          
  if count!= 7:
      print("You Win!!")

  j = int(input("Enter 0 to play again,1 to exit\n"))
    