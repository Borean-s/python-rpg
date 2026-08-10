
from knight import Knight
from juggernaut import Juggernaut
from scout import Scout
import random

def get_name():
 
 while True:
    name = input("Enter your name, Warrior!\n").strip().title() 
    if name and len(name) < 12:
      break
    else:
      print("Your name cannot be longer than 12 characters!")

 return name

hero_classes = {1: Knight, 2: Juggernaut, 3: Scout}
def choose_hero(name):

  while True:

    print("\n***********")
    print("1- Knight")
    print("2- Juggernaut")
    print("3- Scout")
    print("***********\n")

    try:
      choice = int(input(f"Choose your character, {name}!\n"))

      if choice in (1, 2, 3):
        break
      else:
        print("Please enter a number between 1 and 3.\n")

    except ValueError:
      print("Please enter a valid number.\n")
  chosen_hero = hero_classes[choice](name)
  return chosen_hero


def get_encounter():
  dice = random.randint(1, 100)

  if dice <= 30:
    return "none"
  elif dice <= 60:
    return "hostile"
  elif dice <= 90:
    return "chest"
  else:
    return "docile" 
  
def proceed():

  while not game_over:

    print("\n")



def main():

  user_name = get_name()


  player = choose_hero(user_name)

  print(player.get_name())
  
if __name__ == "__main__":
  main()