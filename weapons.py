from abc import ABC, abstractmethod

class Wep(ABC):
  def __init__(self, name, wep_damage, accuracy):
    self.name = name
    self.wep_damage = wep_damage
    self.accuracy = accuracy


  def get_name(self):
    return self.name

  def get_wep_damage(self):
    return self.wep_damage

  def get_accuracy(self):
    return self.accuracy


class WoodenSword(Wep):
  def __init__(self):
    super().__init__(
      name = "Wooden Sword",
      wep_damage = 30,
      accuracy = 80
      )

class RustyDagger(Wep):
  def __init__(self):
    super().__init__(
      name = "Rusty Dagger",
      wep_damage = 35,
      accuracy = 100
      )

class LumberjackAxe(Wep):
  def __init__(self):
    super().__init__(
      name = "Lumberjack Axe",
      wep_damage = 50,
      accuracy = 60
      )  

class Twig(Wep):
  def __init__(self):
    super().__init__(
      name = "Twig",
      wep_damage = 10,
      accuracy = 95
      )  

class RoyalSword(Wep):
  def __init__(self):
    super().__init__(
      name = "Royal Sword",
      wep_damage = 80,
      accuracy = 85
      )  


