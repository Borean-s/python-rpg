from abc import ABC, abstractmethod

class Wep(ABC):
  def __init__(self, name, wep_damage):
    self.name = name
    self.wep_damage = wep_damage


  def get_damage(self):
    return self.damage

  