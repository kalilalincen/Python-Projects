from replit import clear
from auction_art import logo

#Print welcoming logo
print(logo)

#Create empty dictionary
bids = {}
#End bidding
end_bidding = False

#Function to find highest bidder
def highest(bids_record):
  
  highest_bid = 0
  
  for bidder in bids_record:
    amount = int(bids_record[bidder])
    
    if amount > highest_bid:
      highest_bid = amount
      winner = bidder
  
  print(f"The winner is {winner} with a bid of ${highest_bid}.")
  
  
#Loop
while end_bidding == False:
  
  #Take inputs
  name = input("What is your name?: ")
  price = input("What is your bid?: $")

  #Add inputs to bids dictionary
  bids[name] = price
  
  #Ask if more bidder
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  
  if should_continue == "no":
    end_bidding = True
    highest(bids)
  elif should_continue == "yes":
    clear()
