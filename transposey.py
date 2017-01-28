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
	if (pos + 1 < lineLen) and line[pos + 1] in ['#', 'b']:
		char = line[pos:pos + 2]
		#print("XXX found (%s)" % char)
	else:
		char = line[pos]
	return char



if len(sys.argv) < 2:
	sys.stderr.write("Usage: %s filename" % sys.argv[0])
	sys.exit()

filename = " ".join(sys.argv[1:])

try:
	f = open(filename)
	lines = f.readlines()[1:]
	f.close()
except:
	sys.stderr.write("File '%s' not found" % filename)
	sys.exit()


for line in lines:
	line = line.strip()

	if len(line) == 0:
		print()
		continue

	currentPos = 0
	lineLen = len(line)
	hasSavedSpace = False
	hasSavedSpaceSkip = False

	while currentPos < lineLen:
		
		#print("\nINPUT '%s'" % char)
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

	print("")

sys.stdout.flush()	
