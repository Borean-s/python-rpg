from heroes import Hero

class Knight(Hero):

  def __init__(self, name):
    super().__init__(
      name = name,
      max_hp = 100,
      damage_multiplier = 1,
      movement_speed = 60
      )

    

