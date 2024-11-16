'''
Created on 10/2/2024
@author:   Yahia Abdelsalam
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"
CS115 - Hw 2
'''
import sys

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']



"""
Part 1:
letterScore(letter, scorelist)
- takes a letter and a scrabble score list (where each entry is a list with a list and its score like ["a", 1] and returns the score for that letter
- Check each sublist to see if the letter matches the input letter
"""

def letterScore(letter, scorelist):
    if not scorelist:
        return 0
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

"""
Part 2:
wordScore(S, scorelist)
- Computes the score of an entire word by summing the scores of its individual letters using letterScore
"""

def wordScore(S, scorelist):
    if not S:
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

"""
Part 3:
scoreList(Rack)
- takes a list of letter(the "Rack") and returns a list of words from the dictionary that can be made from the Rack, along with their Scrabble scores
"""

def canMakeWord(word, rack):
    if not word:
        return True
    if word[0] in rack:
        rack_copy = rack[:]
        rack_copy.remove(word[0])
        return canMakeWord(word[1:], rack_copy)
    return False

def scoreListHelper(rack, dictionary):
    if not dictionary:
        return []
    word = dictionary[0]
    rest = dictionary[1:]
    if canMakeWord(word, rack):
        return [[word, wordScore(word, scrabbleScores)]] + scoreListHelper(rack, rest)
    return scoreListHelper(rack, rest)

def scoreList(rack):
    return scoreListHelper(rack, Dictionary)

"""
Part 4:
bestWord(rack)
- Returns the highest scoring word from the rack and its score.
"""

def bestWordHelper(words_with_scores, best):
    if not words_with_scores:
        return best
    word, score = words_with_scores[0]
    if score > best[1]:
        return bestWordHelper(words_with_scores[1:], [word, score])
    return bestWordHelper(words_with_scores[1:], best)

def bestWord(rack):
    return bestWordHelper(scoreList(rack), ["", 0])

# Test cases:
print(letterScore("c", scrabbleScores))  
print(letterScore("a", scrabbleScores))  
print(wordScore('spam', scrabbleScores))  
print(scoreList(["a", "s", "m", "t", "p"]))  
print(bestWord(["a", "s", "m", "t", "p"]))  

























