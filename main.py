MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_reducer(user_input):
  global resources
  for i in resources:
    if i in MENU[user_input]["ingredients"]:
      resources[i] -= MENU[user_input]["ingredients"][i]

def coin_check():
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickles?: "))
  pennies = int(input("How many pennies?: "))
  total = float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
  return total
  
def resource_check(user_input):
  for i in resources:
    if i in MENU[user_input]["ingredients"]:
      if resources[i] < MENU[user_input]["ingredients"][i]:
        print(f"Sorry there is not enough {i}.")
        return False

machine_continue = True
maintenance_mode = True

money = 0


while machine_continue is True:
  
  user_input = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
  
  if user_input == 'report':
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")
  
  elif user_input == "off":
    print("Shutting down machine.")
    machine_continue = False

  
  elif user_input == "maintenance":
    while maintenance_mode is True:
      print("Machine on maintenance mode!")
      maintain_choice = int(input("Maintenance mode choices are: \n 1. Refill the resources \n 2. Withdraw money \n 3. Return machine to normal operations \n 4. Off machine \n What would you like to do? (enter '1', '2', '3' or '4'): "))
      if maintain_choice == 1:
        refill_choice = input("Do you wish to refill the resources? 'Y' or 'N': ").lower()
        if refill_choice == 'y':
          resources["water"] = 300
          resources["milk"] = 200
          resources["coffee"] = 100
          print("The resources have been refilled! \n")
          maintenance_mode = True
        else:
          print("Goodbye!")
          maintenance_mode = True
      elif maintain_choice == 2:
        print(f"The machine has collected an amount of ${money}.")
        withdraw = input("Do you wish to withdraw this amount? 'Y' or 'N': ").lower()
        if withdraw == 'y':
          money = 0
          print("The collected amount has been withdrawn. \n")
          maintenance_mode = True
        else:
          print(f"The amount {money} will be left in the machine till it is withdrawn. \n")
          maintenance_mode = True
      elif maintain_choice == 3:
        print("Returning machine to normal operational mode. \n")
        maintenance_mode = False
        
      elif maintain_choice == 4:
        print("Shutting down machine. Have a good day! \n")
        maintenance_mode = False
        machine_continue = False

    maintenance_mode = True
  else:
    resource_available = resource_check(user_input)
  
    if resource_available is not False:
      coin_provided = coin_check()
      if coin_provided < MENU[user_input]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        machine_continue = False
      elif coin_provided == MENU[user_input]["cost"]:
        money += coin_provided
        resource_reducer(user_input)
        print(f"Here is your {user_input}. Enjoy!")
        machine_continue = True
      elif coin_provided > MENU[user_input]["cost"]:
        change = coin_provided - MENU[user_input]["cost"]
        money += MENU[user_input]["cost"]
        resource_reducer(user_input)
        print(f"Here is ${change} in change.")
        print(f"Here is your {user_input}. Enjoy!")
        machine_continue = True
  
  

  
  