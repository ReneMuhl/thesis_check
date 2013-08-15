#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2do:
# Groß-und Kleinschreibung beim Suchen ignorieren!




import argparse         # parse command line arguments
import os.path          # test if file/dir exists
import fnmatch          # test if filename consists of pattern

# constants
OUTPUT_FILENAME = "expletives_summary.txt"



# Create valid arguments and their outputs in the help
parser = argparse.ArgumentParser(description='Search the thesis of expletives.')
parser.add_argument("thesis_dirname", help="Enter the absolute directory name of the thesis.")
parser.add_argument("expletives_filename", help="Enter the filename of file with the collection of expletives.")
args = parser.parse_args()

print(args.thesis_dirname)
print(args.expletives_filename)


# Check if thesis directory exists and save the path of all LateX files (with the ending of ".tex") in a list
if os.path.isdir(args.thesis_dirname):
    print("Directory with thesis exists!")
    matches = []
    for root, dirnames, filenames in os.walk(args.thesis_dirname):
        for filename in fnmatch.filter(filenames, '*.tex'):
            matches.append(os.path.join(root, filename))
else:
    print("Directory with thesis doesn't exists!")


# Check if expletives file exists and read the content
if os.path.isfile(args.expletives_filename):
    print("File with expletives exists!")
    try:
        with open(args.expletives_filename, 'r') as file:
            expletives = file.read().split(',')
            #print(expletives)
            file.close
    except IOError:
        print("Can not open the file!")
else:
    print("File with expletives doesn't exists!")


# Check if the expletives appear in the found files.

# reset file
with open(OUTPUT_FILENAME, "w") as outputFile:
    outputFile.write("")
    outputFile.close

# open file in matches
for matchedFile in matches:
    matchedFilenameWritten = False
    #print(matchedFile)
    # Check if LaTeX file exists and read the content
    if os.path.isfile(matchedFile):
        #print("matchedFile exists!")
        try:
            with open(matchedFile, 'r') as file:
                content = file.read()
                for expletive in expletives:
                    if content.count(expletive) > 1:
                        with open(OUTPUT_FILENAME, "a") as outputFile:
                            if not matchedFilenameWritten:
                                outputFile.write(matchedFile)
                                matchedFilenameWritten = True
                            print(matchedFile)
                            print(expletive, ":", content.count(expletive), "\n")
                            outputString = str('\n')
                            outputString += expletive
                            outputString += ":"
                            outputString += str(content.count(expletive))
                            outputString = str('\n')
                            outputFile.write(outputString)
                file.close
        except IOError:
            print("Can not open the file!")
    else:
        print("matchedFile", matchedFile, "doesn't exists!")
