# Simple script to take a massive list of words, and filter down to only the 5 letter words
# Also uses the alt-profanity-check library https://pypi.org/project/alt-profanity-check/
# in order to try and filter out profanity
# Configured to take the CSW21 (Scrabble valid words) list found here: https://ia803406.us.archive.org/31/items/csw21/CSW21.txt
# Then ranks each word by its frequency using https://pypi.org/project/wordfreq/
# Set to only take words that are somewhat common ( > 2.1 on a scale of 0 to 8)

import sys
import profanity_check
import wordfreq
from profanity_check import predict, predict_prob
from wordfreq import zipf_frequency

with open('CSW21.txt', 'r+') as wordFile: # change me for other file names/sources
    with open('5 Letter Words.txt', 'w') as outputFile:
        try:
            totalLines = wordFile.readlines() # get all the lines
            for line in totalLines: # go through each line
                line = line.rstrip('\n') # strip the newline character off of the line otherwise the lengths are wrong
                #print(line)
                if len(line) == 5: #look at each line and see if it is 5 characters long
                    array = [line] #put the 5 letter word in an array for testing
                    if predict(array) == 0: # use the at-profanity-check library to see if the array (single word) is not offensive
                        frequency = zipf_frequency(line, 'en', wordlist='best') # get a value from 0-8 for how frequent the word is used
                        # print(line + ',' + str(frequency))
                        if frequency > 2.1: #CHANGE ME TO INCLUDE MORE UNCOMMON WORDS IF DESIRED
                            print(line, file=outputFile) # if not offensive and above the commonness cutoff, print it to the output file
                    else:
                        print("Offensive: " + line) # if it is offensive, just print to console for debug purposes
                        
        except Exception as er:
            print('Error: ' + str(er))
