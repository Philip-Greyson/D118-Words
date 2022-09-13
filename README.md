# D118-Words

Simple script to take a massive list of words, and filter down to only the 5 letter words
Also uses the alt-profanity-check library https://pypi.org/project/alt-profanity-check/
in order to try and filter out profanity
Configured to take the CSW21 (Scrabble valid words) list found here: https://ia803406.us.archive.org/31/items/csw21/CSW21.txt
Then ranks each word by its frequency using https://pypi.org/project/wordfreq/
Set to only take words that are somewhat common ( > 2.1 on a scale of 0 to 8)
