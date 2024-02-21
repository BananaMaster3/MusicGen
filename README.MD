# MusicGen
A python ai-like algorythm to generate both melodies and rhythms.

## Maintaining
### File structure
*I'm aware that the definitions of different classes in the `types` folder aren't technically accurate in normal music theory, but those are the definitions for this algorythm*
 - `main.py` - Displays terminal interface to guide user through generation process
 - `globals.py` - List of globals (note frequency, etc.)
 - 📁 `types` - Contains different classes needed for generation
     - interval.py - Contains class for an interval (two notes played in succession)
     - note.py - Contains class for a note (a pitch played for a certain amount time)
### Customs
As a rule of thumb, notes are passed not as pitches but as indexs in the `notes` list in `globals.py`.