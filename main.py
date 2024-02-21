import globals
import logging
from gen.rhythmgen import RhythmGen

r = RhythmGen(4, [1,0.5, 0.25])

while True:
  print(r.rated_phrases)
  generation = r.generate([])
  print(generation)
  i = int(input("Rating: "))
  r.train(generation, i)

