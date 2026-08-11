
from knight import Knight
from juggernaut import Juggernaut
from mobs import Goblin, Gorilla, Grizzly, Rabbit, Sheep, Trader, Wolf
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
      choice = int(input(f"Choose your character!\n"))

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

def encounter_hostile():
  dice = random.randint(1, 100)

  if dice <= 40:
    wolf = Wolf()
    return wolf
  elif dice <= 50:
    gorilla = Gorilla()
    return gorilla
  elif dice <= 85:
    goblin = Goblin()
    return goblin
  else:
    grizzly = Grizzly()
    return grizzly
 
    
def encounter_docile():
  dice = random.randint(1, 100)
  if dice <= 30:
    trader = Trader()
    return trader
  elif dice <= 60:
    rabbit = Rabbit()
    return rabbit
  else:
    sheep = Sheep()
    return sheep

def encounter_chest():
  dice = random.randint(1, 100)

  if dice <= 30:
    print("You found a chest!")
  if dice <= 60:
    print("You found a locked chest!")
  else:
    print("You found a diamond chest!")

def proceed(player):

  

  print("\n")

  dice = random.randint(1, 100)

  if dice <= 50:
    encounter = get_encounter()

    if encounter == "none":
      print("Luckily you didn't encounter anything.\n")
      while True:
        print("\nType 'proceed' to continue your journey.\n")
        if input().strip().lower() == "proceed":
          break
        else:
          print("Type 'proceed' to continue your journey.\n")

    elif encounter == "hostile":
      hostile_mob = encounter_hostile()
      print(f"\nYou have encountered a {hostile_mob.get_name()}!\nHP: {hostile_mob.get_maxHP()}\n")
      mob_Panel(hostile_mob, player)
    elif encounter == "docile":
      docile_mob = encounter_docile()
      print(f"\nYou have encountered a {docile_mob.get_name()}!\nHP: {docile_mob.get_maxHP()}\n")
      mob_Panel(docile_mob, player)
    elif encounter == "chest":
      encounter_chest()


def mob_Panel(mob, player):

  

  while True:
  
      print(f"\n1- Attack\n2- Run\n3- Check Stats\n4- Check Inventory\n")
      
  
      try:
        choice = int(input())
  
        if choice in (1, 2, 3, 4):
          break
        else:
          print("Please enter a number between 1 and 4.\n")
  
      except ValueError:
        print("Please enter a valid number.\n")
  
  match choice:
    case 1:
      attack_mob(mob, player)
    case 2:
      print("You run away from the mob!")
    case 3:
      print("You check your stats!")
    case 4:
      print("You check your inventory!")  

def attack_mob(mob, player):

  print(f"You attacked the {mob.get_name()}!\n")
  print(f"You deal {player.calculate_damage(player.get_weapon())} damage to the {mob.get_name()}!\n")
  mob.current_hp -= player.calculate_damage(player.get_weapon())
  if mob.get_currentHP() <= 0:
    print(f"You have defeated the {mob.get_name()}!")
    return 
  else:
   print(f"The {mob.get_name()} has {mob.get_currentHP()} HP left!")
  mob_Panel(mob, player)

def main():

  user_name = get_name()

  player = choose_hero(user_name)

  print(f"\nWelcome, {player.get_Name()}! You are a {player.get_class()}.\nHP: {player.get_maxHP()}\nWeapon: {player.get_weapon().get_name()} ({player.calculate_damage(player.get_weapon())} AD)\nMovement Speed: {player.get_movementSpeed()}\n")
  print(f"\nGet ready to embark on your journey, {player.get_Name()}! in Gründelsraum all sorts of unholy creatures await you!\n\nType 'ready' to  proceed.\n")

  while not input().strip().lower() == "ready":
    print("Type 'ready' to continue.\n") 

  while not game_over and not win:
    proceed(player)

  
if __name__ == "__main__":
  game_over = False
  win = False
  main()

  