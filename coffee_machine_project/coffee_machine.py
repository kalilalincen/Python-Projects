
#funtion to check resources
def is_resource_enough(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

#function to calculate money
def process_coins():
  print("Please insert coins.")
  total = int(input("How many quarters?: ")) * 0.25
  total += int(input("How many dimes?: ")) * 0.1
  total += int(input("How many nickles?: ")) * 0.05
  total += int(input("How many pennies?: ")) * 0.01
  return total

#function to check transaction successful
def is_payed(money_received, drink_cost):
  #if yes
  if money_received >= drink_cost:
    #provice change
    change = round(money_received-drink_cost, 2)
    print(f"Here is ${change} dollars in change.")
    #add to profit
    global profit
    profit += drink_cost
    return True
  #if not
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False

#funtion to make coffee
def make_coffee(drink, order_ingredients):
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Here is your {drink} Enjoy! ☕")

#function to add resources
def add_resources(order_ingredients):
  for item in order_ingredients:
    resources[item] += order_ingredients[item]
    if resources[item] > 500:
      resources[item] = 500
      if item == "water" or "milk":
        print(f"This coffee machine can store maximun 500ml of {item}.")
      else:
        print(f"This coffee machine can store maximun 200g of {item}.")
  print(f"You have added ingredients suceessfully.")
  
#pre-define
menu = {
  "espresso": {"ingredients": {"water":50, "coffee":18}, "cost":1.5,},
  "latte": {"ingredients": {"water":200, "milk":150, "coffee":24}, "cost":2.5},
  "cappuccino": {"ingredients": {"water":250, "milk":100, "coffee":24}, "cost":3.0},
}
resources = {"water":300, "milk":200, "coffee":100}
profit = 0

#on & off buttom
is_on = True

#when it is on
while is_on:
  #take input
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  
  #secret command to turn off the machine
  if choice == "off":
    is_on = False
    
  elif choice == "report":
    print(f"""Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}""")
  
  elif choice == "add":
    add_ingredients = {}
    #take input of how many adding
    add_water = int(input("how many ml of water you wish to add?: "))
    add_ingredients['water'] = add_water
    add_milk = int(input("how many ml of milk you wish to add?: "))
    add_ingredients['milk'] = add_milk
    add_coffee = int(input("how many g of coffee you wish to add?: "))
    add_ingredients['coffee'] = add_coffee
    #call add function and print result
    add_resources(add_ingredients)
    print(f"""Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}""")
    
  else:
    drink = menu[choice]
    if is_resource_enough(drink["ingredients"]):
      payment = process_coins()
      if is_payed(payment, drink['cost']):
        make_coffee(choice, drink["ingredients"])
        
      
      
    
    
  
    
  