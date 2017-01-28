import sys

# + 5 half steps
steps = 5

# Some notes are written relative to song key, e.g. Db => C#, G# => Ab
# Please adapt for your own needs
notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']

# To be able to keep multiple notes on same index value:
notesHash = {\
'C':   0, \
'C#':  1, 'Db':  1, \
'D':   2, \
'D#':  3, 'Eb':  3, \
'E':   4, \
'F':   5, \
'F#':  6, 'Gb':  6, \
'G':   7, \
'G#':  8, 'Ab':  8, \
'A':   9, \
'Bb': 10, \
'B':  11, 'H':  11 \
}

def transpose(note):
	try:
		noteIdx = notesHash[note]
		notesLen = len(notes)
		newIdx = (noteIdx + steps) % notesLen
		note = notes[newIdx]
	except ValueError:
		pass
	return note
	
def isNote(char):
	return (char >= 'A') and (char <= 'H')

def getfullNote(line, pos):
	# check sharp or flat
	if (pos + 1 < len(line)) and line[pos + 1] in ['#', 'b']:
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
	lines = f.readlines()
	sys.stdout.write(lines[0])
	lines = lines[1:]
	f.close()
except:
	sys.stderr.write("File '%s' not found" % filename)
	sys.exit()


for line in lines:
	currentPos = 0 # current position on the input line
	line = line.strip()
	lineLen = len(line)
	
	# Flags used to compensate whitespace when replacing a note of different length.
	# This way your text file won't get crooked
	hasSavedSpace = False 
	hasSavedSpaceSkip = False

	while currentPos < lineLen:
		char = line[currentPos]
		if isNote(char):
			note = getfullNote(line, currentPos)
			oldNoteLen = len(note)
			char = transpose(note)
			newNoteLen = len(char)
			currentPos += len(note)

			# to keep indentation straight
			if newNoteLen < oldNoteLen:
				hasSavedSpace = True
			elif oldNoteLen < newNoteLen:
				hasSavedSpaceSkip = True

		else:
			if char == ' ':
				if hasSavedSpace:
					char = '  '
					hasSavedSpace = False
				elif hasSavedSpaceSkip:
					char = ''
					hasSavedSpaceSkip = False
			currentPos += 1

		sys.stdout.write(char)
	sys.stdout.write("\n")

sys.stdout.flush()	
