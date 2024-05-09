import random
import hangman_words
import hangman_art

#Create welcome animation
print(hangman_art.logo)

#Randomly choose a word from the word_list
chosen_word = random.choice(hangman_words.word_list)

#Pre define variables
lw = len(chosen_word)
lives = lw
display = []

#Print display _ _ _ _ _ according to the length of chosen_word
for _ in chosen_word:
  display.append("_")

print(f"Welcome to the Harry Potter edition of Hangman Game. This word has {lw} letter.")
print(display, end="\n\n")

#Use loop to repeat the game
end_game = False
while not end_game:
  
  #Take input and assign it to a variable called guess. Make guess lowercase.
  guess = input("Guess a letter: ").lower()
  
  #Check if match letter by letter
  for i in range(lw):
    letter = chosen_word[i]
    if letter == guess:
      display[i] = letter
  
  print(display)
  
  #If not match, reduce lives by 1
  if guess not in chosen_word:
    print(hangman_art.stages[lives])
    print(f"You guessed {guess}, that's not in the word. You lost a life.\n")
    lives-=1
    #If no lives, end the game
    if lives == 0:
      end_game = True
      print("Sorry, you lost.")
      
  
  #Chech if repeat correct input
  if guess in display:
    print("This is a correct answer.\n")

  
  #check if any "_" left, if not, end the game
  if "_" not in display:
    end_game = True
    print(hangman_art.house)
    print("Congratulations! You have won 100 points for your house!\n")
    