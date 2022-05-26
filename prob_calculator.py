import copy
import random

class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      for i in range(v):
        self.contents.append(k)   
    print(self.contents)

  def __str__(self):
    return ', '.join(self.contents)

  def get_contents(self):
    return self.contents
   
  def draw(self, num):
    removed_balls = []
    if num > len(self.contents):
      return self.contents
    else:
      for i in range(num):
        removed_ball = random.choice(self.contents)
        removed_balls.append(removed_ball)
        self.contents.remove(removed_ball)
    return removed_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  n = num_experiments
  m = 0
  
  for i in range(n):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_picked = hat_copy.draw(num_balls_drawn)
    for color in colors_picked:
      if color in expected_copy:
        expected_copy[color] -= 1
    
    if all(s <= 0 for s in expected_copy.values()):
      m += 1

  return m / n