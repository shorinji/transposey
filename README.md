# transposey

## What is it already?

Small python script that transposes (changes key of) chords found in a text file and write it to standard out.
The code is written to solve my particular problem, and notation and might not fit for all.
On the plus side, the script should be easy to modify.

## Usage

Requires Python 3.

`transposey.py filename`

To try it out, use it with provided example file *No more blues.txt*.


## File format

The files you put through transposey are text files with chords for a song. This sort of file is used commonly used on the internet.
The kind of files compatible with transposey starts with the first line which contains the name of the song. This line is skipped, as are blank lines.
Chords are written in capital letters as such: (C, Db, D, Eb, E, F, F#, G, G#, A, Bb, B). 

If you are familiar with music notation, you might know that a note can be written in different ways depending on the key of the song. For example: Db is also known as C# and G# is often written Ab. The script support multiple variations as input, that should cover all. Since the script is unaware of the key of the song, the transposed note will be correct, although you could consider it using the wrong notation.

The script is quite simple, so it just replaces the characters denoting a chord, in the span of characters A-H.
This means any other text beyond the first line containing these letters will get modified as well. So take care writing things like "dim" with lowercase letters and it will be untouched.

By default the script transposes up 5 half tones, currently configured inside the script.


If you find use for this script please let me know. It was written for own consumption primarily :)
