
import random
import time
from replit import audio

def play_note(note, duration):
  note_to_freq = {
      "C": 262, "D": 294, "E": 330, "F": 349, "G": 392, "A": 440
  }
  audio.play_tone(duration, note_to_freq[note], 0, volume=2)
  time.sleep(duration)


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

r = RhythmGen(4, [1,0.5, 0.25])


while True:
  print(r.rated_phrases)
  generation = r.generate([])
  print(generation)
  def play(g):
    a = 0
    for item in g:
      play_note(["C", "D", "E", "F", "G", "A", "C", "D", "E", "F", "G", "A", "C", "D", "E", "F", "G", "A", "C", "D", "E", "F", "G", "A"][a], item)
      a += 1
  i = input("Press p to play: ")
  while i == "p":
    play(generation)
    i = input("Press p to play again: ")

  i = int(input("Rating: "))
  r.train(generation, i)

