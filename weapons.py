from abc import ABC, abstractmethod

class Wep(ABC):
  def __init__(self, name, wep_damage):
    self.name = name
    self.wep_damage = wep_damage


  def get_name(self):
    return self.name

  def get_wep_damage(self):
    return self.wep_damage


class WoodenSword(Wep):
  def __init__(self):
    super().__init__(
      name = "Wooden Sword",
      wep_damage = 30
      )

class RustyDagger(Wep):
  def __init__(self):
    super().__init__(
      name = "Rusty Dagger",
      wep_damage = 35
      )

class LumberjackAxe(Wep):
  def __init__(self):
    super().__init__(
      name = "Lumberjack Axe",
      wep_damage = 50
      )  

