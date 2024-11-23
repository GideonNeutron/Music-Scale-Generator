#List of the 12 Music Keys
music_notes = ['C','C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

key = input("Enter key: ").capitalize()

#Sort the notes by the key entered
if key in music_notes:
    music_notes = music_notes[music_notes.index(key):] + music_notes[:music_notes.index(key)]
    #print(music_notes)
else:
    print("Invalid key entered.")
    exit()

file_path = 'c:/Users/gideo/OneDrive/Documents/CS 110/Python Exercises/Music dictionary/'

#Read the chord dictionary file and store the chord types and corresponding notes in a dictionary
chord_file = [i.strip() for i in open(file_path + 'Full_Music_chord_types.txt')]

#Create a Chord Dictionary
chord_dict = {}
for line in chord_file:
    line = line.split(': ')
    line[1] = [int(x) for x in line[1] if x.isdigit()]
    chord_dict[line[0]] = [0]+line[1]

#print(chord_dict)

#For reference, see the list below for the various chord types.
'''
['Major', 'Minor', 'Diminished', 'Augmented', 'Dominant 7th', 'Minor 7b5 (Half-diminished)', 
'Fully Diminished 7th', 'Augmented 7th', 'Minor 7th flat 5', 'Half-diminished 7th', 'Major 9th', 
'Minor 9th', 'Dominant 9th', 'Minor 9th flat 5', 'Major 11th', 'Minor 11th', 'Dominant 11th', 
'Minor 11th flat 5', 'Major 13th', 'Minor 13th', 'Dominant 13th', 'Minor 13th flat 5', 
'Major 6th', 'Minor 6th', 'Minor Seventh', 'Major Seventh', 'Minor Seventh Flat Five (Half-Diminished)', 
'Fully Diminished Seventh', 'Major Ninth', 'Minor Ninth', 'Dominant Ninth', 'Minor Ninth Flat Five', 
'Major Thirteenth', 'Minor Thirteenth', 'Dominant Thirteenth', 'Minor Thirteenth Flat Five', 
'Suspended Second', 'Suspended Fourth']
'''

#Input chord type
chord_type = input("Enter chord type: ")

if chord_type in chord_dict:
    chords = [music_notes[i] for i in chord_dict[chord_type]]
    print(f'Notes of chord of key {key} {chord_type} are: {chords}')
else:
    print("Invalid chord type entered.")


