from abc import ABC, abstractmethod

from weapons import Wep, WoodenSword

class Hero(ABC):
  def __init__(
      self, 
      name, 
      max_hp: int, 
      damage_multiplier: float, 
      movement_speed: int, 

      
      ):

    self.name = name
    self.max_hp = max_hp
    self.current_hp = self.max_hp
    self.damage_multiplier = damage_multiplier
    self.movement_speed = movement_speed
    self.weapon = WoodenSword()
    
  def get_Name(self):
    return self.name

  def get_damage(self):
    return self.damage

  def get_damageMultiplier(self):
    return self.damage_multiplier 

  def get_weapon(self):
    return self.weapon

  def get_movementSpeed(self):
    return self.movement_speed

  def get_maxHP(self):
    return self.max_hp

  def get_currentHP(self):
    return self.current_hp

  def get_class(self):
    return self.__class__.__name__

  def calculate_damage(self, weapon):
    return self.damage_multiplier * weapon.get_wep_damage()

 # def take_damage(self, damage: int):
