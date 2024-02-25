
#create a words list
#1 randomly choose a word from the word list
#2 ask the player to guess a letter 
#check if the letter the player guessed is one of the letters
##that one the system choosen
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']





#word list
word_list = ["voyeurism", "whizzing", "zombie", "subway", "syndrome", "beekeeper", "sarania"]
#chose random word from list
chosen_word = random.choice(word_list)
print(chosen_word)
#change the chosen word to this format _ _ _ _ _ 
chosen_word_e=[]
for i in range(len(chosen_word)):
    chosen_word_e+="_"
#ask the user to guess the letter 
live = 6  
while not list(chosen_word)==chosen_word_e and live !=0:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if letter == guess:
                chosen_word_e[i]=guess
        print(' '.join(chosen_word_e))
    else:
        live-=1
        print(stages[live])
        if live==0:
           break
        print("try agian")
if "_" not in chosen_word_e :
    print("you win")
else:
    print("you lose")