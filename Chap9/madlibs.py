#! python3

import re
from pathlib import Path

# Open text file and capture contents in a string variable
inputFile = open(Path.cwd()/'madLibs.txt', 'r')
fileText = inputFile.read()

# Find and replace words 'ADJECTIVE', 'NOUN', 'ADVERB', and 'VERB'

# Prior solution for reference:
# fileText = re.sub(r'ADJECTIVE', input('Enter an adjective:\n'), fileText)
# fileText = re.sub(r'NOUN', input('Enter an noun:\n'), fileText)
# fileText = re.sub(r'ADVERB', input('Enter an adverb:\n'), fileText)
# fileText = re.sub(r'VERB', input('Enter an verb:\n'), fileText)

# Refine code to compile a regex object first
textRegexAdj = re.compile(r'ADJECTIVE')
textRegexNoun = re.compile(r'NOUN')
textRegexAdv = re.compile(r'ADVERB')
textRegexVerb = re.compile(r'VERB')

fileText = textRegexAdj.sub(input('Please enter an adjective:\n'), fileText)
fileText = textRegexNoun.sub(input('Please enter an noun:\n'), fileText)
fileText = textRegexAdv.sub(input('Please enter an adverb:\n'), fileText)
fileText = textRegexVerb.sub(input('Please enter an verb:\n'), fileText)

# Print new text to the screen.
print(fileText)

# Write revised text to a new newMadLibs.txt
outputFile = open('newMadLibs.txt', 'w')
outputFile.write(fileText)
