import logging

notes = [262, 294, 330, 349, 392, 440]

class Note:
    def __init__(self, index: int = None, pitch: int = None) -> None:
        if index != None:
            self.index = index
            self.pitch = notes[index]
        elif pitch != None:
            self.pitch = pitch
            self.index = notes.index(pitch)
        else:
            raise ValueError("Either index or pitch argument must be passed to create a Note, but neither are passed.")
        logging.info(f"Creating a Note class with a pitch of {pitch} and an index of {index}")
    def get_interval_to(self, other_note) -> int:
        return self.index - other_note.index
