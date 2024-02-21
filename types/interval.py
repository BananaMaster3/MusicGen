import globals
from note import Note

class Interval:
    def __init__(self, note1: Note, note2:Note) -> None:
        self.note1 = note1
        self.note2 = note2
        self.difference = note1.get_interval_to(note2)