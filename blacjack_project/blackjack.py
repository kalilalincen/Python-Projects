import random
import blackjack_art

#Function to randomly choose a card and add to card list
def deal_card():
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Function to calculate the score of the card list
def calculate_score(cards):
  
  #If the sum of the cards are 21 and only two cards
  if sum(cards) == 21 and len(cards) == 2:
    #Blackjack
    return 0
  #If there is an A card (11 points) and sum > than 11, A card would = 1 point only
  if 11 in cards and sum(cards) > 11:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Function to compare the score
def compare(user_score, compuer_score):
  if user_score == compuer_score:
    return "Draw 🤷🤷🤷"
  elif compuer_score == 0:
    return "Lose, the opponent has Blackjack 😨😨😨"
  elif user_score == 0:
    return "Win with a Blackjack 😎😎😎"
  elif user_score > 21:
    return "You went over 21. You lost 😕😕😕"
  elif compuer_score > 21:
    return "The opponet went over 21. You win 😏😏😏"
  elif user_score > compuer_score:
    return "Your score is higher. You win 😜😜😜"
  else:
    return "You score is lower. You lost ☹️☹️☹️"

#Function to add all function into a game
def play_game():
  #Pre-define
  user_cards = []
  computer_cards = []
  end_game = False

  #Loop to deal card, 2 cards per role
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not end_game:
    #Calculationg score
    user_score= calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    #Print score info of each role
    print("\n###################################################################\n")
    print(f"You cards: {user_cards}, current socre: {user_score}")
    print(f"The opponent's card: [{computer_cards[0]}, ❓] current socre: ❓\n")
    print("###################################################################\n")
    #print(f"Computer's card: {computer_cards}, current socre: {computer_score}")
      
    #Decide end game if winner
    if user_score==0 or computer_score==0 or user_score > 21 or computer_score > 21:
      end_game = True

    #Decide deal card again if no winner
    else:
      user_next_deal = input("Type 'y' to get another card, otherwise type 'n' to pass: ")
      if user_next_deal == "y":
        print(f"\nYou has decided to  deal a new card...\n")
        user_cards.append(deal_card())
      else:
        print(f"\nYou has decided to stand.\n")
        end_game = True

  #Compuer decide if deal new card
  while calculate_score != 0 and computer_score < 17:
    print(f"The opponent has decide to deal a new card...")
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  #Print final result
  
  print("\n###################################################################\n")
  print("⚠️  Ｆｉｎａｌ　Ｒｅｓｕｌｔ⚠️\n")
  print(f"Your final hand: {user_cards}, final score: {user_score}        ")
  print(f"The opponent's final hand: {computer_cards}, final score: {computer_score}")
  print("\n###################################################################\n")

  print(compare(user_score, computer_score))
  
#Print welcome logo
print(blackjack_art.logo)

#Should repeat game?
while input ("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
  
  