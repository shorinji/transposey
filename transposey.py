import sys

# + 5 half steps
steps = 5

# Some notes are written relative to song key, e.g. Db => C#, G# => Ab
# Please adapt for your own needs
notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']

def transpose(note):
	try:
		noteIdx = notes.index(note)
		notesLen = len(notes)
		newIdx = (noteIdx + steps) % notesLen
		note = notes[newIdx]
	except ValueError:
		print("ERROR invalid note ", note)
	return note
	
def isNote(line, pos):
	if line[pos:pos + 3] in ['Dim', 'Maj']:
		return False

	char = line[pos]

	return (char >= 'A') and (char <= 'G')

def getfullNote(line, pos):
	lineLen = len(line)
	# check sharp or flat
	if (pos + 1 < lineLen) and line[pos + 1] in ['#', 'b']:
		endPos = pos + 2
	else:
		endPos = pos + 1

	return line[pos:endPos]



if len(sys.argv) < 2:
	sys.stderr.write("Usage: %s filename" % sys.argv[0])
	sys.exit()

filename = " ".join(sys.argv[1:])

try:
	f = open(filename)
	lines = f.readlines()[1:] # skips first line (song title)
	f.close()
except:
	sys.stderr.write("File '%s' not found" % filename)
	sys.exit()


for line in lines:
	currentPos = 0
	line = line.strip()
	lineLen = len(line)
	
	# Flags used to compensate whitespace when replacing a note of different length.
	# This way your text file won't get crooked
	hasSavedSpace = False 
	hasSavedSpaceSkip = False

	while currentPos < lineLen:
		
		if isNote(line, currentPos):
			note = getfullNote(line, currentPos)
			oldNoteLen = len(note)
			char = transpose(note)
			newNoteLen = len(char)
			currentPos += len(note)

			if newNoteLen < oldNoteLen:
				hasSavedSpace = True
			elif oldNoteLen < newNoteLen:
				hasSavedSpaceSkip = True

		else:
			char = line[currentPos]
			if char == ' ':
				if hasSavedSpace:
					char = '  '
					hasSavedSpace = False
				elif hasSavedSpaceSkip:
					char = ''
					hasSavedSpaceSkip = False

			currentPos += 1

		sys.stdout.write(char)
	print()

sys.stdout.flush()	
