import random

def chunk_list(lst, chunk_size):
  returns = []
  for i in range(0, len(lst), chunk_size):
    if len(lst[i:i + chunk_size]) == chunk_size: returns += [lst[i:i + chunk_size]]
  for i in range(1, len(lst), chunk_size):
    if len(lst[i:i + chunk_size]) == chunk_size: returns += [lst[i:i + chunk_size]]
  for i in range(2, len(lst), chunk_size):
    if len(lst[i:i + chunk_size]) == chunk_size: returns += [lst[i:i + chunk_size]]
  return returns

def list2string(list):
  return "/".join([str(z) for z in list])
def string2list(string):
  return [int(z) for z in string.split("/")]


class RhythmGen:
  def __init__(self, beats: int, allowed_divisions: list) -> None:
    self.allowed_divisions = allowed_divisions
    self.beats = beats
    self.rated_phrases = {}
    self.chunk_size = 3
    

  def generate(self, prelist) -> list:
    # generate rhythm
    rhythm = prelist
    b = 0
    for item in rhythm:
      b += item
    while b < self.beats:
      new_beat = random.choice(self.allowed_divisions)
      rhythm.append(new_beat)
      b += new_beat
    while b > self.beats:
      rhythm.pop()
      b = 0
      for item in rhythm:
        b += item
    print(b)
    print(rhythm)
    if b < self.beats:
      return self.generate(rhythm)




    for chunk in chunk_list(rhythm, self.chunk_size):
      if list2string(chunk) in self.rated_phrases:
        if self.rated_phrases[list2string(chunk)] <= -2:
          return self.generate([])
      else:
        self.rated_phrases[list2string(chunk)] = 0
    return rhythm

  def train(self, rhythm, rating):
    for chunk in chunk_list(rhythm, self.chunk_size):
      if list2string(chunk) in self.rated_phrases:
        self.rated_phrases[list2string(chunk)] += rating
      else:
        self.rated_phrases[list2string(chunk)] = rating