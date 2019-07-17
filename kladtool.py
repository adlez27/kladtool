import sys

print("kladtool: spitting input somewhere else")

log = open("C:\\Users\\Mark\\Music\\UTAU\\kladsamp\\wavtool-input.txt", "a")
args = ""
for s in sys.argv:
    args += s + "\n"
log.write(args + "\n")
log.close()

print("kladtool: slapping files together")

import os.path
from os import path
from pydub import AudioSegment

if not (path.exists(sys.argv[1])):
    newfile = AudioSegment.empty()
    newfile.export(sys.argv[1], format="wav")

sound1 = AudioSegment.from_wav(sys.argv[1])
sound2 = AudioSegment.from_wav(sys.argv[2])

combined_sounds = sound1 + sound2
combined_sounds.export(sys.argv[1], format="wav")
