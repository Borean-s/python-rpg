from heroes import Hero

class Juggernaut(Hero):

  def __init__(self, name):
    super().__init__(
      name = name,
      max_hp = 150,
      damage_multiplier = 1.3,
      movement_speed = 40
      )

    

