from abc import ABC, abstractmethod
from typing import List
from weapons import LumberjackAxe, RoyalSword, RustyDagger, Twig, Wep, WoodenSword
import random 

from weapons import Wep

class Chest(ABC):
  def __init__(self, name: str, contents: List[Wep], chances):
    self.name = name
    self.contents = contents
    self.chances = chances

  def determine_contents(self):
    return random.choices(self.contents, weights=self.chances, k=1)[0]

  def open(self):
    selected_weapon = self.determine_contents()

    if selected_weapon != "None": 
      weapon = selected_weapon()
      return weapon
    else:
      return "None"

  def get_name(self):
    return self.name


wooden_chest = Chest(
  name = "Wooden Chest",
  contents = [
    WoodenSword,
    RustyDagger,
    Twig,
    LumberjackAxe,
    RoyalSword,
    "None"
  ],
  chances = [
    30, # Wooden Sword
    30, # Rusty Dagger
    10, # Twig
    20,  # Lumberjack Axe
    5,  # Royal Sword
    30  # None
  ]
  )

hidden_chest = Chest(
  name = "Hidden Chest",
  contents = [
    WoodenSword,
    RustyDagger,
    Twig,
    LumberjackAxe,
    RoyalSword,
    "None"
  ],
  chances = [
    10, # Wooden Sword
    10, # Rusty Dagger
    10, # Twig
    30,  # Lumberjack Axe
    15,  # Royal Sword
    10  # None
  ]
  )

royal_chest = Chest(
  name = "Royal Chest",
  contents = [
    WoodenSword,
    RustyDagger,
    Twig,
    LumberjackAxe,
    RoyalSword,
    "None"
  ],
  chances = [
    2, # Wooden Sword
    2, # Rusty Dagger
    1, # Twig
    8,  # Lumberjack Axe
    12,  # Royal Sword
    2  # None
  ]
  )