import game_art
import game_data
import random
#import clear from replit

#Function to format the data
def formatdata(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]

  return (f"{account_name}, a {account_description}, from {account_country}")

#Function to check answer
def check_answer(guess, a_follower, b_follower):
  if a_follower > b_follower:
    return guess == "a"
  else:
    return guess == "b"

#Welcoming art
print(game_art.logo)
score = 0
end_game = False
account_b = random.choice(game_data.data)

while not end_game:
  #Generate random account
  account_a = account_b
  account_b = random.choice(game_data.data)
  #Regenerate B if same
  while account_a == account_b:
    account_b = random.choice(game_data.data)

  #Print info of account
  print(f"Compare A: {formatdata(account_a)}")
  print(game_art.vs)
  print(f"Against B: {formatdata(account_b)}")

  #Take input
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_follower_account = account_a["follower_count"]
  b_follower_account = account_b["follower_count"]

  #clear()
  
  #Check input and print answer
  is_correct = check_answer(guess, a_follower_account, b_follower_account)
  if is_correct:
    score += 1
    print(f"You are right! Current score is {score}.")
  else: 
    end_game = True
    print(f"Sorry, You are wrong! Final score is {score}.")