class GameLog:

   def __init__(self, name, hero_class):
    self.name = name
    self.hero_class = hero_class
    self.moves = 0
    self.mobs_killed = []
    self.weapons_used = []

   def record_move(self):
        self.moves += 1

   def record_kill(self, mob):
        self.mobs_killed.append(mob.get_name())

   def record_weapon(self, weapon):
        self.weapons_used.append(weapon.get_name())

  

   def create_report(self, xp):
        report = f"""
========== GAME LOG ==========

Name: {self.name}
Class: {self.hero_class}
Moves: {self.moves}
Mobs killed: {len(self.mobs_killed)}
XP: {xp}

Weapons used:
"""

        for weapon in self.weapons_used:
            report += f"- {weapon}\n"

        report += "\n==============================\n"

        return report

   def save(self, xp):
        report = self.create_report(xp)

        with open("game_log.txt", "a") as file:
            file.write(report)