from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
  def setup(self):
    self.player = Character()
    self.monsters = [
      Goblin(),
      Troll(),
      Dragon()
    ]
    self.monster = self.get_next_monster()
    
  def get_next_monster(self):
    try:
      return self.monsters.pop(0)
    except IndexError:
      return None
    
  def monster_turn(self):
    # check to see if the monster attacks
    # if so, tell the player
      # check if the player wants to dodge
      # if so, see if the dodge is successful
        # if it is, move on
      # if it's not, remove one player hit point
    # if the monster isn't attacking, tell that too
    
  def player_turn(self):
    # let the player attack, rest, or quit
    # if they attack:
      # see if the attack is successful
        # if so, see if the monster dodges
          # if dodged, print that
          # if not dodged, subtract the right num hit points from the monster
        # if not a good attack, tell the player
    # if they rest:
      # call the player.rest() method
    # if they quit, exit the game
    # if they pick anything else, re-run this method
    
  def cleanup(self):
    # if the monster has no more hit points:
      # up the player's experience
      # print a message
      # get a new monster
      
  def __init__(self):
    self.setup()
    
    while self.player.hit_points and (self.monster or self.monsters):
      print(self.player)
      self.monster_turn()
      self.player_turn()
      self.cleanup()
      
    if self.player.hit_points:
      print("You win!")
    elif self.monsters or self.monster:
      print("You lose!")