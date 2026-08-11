from abc import ABC, abstractmethod

class Mob(ABC):
  def __init__(
      self, 
      name, 
      max_hp: int, 
      movement_speed: int, 
      damage: int,
      hostility: int,
      xp: int
      ):

    self.name = name
    self.max_hp = max_hp
    self.current_hp = self.max_hp
    self.movement_speed = movement_speed
    self.damage = damage
    self.hostility = hostility
    self.xp = xp

  def get_name(self):
    return self.name

  def get_maxHP(self):
    return self.max_hp

  def get_currentHP(self):
    return self.current_hp

  def get_movementSpeed(self):
    return self.movement_speed

  def get_damage(self):
    return self.damage

  def get_hostility(self):
    return self.hostility

  def get_xp(self):
    return self.xp

class Wolf(Mob):
  def __init__(self):
    super().__init__(
      name = "Forest Wolf",
      max_hp = 30,
      movement_speed = 50,
      damage = 20,
      hostility = 70,
      xp = 10
      )

class Grizzly(Mob):
  def __init__(self):
    super().__init__(
      name = "Grizzly",
      max_hp = 120,
      movement_speed = 40,
      damage = 40,
      hostility = 80,
      xp = 60
      )    


class Goblin(Mob):
  def __init__(self):
    super().__init__(
      name = "Goblin",
      max_hp = 50,
      movement_speed = 120,
      damage = 20,
      hostility = 60,
      xp = 20
      )
      

class Gorilla(Mob):
  def __init__(self):
    super().__init__(
      name = "Gorilla",
      max_hp = 100,
      movement_speed = 60,
      damage = 40,
      hostility = 20,
      xp = 70
      )

class Sheep(Mob):
  def __init__(self):
    super().__init__(
      name = "Sheep",
      max_hp = 40,
      movement_speed = 30,
      damage = 0,
      hostility = 0,
      xp = 5
      )

class Rabbit(Mob):
  def __init__(self):
    super().__init__(
      name = "Rabbit",
      max_hp = 20,
      movement_speed = 150,
      damage = 0,
      hostility = 0,
      xp = 5
      )

class Trader(Mob):
  def __init__(self):
    super().__init__(
      name = "Trader",
      max_hp = 60,
      movement_speed = 40,
      damage = 0,
      hostility = 0,
      xp = 10
      )