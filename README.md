# transposey

## What is it already?

Small python script that transposes (changes key of) chords found in a text file.
The code is written to solve my particular problem, and notation and might not fit for all.
On the plus side, the script should be easy to modify.

## Usage

Requires Python 3.

`transposey.py filename`

To try it out, use it with provided example file *No more blues.txt*.

## Details

By default it transposes up 5 half tones. This is set inside the script currently. As you also can see in the script there is a certain notation of chords required for the script to work. 

`notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']`

If you are familiar with music notation, you might know that a note can be written in two ways depending on the key of the song. For example: Db is also known as C# and G# is often written Ab. The script currently only support the notes listed above.

If you find use for this script please let me know. It was written for own consumption primarily :)
